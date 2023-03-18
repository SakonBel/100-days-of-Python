print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? : $")
num_of_people = input("How many people to split the bill? : ")
tip_percentage = input("What percentage of tip would you like to give? : ")
print("Each person should pay: $" + str(round((float(total_bill) * ((int(tip_percentage) + 100)/100)) / int(num_of_people), 2)))
่