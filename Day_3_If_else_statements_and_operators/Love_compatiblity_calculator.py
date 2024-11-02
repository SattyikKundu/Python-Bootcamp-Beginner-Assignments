# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
name3 = str(name1 + name2) #combine names into 1 string
name3 = name3.lower() #lowercase all letters
digit1 = int(0)
digit1 += name3.count("t")
digit1 += name3.count("r")
digit1 += name3.count("u")
digit1 += name3.count("e")

digit2 = int(0)
digit2 += name3.count("l")
digit2 += name3.count("o")
digit2 += name3.count("v")
digit2 += name3.count("e")

score = int(str(digit1)+str(digit2))

if (score < 10) or (score > 90):
    print(f"You score is {score}, you go together like coke and mentos.")
elif (40 < score) or (score < 50):
    print(f"You score is {score}, you are alright together.")
else:
    print(f"You score is {score}.")


