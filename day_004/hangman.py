import random

#Start the game
print("Welcome to the Hangman Game!\n")

#Generate random word and guess word
word_list = ["lion", "tiger", "rabbit", "monkey", "elephant"]
guess_chances = 6
match_letter = 0

random_word = random.choice(word_list)
guess_word = ""

#Generate list for holdin temporary letter
arr_random = []
arr_guess = []

#Initialize starting guess word and word holder
for letter in random_word:
  guess_word += "_"
  arr_guess += "_"
  arr_random += letter

#Create ASCII art for each state

state_one = '''

  |-------|
  |       |
          |
          |
          |
          |

'''

state_two = '''

  |-------|
  |       |
  O       |
          |
          |
          |

'''

state_three = '''

  |-------|
  |       |
  O       |
  |       |
          |
          |

'''

state_four = '''

  |-------|
  |       |
  O       |
 /|       |
          |
          |

'''

state_five = '''

  |-------|
  |       |
  O       |
 /|\      |
          |
          |

'''

state_six = '''

  |-------|
  |       |
  O       |
 /|\      |
 /        |
          |

'''

state_seven = '''

  |-------|
  |       |
  O       |
 /|\      |
 / \      |
          |

'''

#Define logic to continue playing the game.
while (random_word != guess_word ) and (guess_chances > 0):
  #Show ASCII art based on chance count
  if guess_chances == 6:
    print(state_one)
  elif guess_chances == 5:
    print(state_two)
  elif guess_chances == 4:
    print(state_three)
  elif guess_chances == 3:
    print(state_four)
  elif guess_chances == 2:
    print(state_five)
  elif guess_chances == 1:
    print(state_six)

  #Show guess word to the user
  if guess_chances > 1:
    print(f"\nGuess chances: {guess_chances}\n")
  else:
    print(f"\nGuess chance: {guess_chances}\n")
  print(f"Guess this word : {guess_word}")

  #Ask user to guess the letter in word
  guess_letter = input("\nPlease guess the letter.\nThis man life depending on you. : ")

  match_letter = 0
  for index in range(len(random_word)):
    if guess_letter == arr_random[index] and guess_letter != arr_guess[index]:
      arr_guess[index] = guess_letter
      match_letter += 1

  #Decrease chances when guess wrong
  if match_letter == 0:
    guess_chances -= 1

  #Create new guess word based on the correct guess letter
  guess_word = ""
  for letter in arr_guess:
    guess_word += letter

#Define game over scenarios
if random_word == guess_word:
  print("\nYou win!!\nYou just save the man life.\n")
else:
  print(state_seven)
  print("\nGame over!!\nThis man dies because of you.\n")