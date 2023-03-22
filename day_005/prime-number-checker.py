#Greet the user
print("Welcome to the Prime Number Checker!")

#Ask for user to input the desired number
check_num = int(input("Please input the number that you want to check. : "))

#Define function to check for the number
def prime_checker(number):
  if number % number == 0 and number % 1 == 0 and number != 1:
    if number == 2:
      print(f"The {number} number is the prime number")
    elif number == 3:
      print(f"The {number} number is the prime number")
    elif number == 5:
      print(f"The {number} number is the prime number")
    else:
      if number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
        print(f"The {number} number is not the prime number!")
      else:
        print(f"The {number} number is the prime number")
  else:
    print(f"The {number} number is not the prime number")

#Check for the number and return the result
prime_checker(check_num)