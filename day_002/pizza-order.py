print("Welcome to the pizza deliveries!\n")

size = input("What size of pizza that you want? S, M, or L\n")
add_pepperoni = input("Do you want Pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")

price = 0
pepperoni = ""
cheese = ""

if size == "S":
  price = 15
elif size == "M":
  price = 20
else:
  price = 25

if add_pepperoni == "Y":
  pepperoni = "with pepperoni"
  if size == "S":
    price += 2
  else:
    price += 3
else:
  pepperoni = "without pepperoni"

if extra_cheese == "Y":
  cheese = "and want extra cheese"
  price += 1
else:
  cheese = "and want regular cheese"

print(f"You have order pizza size {size} {pepperoni} {cheese}\nYour final bill is: ${price}")