print("Welcome to the leap-year checker!\n")

year = int(input("Please enter the year that you want to check\n"))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(f"The year {year} is a leap year!")
    else:
      print(f"The year {year} is not a leap year!")
  else:
    print(f"The year {year} is a leap year!")
else:
  print(f"The year {year} is not a leap year!")