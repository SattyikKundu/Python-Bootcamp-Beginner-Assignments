# Import the random module here
import random

# Split string method
# Angela, Ben, Jenny, Michael, Chloe
names_string = input("Give me everybody's names, separated by a comma: ")
names = names_string.split(", ")


# 🚨 Don't change the code above 👆
# Write your code below this line 👇
print(f"List is: {names} and number of participants is {len(names)}")
random_choice = random.randint(0,(len(names)-1))
print(f"{names[random_choice]} is going to get a free meal today!")
