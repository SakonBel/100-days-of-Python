# with open("weather_data.csv") as file:
#     data = file.readlines()

# print(data)

# import csv

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


import statistics
import pandas as pd

data = pd.read_csv("weather_data.csv")
print(type(data["day"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)


# average_1 = statistics.mean(temp_list)
# average_2 = sum(temp_list)/len(temp_list)
# average_3 = data["temp"].mean()
# print(average_1, average_2, average_3)

# max_temp = data["temp"].max()
# print(max_temp)

# Get hold of the row instead of column
print(data[data["temp"] == data["temp"].max()])

# Get hold of the single cell in particular row
monday = data[data.day == "Monday"]
monday_f = (monday.temp * 9/5) + 32
print(monday_f)

new_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

# convert dict into dataframe
new_data = pd.DataFrame(new_dict)

# create csv file from dataframe
new_data.to_csv("new_file.csv")
