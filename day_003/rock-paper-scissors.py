import random

print("Welcome to the Rock-Paper-Scissors Game!\n")

choice = input("Choose what you want againts me(rock, paper or scissors)!\n").lower()
choice_c = ""

your_choice = ""
computer_choice = ""
result = ""
choice_random = random.randint(1, 3)

if choice_random == 1:
  choice_c = "scissors"
  computer_choice = """
    .-.  _
    | | / )
    | |/ /
  _|__ /_
  / __)-' )
  \  `(.-')
  > ._>-'
  / \/

  Computer choose: Scissors!
  """
elif choice_random == 2:
  choice_c = "paper"
  computer_choice = '''
  
          ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
___        '--...__"";
    `-..__ '"---..._;"
          """"----'       


  Computer choose: Paper!
  '''
else:
  choice_c = "rock"
  computer_choice = '''
  
      ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
      `-----"


  Computer choose: Rock!
  '''


if choice == "scissors":
  your_choice = """
    .-.  _
    | | / )
    | |/ /
  _|__ /_
  / __)-' )
  \  `(.-')
  > ._>-'
  / \/

  You choose: Scissors!
  """
elif choice == "paper":
  your_choice = '''
  
          ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
___        '--...__"";
    `-..__ '"---..._;"
          """"----'       


  You choose: Paper!
  '''
else:
  your_choice = '''
  
      ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
      `-----"


  You choose: Rock!
  '''


if choice == "paper" and choice_c == "paper":
  result = "It's a draw!\n\nPlease play again\n"
elif choice == "scissors" and choice_c == "scissors":
  result = "It's a draw!\n\nPlease play again\n"
elif choice == "rock" and choice_c == "rock":
  result = "It's a draw!\n\nPlease play again\n"
elif choice == "scissors" and choice_c == "rock":
  result = "You lose!\n\nSorry about that.\n"
elif choice == "rock" and choice_c == "paper":
  result = "You lose!\n\nSorry about that.\n"
elif choice == "paper" and choice_c == "scissors":
  result = "You lose!\n\nSorry about that.\n"
elif choice == "scissors" and choice_c == "paper":
  result = "You win!\n\nCongratulation!!.\n"
elif choice == "rock" and choice_c == "scissors":
  result = "You win!\n\nCongratulation!!.\n"
elif choice == "paper" and choice_c == "rock":
  result = "You win!\n\nCongratulation!!.\n"


if (choice != "rock") and (choice != "scissors") and (choice != "paper"):  
  print("\nHey, that illegal!\nPlease choose something between 'rock','paper' or 'scissors'!\n")
else:
  print("\nAnd the result is....\n\n")
  print(your_choice)
  print(computer_choice)
  print(result)

