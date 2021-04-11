import pygame
import random
import os

pygame.mixer.init()
pygame.init()

clock = pygame.time.Clock()

screen_width = 900
screen_height = 500

# Create Window
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ayeti's Snake Game")

backgroundImage = pygame.image.load("sprites/bg.png")
backgroundImage = pygame.transform.scale(backgroundImage, (screen_width, screen_height)).convert_alpha()
welcomeScreenImage = pygame.image.load("sprites/ws.png")
welcomeScreenImage = pygame.transform.scale(welcomeScreenImage, (screen_width, screen_height)).convert_alpha()
gameOverImage = pygame.image.load("sprites/go.png")
gameOverImage = pygame.transform.scale(gameOverImage, (screen_width, screen_height)).convert_alpha()

backgroundMusic = pygame.mixer.Sound("audio/backgroundm.wav")
eatingMusic = pygame.mixer.Sound("audio/eatingm.wav")
gameOverMusic = pygame.mixer.Sound("audio/gameoverm.wav")


font = pygame.font.SysFont("arial", 30)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gW, color, snk_coord_list, w):
    for x, y in snk_coord_list:
        pygame.draw.rect(gW, color, [x, y, w, w])


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

pygame.display.update()


def welcome():
    backgroundMusic.play()
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        gameWindow.blit(welcomeScreenImage, (0, 0))
        text_screen("Welcome to Ayeti's Snake Game", black, screen_width/5, screen_height/5)
        text_screen("Press Space Bar to start the game", black, screen_width/5, screen_height/5+50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                backgroundMusic.stop()
                gameloop()
        pygame.display.update()
        clock.tick(32)

    pygame.quit()
    quit()


def gameloop():
    fps = 32
    snake_x = screen_width / 2
    snake_y = screen_height / 2
    dx = 0
    dy = 0
    initial_vel = 5
    snake_size = 10
    snake_coord_list = []
    snake_length = 1

    food_x = random.randint(20, screen_width - 20)
    food_y = random.randint(50, screen_height - 20)

    score = 0
    if not os.path.exists("HighScore.txt"):
        with open("HighScore.txt", "w") as f:
            f.write("0")

    with open("HighScore.txt", "r") as f:
        highScore = f.read()

    exit_game = False
    game_over = False

    while not exit_game:
        if game_over:
            with open("HighScore.txt", "w") as f:
                f.write(str(highScore))
            backgroundMusic.stop()
            gameOverMusic.play()
            gameWindow.fill(white)
            gameWindow.blit(gameOverImage,(0, 0))
            text_screen("Press Enter to restart", red, 0, 0)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    gameOverMusic.stop()
                    welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        dx = initial_vel
                        dy = 0
                    if event.key == pygame.K_LEFT:
                        dx = -initial_vel
                        dy = 0
                    if event.key == pygame.K_UP:
                        dy = -initial_vel
                        dx = 0
                    if event.key == pygame.K_DOWN:
                        dy = initial_vel
                        dx = 0
            snake_x += dx
            snake_y += dy

            if abs(food_x - snake_x) < 8 and abs(food_y - snake_y) < 8:
                eatingMusic.play()
                score += 1
                food_x = random.randint(20, screen_width - 20)
                food_y = random.randint(50, screen_height - 20)
                snake_length += 5
                if score > int(highScore):
                    highScore = score

            gameWindow.fill(white)
            gameWindow.blit(backgroundImage, (0, 0))
            text_screen("Score: " + str(score) + " High Score: " + str(highScore), red, 10, 10)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_coord_list.append(head)

            if len(snake_coord_list) > snake_length:
                del snake_coord_list[0]

            if snake_x < 0 or snake_x > screen_width \
                    or snake_y > screen_height or snake_y < 0 \
                    or head in snake_coord_list[:-1]:
                game_over = True

            plot_snake(gameWindow, black, snake_coord_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


welcome()
