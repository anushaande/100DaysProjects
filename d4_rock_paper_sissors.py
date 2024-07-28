## https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences - resourse for random module 

import random

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

#Write your code below this line 👇

user_choice =int(input(f'What do you choose? Type 0 for rock, 1 for paper or 2 for Scissors.\n')) 

if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)

computer_choice = random.choice([0,1,2])
if computer_choice == 0:
    computer_img = rock
elif computer_choice == 1:
    computer_img = paper
elif computer_choice == 2:
    computer_img = scissors
print(f"Computer chose:\n{computer_img}")

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")