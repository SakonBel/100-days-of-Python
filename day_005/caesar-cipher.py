#Greet the user
print("Welcome to the caesar cipher!")

#Create initial letters
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

message = input("Enter your secret message.\n").lower()

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

print(num_m_list, new_num_list, m_list, new_m_list)

#Create cipher function
def cipher(i_list):
  new_message = ""
  for char in i_list:
    new_message += char
  print(f"Your message has been turn to : {new_message}")

def decipher(i_list):
  revert_message = ""
  for char in i_list:
    revert_message += char
  print(f"Your message has been turn to : {revert_message}")

cipher(new_m_list)
decipher
#Promp the user if they want to see the new message?
see_new = ""
see_old = ""

def prompt_user(prompt):
  prompt = input("Do you want to see the message that been ciphered?\ny : to see\nn : to not see\n q : to exit\n ").lower()

if see_new == "y":
  prompt_user(see_old)
elif see_old == "y":
  prompt_user(see_new)


