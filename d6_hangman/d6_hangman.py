from hangman_art import stages,logo
from hangman_words import word_list,fruit_list
import random

word = random.choice(fruit_list)
final_word = ""
lives = 6
chances = 6
game_on = True
hangman= ""

for l in word:
    final_word+='_'
print(logo)

while game_on:
    print(f"Word to Guess : {final_word}")
    letter = input("Guess a letter: ")
    f_word = list(final_word)
    if letter in final_word:
        print('You already guessed the letter. Pick a different letter')
    elif letter in word:
        for i in range(len(word)):
            if letter == word[i]:
               f_word[i] = letter
    else:
        print(f"You guessed {letter}, that is not in the word. You lose a life")
        lives-=1            
    hangman = stages[lives]
    final_word = "".join(f_word)
    if lives > 0 and '_' in final_word:
        print(hangman)
        print(f"******************************************* {lives}/6 Lives Left ****************************************************")
        game_on = True
    elif lives <= 0 and '_' in final_word:
        game_on = False
        print(hangman)
        print(f"******************************************* {lives}/6 Lives Left ****************************************************")
        print("You could not guess the word. Your man is dead. Please try again later.")
    elif lives > 0 and '_' not in final_word:
        game_on = False
        print(f"You guessed the word. Your word {final_word} matched with {word}. YOU WON!")

        
    
        
    






