student_height = [180, 124, 165, 173, 189, 169, 146]
total_height = 0
total_students = 0

for height in student_height:
  total_height += height
  total_students += 1

average_height = round(total_height / total_students)

print(f"Average height of all student is {average_height} cm.")