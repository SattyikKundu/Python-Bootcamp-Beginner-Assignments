# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores: ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

curr_high = 0
temp_hold = 0
indx = 0
for score in student_scores:
    temp_hold = int(student_scores[indx])
    if curr_high < temp_hold:
        curr_high = temp_hold
    indx += 1  # indx = indx +1
highest_score = curr_high
print(f"The highest score in the class is: {highest_score}")




