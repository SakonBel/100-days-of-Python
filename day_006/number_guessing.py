import random
from os import system


def clear(): return system("clear")


print("Welcome to the number guessing game!\n")

playing = True

while playing:
    secret_number = random.randint(1, 100)
    life = 0
    difficult = input(
        "Choose the difficulty level - easy(e) or hard(h) : ").lower()
    if difficult == "h":
        life = 5
    elif difficult == "e":
        life = 10

    clear()
    guess_number = ""
    while (not guess_number == secret_number) and (not life == 0):
        print(f"Your life count : {life}")
        guess_number = int(input("Guess the secret number! : "))
        if guess_number > secret_number:
            life -= 1
            clear()
            print("Too high.\nGuess again!\n")
        elif guess_number < secret_number:
            life -= 1
            clear()
            print("Too low. \nGuess again!\n")

    if life == 0:
        clear()
        print("GAME OVER!")
        print(f"You lose!!! the secret number is : {secret_number}")
        try_again = input("Do you want to try again? (Y or N) : ").lower()

        if try_again == "n":
            clear()
            print("Thank you for playing!")
            playing = False

    if guess_number == secret_number:
        clear()
        print("GAME OVER!")
        print("You win!!!")
        try_again = input("Do you want to try again? (Y or N) : ").lower()

        if try_again == "n":
            clear()
            print("Thank you for playing!")
            playing = False
