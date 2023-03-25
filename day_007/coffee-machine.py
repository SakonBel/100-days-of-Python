# todo: import and set initial value
from os import system
from time import sleep


def clear(): return system("clear")


def return_coin(coin):
    print(f"Your have been return ${coin} of coins.")


def check_portion(this_coffee):
    valid = True
    deduct = {}
    for material in this_coffee["portion"]:
        if (material == "water") and (this_coffee["portion"][material] > water):
            valid = False
        elif (material == "coffee") and (this_coffee["portion"][material] > coffee):
            valid = False
        elif (material == "milk") and (this_coffee["portion"][material] > milk):
            valid = False
        else:
            if material == "water":
                deduct["water"] = this_coffee["portion"][material]
            elif material == "coffee":
                deduct["coffee"] = this_coffee["portion"][material]
            elif material == "milk":
                deduct["milk"] = this_coffee["portion"][material]
            valid = valid and True

    return valid, deduct


water = 500
coffee = 100
milk = 300

enough = False
deduct_value = ""
recipe_name = ""
recipe_number = ""
coffee_recipe = [
    {
        "name": "Espresso",
        "price": 1.50,
        "portion": {
            "water": 50,
            "coffee": 18
        }
    },
    {
        "name": "Latte",
        "price": 2.50,
        "portion": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        }
    },
    {
        "name": "Capuccino",
        "price": 3.00,
        "portion": {
            "water": 250,
            "coffee": 24,
            "milk": 100
        }
    },
]

coin_type = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25,
}

have_material = True
while have_material:
    # todo: Greeting the user of this machine.
    clear()
    print("Welcome to the Wonderful Coffee Machine!!")
    sleep(2)

    # todo: Let the user select what type of machine they want.
    order = True
    while order:
        print(
            f"\nMaterial left: coffee={coffee}g, water={water}ml, milk={milk}ml.")
        select_coffee = input(
            "What type of coffee that you want? \n-Espresso(e)\n-Latte(l)\n-Capuccino(c)\n: ").lower()

        # todo: Let the user insert the number of coin that they want.
        print("\nPlease insert the coin that you want.")
        penny = int(input("Penny : "))
        nickel = int(input("Nickel : "))
        dime = int(input("Dime : "))
        quarter = int(input("Quarter : "))

        coin_amount = round((coin_type["penny"] * penny) + (coin_type["nickel"] * nickel) + (coin_type["dime"] * dime) + (
            coin_type["quarter"] * quarter), 2)

        # todo: Check for coin amount compare to the coffee price
        condition = False
        if select_coffee == "c":
            select_coffee = "Capuccino"
        elif select_coffee == "l":
            select_coffee = "Latte"
        elif select_coffee == "e":
            select_coffee = "Espresso"

        for i_item, v_item in enumerate(coffee_recipe):
            if select_coffee in v_item.values() and coin_amount >= v_item["price"]:
                recipe_number = i_item
                recipe_name = select_coffee
                condition = True

        if not condition:
            print(f"\nYour coin amount is ${coin_amount}!")
            print("You have not put enough coin for this recipe.")
            return_coin(coin_amount)
        # todo: Preparing the order based on condition.
        if condition:
            return_coin(
                round(coin_amount - (coffee_recipe[recipe_number]["price"]), 2))
            print("\nPlease wait a moment for the machine to prepare your order...\n")
            sleep(2)
            enough, deduct_value = check_portion(coffee_recipe[recipe_number])
            if enough:
                print(f"Here your delicious {recipe_name}!")
                for item in deduct_value:
                    if item == "water":
                        water -= deduct_value[item]
                    elif item == "milk":
                        milk -= deduct_value[item]
                    elif item == "coffee":
                        coffee -= deduct_value[item]
                sleep(2)
            else:
                print(
                    f"Sorry! We don't have enough material for {recipe_name}!")
                return_coin(
                    round(coin_amount - (coin_amount - (coffee_recipe[recipe_number]["price"])), 2))
                sleep(2)
                order = False
                have_material = False
    # todo: serve another user again.
        if have_material:
            answer = input("Do you want to order again?(y or n) : ").lower()
            if answer == "n":
                order = False
                have_material = False
                print("See you again!")
                sleep(2)
                clear()
            elif answer == "y":
                clear()
                print("Let's do another drink.")
        else:
            print("\nPlease come back another time when we refill material.")
            sleep(2)
            clear()
