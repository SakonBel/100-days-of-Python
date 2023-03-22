#Greet the user
print("Welcome to the caesar cipher!")

#Create initial letters
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

message = input("\nEnter your secret message.\n").lower()

#Store each message character in list
m_list = []

#Create list to store each character position
num_m_list = []

#Create list to store new character for the message
new_m_list = []

#Create list to store new character position
new_num_list = []

shift_count = int(input("Please enter your shift count for the message.\n"))
#Adding each character to list
for char in message:
  m_list += char
  #Define way to know each character position
  num_index = 0

  for letter in letters:
    if char == letter:
      #Adding each position to the list
      num_m_list.append(num_index)
      if num_index + shift_count < 26:
        new_num_list.append(num_index + shift_count)
      else:
        new_num_list.append(num_index + shift_count - 26)
    num_index += 1

for pos in new_num_list:
  new_m_list += letters[pos]

# print(num_m_list, new_num_list, m_list, new_m_list)

#Create cipher function
def cipher(i_list):
  new_message = ""
  for char in i_list:
    new_message += char
  print(f"\nYour message has been turn to : {new_message}\n")

def decipher(i_list):
  revert_message = ""
  for char in i_list:
    revert_message += char
  print(f"\nYour message has been turn to : {revert_message}\n")

#Promp the user if they want to see the new message?
see = ["a"]

def prompt_user(word):
  prompt = input(f"Do you want to see the message that been {word}?\ny : to see\nn : to not see\nq : to exit\n").lower()
  if prompt == "q":
    see[0] = "q"
  elif (prompt == "y" and word == "cipher") or (prompt == "n" and word == "decipher"):
    see[0] = "n"
    print(see[0])
  elif (prompt == "y" and word == "decipher") or (prompt == "n" and word == "cipher"):
    see[0] = "o"
    print(see[0])

def prompt_init():
  input_a = input("Do you want to see old message or new message?\na : new\nb : old\n").lower()
  if input_a == "a":
    see[0] = "n"
  else:
    see[0] = "o"

prompt_init()
while see[0] == "n" or see[0] == "o":
  if see[0] == "n":
    cipher(new_m_list)  
    prompt_user("decipher")
  elif see[0] == "o":
    decipher(m_list)
    prompt_user("cipher")

if see[0] == "q":
  print("\nYou have been quit the program!\n")

