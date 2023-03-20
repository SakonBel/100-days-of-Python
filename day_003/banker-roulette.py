import random

print("Welcome to Banker Roulette!\n\n")

names_string = input("Give me everybody's names, seperated by comma.\n")

names = names_string.split(", ")

# random_number = random.randint(0, len(names)-1)

# unlucky_person = names[random_number]

unlucky_person = random.choice(names)

print(f"\nAnd the one who will pay the bill is.........\n\n{unlucky_person}!!\n")