print("Welcome to the price calculator!\n")

product_price = int(input("What is the price of your product?\n$"))
product_amount = int(input("What amount of this product that you want to buy?\n"))
discount_percentage = int(input("What is percentage of discount of total amount(don't input percentage symbol)?\n"))

after_discounted_price = product_price * (1 - (discount_percentage / 100))
final_price = int(after_discounted_price * product_amount)

print(f"The final price of your product is ${final_price}")