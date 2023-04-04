numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [number * number for number in numbers]
print(squared_numbers)

even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

with open("file_1.txt") as file_1:
    numbers_1 = file_1.readlines()
    num_1_list = [int(item.split("\n")[0]) for item in numbers_1]

with open("file_2.txt") as file_2:
    numbers_2 = file_2.readlines()
    num_2_list = [int(item.split("\n")[0]) for item in numbers_2]


compared_numbers = [
    num1 for num1 in num_1_list for num2 in num_2_list if num1 == num2]
print(compared_numbers)
