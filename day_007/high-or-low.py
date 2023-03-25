from os import system
from time import sleep
import random


def clear(): return system("clear")


# Welcome the player to the game
clear()
print("""    __  ___       __                     __                     
   / / / (_)___ _/ /_     ____  _____   / /   ____ _      __    
  / /_/ / / __ `/ __ \   / __ \/ ___/  / /   / __ \ | /| / /    
 / __  / / /_/ / / / /  / /_/ / /     / /___/ /_/ / |/ |/ /     
/_/ /_/_/\__, /_/ /_/   \____/_/     /_____/\____/|__/|__/      
        /____/                                                  
""")
print("Welcome to the High-or-Low Game!!")
sleep(2)

# Set initial value for playing
playing = True
while playing:
    right = True
    score = 0
    secret_number = random.randint(1, 100)
    initial_number = random.randint(1, 100)

    while right:
        # let the player choose to input high or low
        clear()
        print("""    __  ___       __                     __                     
   / / / (_)___ _/ /_     ____  _____   / /   ____ _      __    
  / /_/ / / __ `/ __ \   / __ \/ ___/  / /   / __ \ | /| / /    
 / __  / / /_/ / / / /  / /_/ / /     / /___/ /_/ / |/ |/ /     
/_/ /_/_/\__, /_/ /_/   \____/_/     /_____/\____/|__/|__/      
        /____/                                                  
""")
        print(f"Your score is : {score}\n")
        print(f"Your number is : {initial_number}")
        guess = input(
            "Please guess that your number is higher(h) or lower?(l) than the secret number : ").lower()

        # Set the rule for winning and losing
        if guess == "h":
            if initial_number > secret_number:
                print(
                    f"\nYou guess correct!\nThe secret number is : {secret_number}")
                score += 1
                initial_number = secret_number
                secret_number = random.randint(1, 100)
                sleep(2)
            elif initial_number == secret_number:
                print("\nWhat a coincident! The numbers are equal.\nPlease guess again")
                secret_number = random.randint(1, 100)
                sleep(2)
            else:
                print(
                    f"\nYou guess wrong!\nThe secret number is : {secret_number}\n\nGAME OVER!!")
                right = False
                sleep(2)
        elif guess == "l":
            if initial_number < secret_number:
                print(
                    f"\nYou guess correct!\nThe secret number is : {secret_number}")
                score += 1
                initial_number = secret_number
                secret_number = random.randint(1, 100)
                sleep(2)
            elif initial_number == secret_number:
                print("\nWhat a coincident! The numbers are equal.\nPlease guess again")
                secret_number = random.randint(1, 100)
                sleep(2)
            else:
                print(
                    f"\nYou guess wrong!\nThe secret number is : {secret_number}\n\nGAME OVER!!")
                right = False
                sleep(2)

    # Ask to play again
    clear()
    print("""    __  ___       __                     __                     
   / / / (_)___ _/ /_     ____  _____   / /   ____ _      __    
  / /_/ / / __ `/ __ \   / __ \/ ___/  / /   / __ \ | /| / /    
 / __  / / /_/ / / / /  / /_/ / /     / /___/ /_/ / |/ |/ /     
/_/ /_/_/\__, /_/ /_/   \____/_/     /_____/\____/|__/|__/      
        /____/                                                  
""")
    print(f"Your final score is : {score}\n")
    answer = input("Do you want to play again? (y or n) : ").lower()
    if answer == 'y':
        clear()
        print("""    __  ___       __                     __                     
   / / / (_)___ _/ /_     ____  _____   / /   ____ _      __    
  / /_/ / / __ `/ __ \   / __ \/ ___/  / /   / __ \ | /| / /    
 / __  / / /_/ / / / /  / /_/ / /     / /___/ /_/ / |/ |/ /     
/_/ /_/_/\__, /_/ /_/   \____/_/     /_____/\____/|__/|__/      
        /____/                                                  
""")
        print("Okay!\nLet's play again.")
        sleep(2)
    elif answer == "n":
        clear()
        print("""    __  ___       __                     __                     
   / / / (_)___ _/ /_     ____  _____   / /   ____ _      __    
  / /_/ / / __ `/ __ \   / __ \/ ___/  / /   / __ \ | /| / /    
 / __  / / /_/ / / / /  / /_/ / /     / /___/ /_/ / |/ |/ /     
/_/ /_/_/\__, /_/ /_/   \____/_/     /_____/\____/|__/|__/      
        /____/                                                  
""")
        print("Thank You for playing!")
        playing = False
        sleep(2)
        clear()
