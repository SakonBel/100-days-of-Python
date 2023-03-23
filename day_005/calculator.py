from os import system
from time import sleep


def clear(): return system("clear")


print("Welcome to the calculator!")
sleep(2)

calc_again = True
result = ""


def value_input():
    if not result:
        clear()
        first = int(input("What's the first number? : "))
    else:
        first = result
    clear()
    print(f"Your first number is {first}")
    print("+\n-\n*\n/")
    oper = input("Pick an operator above : ")
    clear()
    second = int(input("What's the next number? : "))
    return first, oper, second


f_num, operator, n_num = value_input()


def calc_number(first, second, oper):
    while oper == "+" or oper == "-" or oper == "*" or oper == "/":
        if oper == "+":
            return first + second
        elif oper == "-":
            return first - second
        elif oper == "*":
            return first * second
        elif oper == "/":
            return first / second


result = calc_number(first=f_num, second=n_num, oper=operator)

while calc_again:
    clear()
    print(f"Your calculation result = {result}\n")
    type(result)
    answer = input(
        f"Do you want to continue calculate with {result} result? (Y or N) : ").lower()
    if answer == "y":
        f_num, operator, n_num = value_input()
        result = calc_number(first=f_num, second=n_num, oper=operator)
    elif answer == "n":
        calc_again = False
        clear()
        print(f"You final result is {result}!\n")
    else:
        clear()
        print("You type the wrong command!")
        sleep(2)
