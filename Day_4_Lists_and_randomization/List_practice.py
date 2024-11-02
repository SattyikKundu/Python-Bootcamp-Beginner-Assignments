# List documentation: https://docs.python.org/3/tutorial/datastructures.html

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
                     "Massachusetts", "Maryland", "South Carolina", "New Hampshire",
                     "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont",
                     "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi",
                     "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan",
                     "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota",
                     "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming",
                     "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
# print(states_of_america)

# my code below
import random
random_num = random.randint(0,49)
print(f"Random U.S. State: {states_of_america[random_num]}")


# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes",
#               "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
print(f"Negative -4 offset of fruits is: {fruits[-4]}")
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen1 = [fruits, vegetables]
print(dirty_dozen1)
dirty_dozen2 = fruits + vegetables
print(dirty_dozen2)