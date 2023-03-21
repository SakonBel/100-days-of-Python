import random

row_1 = ["[-]", "[-]", "[-]"]
row_2 = ["[-]", "[-]", "[-]"]
row_3 = ["[-]", "[-]", "[-]"]

treasure_map = [row_1, row_2, row_3]

print(f"{row_1}\n{row_2}\n{row_3}\n")

position = input("Where do you want to put the treasure above?(x, y) : ")
arr_position = position.split(", ")

treasure_map[int(arr_position[0])][int(arr_position[1])] = "[x]"

print(f"{row_1}\n{row_2}\n{row_3}\n")
