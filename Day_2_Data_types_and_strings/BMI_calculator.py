# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#NOTE: my version is slightly different from teacher's
height = float(height) #convert strings to float since they encompass all numbers
weight = float(weight)

BMI = int(weight/(height**2)) # BMI equation

print(str(BMI)) #return BMI

####Rounds DOWN to nearest 'int' value
# print(int(20.5/3.1234))
