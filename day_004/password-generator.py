import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to Password Generator!\n")

num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like in your password?\n"))

total_letters = num_letters + num_symbols + num_numbers

password = ""
random_select = 0

for number in range(total_letters):
  if num_letters != 0 and num_symbols != 0 and num_numbers != 0:
    random_select = random.randint(0, 2)
    if random_select == 0:
      password += random.choice(letters)
      num_letters -= 1
    elif random_select == 1:
      password += random.choice(symbols)
      num_symbols -= 1
    else:
      password += random.choice(numbers)
      num_numbers -= 1
  elif num_letters != 0 and num_symbols != 0:
    random_select = random.randint(0, 1)
    if random_select == 0:
      password += random.choice(letters)
      num_letters -= 1
    else:
      password += random.choice(symbols)
      num_symbols -= 1
  elif num_symbols != 0 and num_numbers != 0:
    random_select = random.randint(0, 1)
    if random_select == 0:
      password += random.choice(symbols)
      num_symbols -= 1
    else:
      password += random.choice(numbers)
      num_numbers -= 1
  elif num_letters != 0 and num_numbers != 0:
    random_select = random.randint(0, 1)
    if random_select == 0:
      password += random.choice(letters)
      num_letters -= 1
    else:
      password += random.choice(numbers)
      num_numbers -= 1
  elif num_letters != 0:
    password += random.choice(letters)
    num_letters -= 1
  elif num_symbols != 0:
    password += random.choice(symbols)
    num_symbols -= 1
  else:
    password += random.choice(numbers)
    num_numbers -= 1

print(f"\nYour generated password is [ {password} ]\n")