import math

#Greet the user
print("Welcome to the Paint Area Calculator!")

#Define initial calculation
coverage = 5

def paint_calc(height, width, cove):
  num_of_can = math.ceil((height * width)/cove)
  print(f"\nYou must use [{num_of_can}] cans in order to paint this area.\n")

#Ask for area size
i_height = int(input("Height of wall : "))
i_width = int(input("Width of wall : "))

#Calculate the result
paint_calc(i_height, i_width, coverage)