print("Welcome to the Days In Month Checker!\n")

def is_leap(year):
  """Check if the year is leap year or not and return boolean value."""
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(entered_year, entered_month):
  leap_year = is_leap(int(entered_year))
  if leap_year:
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_days[int(entered_month) - 1]
  else:
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_days[int(entered_month) - 1]


year = input("Enter a year(1990, 1991) : ")
month = input("Enter a month(1, 2) : ")
days = days_in_month(year, month)
print(f"The days of {month} month of year {year} is {days} days!")
