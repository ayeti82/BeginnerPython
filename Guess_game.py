import random

if __name__ == '__main__':
    print("Range of the game 1-20\nYou have 9 guesses in total")
    chances = 9
    num = random.randint(1, 20)
    won = False
    while chances>0:
        print("Enter your guess:")
        guess = int(input())
        if guess == num:
            print("You have won")
            won = True
            break
        else:
            chances -= 1
            if chances != 0:
                print("Try again!\nYou have ", chances,"chances left")

    if not won:
        print("You lose! The number was", num)
    print("[Program terminates]")