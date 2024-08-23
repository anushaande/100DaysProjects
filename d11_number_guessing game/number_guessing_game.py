import random

NUM = random.randint(1,100)
game_on = True
print("Welcome to the Number Guessing Game.")
print("I am thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if level == 'easy':
    attempts = 10
elif level == "hard":
    attempts = 5
else:
    print("level should only be 'easy' or 'hard'. Please check the spelling and try again.")
    game_on = False

while game_on:
    print(f"You have {attempts} attempts remaining to guess the number")
    n = int(input("Make a guess: "))
    if n < NUM :
        print("Too Low.")
        game_on = True
    elif n > NUM:
        print("Too High.")
        game_on = True
    elif n == NUM:
        print(f"You got it! The answer was {NUM}")
        game_on = False
    print("Guess_again.")
    attempts -= 1


