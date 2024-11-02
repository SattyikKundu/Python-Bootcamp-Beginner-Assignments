# Write your code below this row 👇

# Note: My way I tried first
# total = 0
# for num in range(0,100,2):
#    total += int(num)
# print(f"Sum of even numbers from 1-100 is: {total}")

# Another way shown by teacher
total = 0
for num in range(1, 100):
    if num % 2 == 0:
        total += num
print(f"Sum of even numbers from 1-100 is: {total}")