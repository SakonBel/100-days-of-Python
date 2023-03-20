import random

side = random.randint(1,2)
coin = ""

if side == 1:
  coin = "Heads"
else:
  coin = "Tails"

print(f"Your coin toss result is........\n\n{coin}!\n")
