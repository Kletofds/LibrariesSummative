#################################
# Kelton Figurski
# Word Guessing Game
# Main Code
#################################

import random,time
from Modules import Compare

check = False

# reads words in text file
words = open('words.txt', 'r')
lines = words.readlines()

#picks random word from the text file
random_line = random.choice(lines)
random_word = random_line.strip()

print("This is a word guessing game.")


# starts loop for the game
while True:
    #gets word from user
    print("\nGuess a word")
    guessed_word = input(">")
    guessed_word = guessed_word.lower()

    # checks if word is right
    check = Compare.CheckWord(guessed_word, random_word)

    # checks characteristics if word is wrong
    if not check:
        Compare.LetterNum(guessed_word, random_word)#checks number of letters
        Compare.InWord(guessed_word, random_word)#checks if letters are in the word
        Compare.LetterPlace(guessed_word, random_word)#checks if any letters in right place
        time.sleep(3)#waits 3 seconds
        Compare.PrintInfo()#prints all known info about the word
        
    # breaks loop if word is right
    else:
        break
