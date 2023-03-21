students_score = [78, 65, 89, 86, 55, 91, 64, 89]

highest_score = 0

for score in students_score:
  if highest_score < score:
    highest_score = score

print(f"The student highest score is {highest_score}")