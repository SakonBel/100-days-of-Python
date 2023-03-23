from os import system
from time import sleep

clear = lambda: system("clear")

clear()
print("Welcome to the Silent Bidding Auction!\n")

bidding = True
bidder_list = {}

def bidder():
  bidder_name = input("What is your name? : ")
  bidder_price = int(input("What price do you want to bid? : $"))

  bidder_list[bidder_name] = bidder_price

def show_result():
  top_bidder = ""
  for key in bidder_list:
    top_bidder = key

  for bidder in bidder_list:
    if bidder_list[bidder] > bidder_list[top_bidder]:
      top_bidder = bidder
  
  for bidder in bidder_list:
    if bidder_list[top_bidder] == bidder_list[bidder]:
      print(f"The winner of this bid is '{bidder}'\nwith the bidding price at [${bidder_list[bidder]}]\n")

  print("Here the result of other bidders:\n")
  for bidder in bidder_list:
    if not bidder_list[top_bidder] == bidder_list[bidder]:
      print(f"The bidder '{bidder}' has bid for the price at [${bidder_list[bidder]}]")

  print("\nThis conclude the result of this bidding!\n")


bidder()

while bidding:
  clear()
  answer = input("Do you want to continue bidding? (Y or N) : ").lower()
  if answer == "n":
    clear()
    bidding = False
  elif answer == "y":
    clear()
    print("Please input another bidder.\n")
    bidder()
  else:
    clear()
    print("You type the wrong choice!")
    sleep(2)


show_result()
