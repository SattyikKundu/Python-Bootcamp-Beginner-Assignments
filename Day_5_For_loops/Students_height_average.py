# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
height_sum = 0
n = 0
for one_height in student_heights:
    height_sum += int(student_heights[n])    # height_sum = height_sum + int(student_heights[n])
    n += 1                                   # n = n + 1

# print("total heights: " + str(height_sum))
# print("total students: " + str(n))
average = height_sum / n

print(f"Average is {round(average)}")


