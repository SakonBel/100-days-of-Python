print("Welcome to Love Calculator!\n")

name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

name1_lowercase = name1.lower()
name2_lowercase = name2.lower()

letter_1 = name1_lowercase.count("t")
letter_2 = name1_lowercase.count("r")
letter_3 = name1_lowercase.count("u")
letter_4 = name1_lowercase.count("e")
letter_5 = name1_lowercase.count("l")
letter_6 = name1_lowercase.count("o")
letter_7 = name1_lowercase.count("v")
letter_8 = name1_lowercase.count("e")

letter_9 = name2_lowercase.count("t")
letter_10 = name2_lowercase.count("r")
letter_11 = name2_lowercase.count("u")
letter_12 = name2_lowercase.count("e")
letter_13 = name2_lowercase.count("l")
letter_14 = name2_lowercase.count("o")
letter_15 = name2_lowercase.count("v")
letter_16 = name2_lowercase.count("e")

string_number = str(letter_1 + letter_2 + letter_3 + letter_4 + letter_9 + letter_10 + letter_11 + letter_12) + str(letter_5 + letter_6 + letter_7 + letter_8 + letter_13 + letter_14 + letter_15 + letter_16)
integer_number = int(string_number)

message = ""

if integer_number < 10 or integer_number > 90:
  message = f"Your score is {integer_number}, you go together like coke and mentos."
elif integer_number > 40 and integer_number < 50:
  message = f"Your score is {integer_number}, you are alright together."
else:
  message = f"Your score is {integer_number}"

print(message)