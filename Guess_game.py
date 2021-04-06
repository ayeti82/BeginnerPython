import random


def guess_closeness(g, n):
    print("Hint:\tWinning number is lower") if g > n else print("Hint:\tWinning number is higher")

    
if __name__ == '__main__':
    print("Range of the game 1-20\nYou have 5 guesses in total")
    chances = 5
    num = random.randint(1, 20)
    won = False
    while chances > 0:
        print("Enter your guess:")
        guess = int(input())
        if guess == num:
            print("You have won")
            won = True
            break
        else:
            chances -= 1
            if chances != 0:
                guess_closeness(guess, num)
                print("Try again!\t[Chances:", chances, "]")

    if not won:
        print("You lose! The number was", num)
    print("[Program terminates]")
