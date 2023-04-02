import pandas as pd

data = pd.read_csv("squirrel_data.csv")
# data_dict = data.to_dict()
# print(data_dict)
fur_list = data["Primary Fur Color"].to_list()
gray_fur = 0
cinnamon_fur = 0
black_fur = 0

for color in fur_list:
    if color == "Gray":
        gray_fur += 1
    elif color == "Black":
        black_fur += 1
    elif color == "Cinnamon":
        cinnamon_fur += 1

new_dict = {
    "Fur": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_fur, cinnamon_fur, black_fur]
}

new_data = pd.DataFrame(new_dict)
new_data.to_csv("squirrel_count.csv")
