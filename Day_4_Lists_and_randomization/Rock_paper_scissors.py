# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
import random

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:"))
computer_choice = random.randint(0,2)

choices_images = [rock, paper, scissors]
choices_names = ["rock", "paper", "scissors"]

print(f"You choose {choices_names[your_choice]}:\n{choices_images[your_choice]}")
print(f"Computer choose {choices_names[computer_choice]}:\n{choices_images[computer_choice]}")
if your_choice > computer_choice:
    if your_choice == 2 and computer_choice == 0:
        print("Computer wins!")
    else:
        print("You win!")
elif your_choice < computer_choice:
    if your_choice == 0 and computer_choice == 2:
        print("You win!")
    else:
        print("Computer wins!")
elif your_choice == computer_choice:
    print("It's a tie!")
exit()