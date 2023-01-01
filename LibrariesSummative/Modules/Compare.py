########################################
# Kelton Figurski
# Module that compares the words
# Libraries Summative
########################################

# checks if the word is right
def CheckWord(guessed_word, random_word):
    
    # tells user if they got the word
    if guessed_word == random_word:
        print("\nCongratulations! You got the word!")
        
        # returns value to break the loop
        correct = True
        return correct
        
    # tells user if the word is wrong
    else:
        print("\nThat word is incorrect")
            

# checks if the number of letters is right
def LetterNum(guessed_word, random_word):
    
    # finds length of the two words
    GuessedNum = len(guessed_word)  
    RandomNum = len(random_word)

    # tells user if they got the right number of letters
    if GuessedNum == RandomNum:
        print("You got the right number of letters.\n")
        
        # saves number of letters if correct
        global NumberLetters
        NumberLetters = RandomNum
        
    #tells user if the number of letters is wrong
    else:
        print("You did not get the right number of letters.\n")
        
        
# checks if any of the letters are in the word
def InWord(guessed_word, random_word):
    
    # create list if not already created
    global LettersInWord
    try:
        LettersInWord
    except:
        LettersInWord = []
    
    #turns words into lists
    GuessedLetters = list(guessed_word)
    RandomLetters = list(random_word)
    
    # finds if letters in word if guessed word has more letters
    if len(GuessedLetters) > len(RandomLetters):
        for i in RandomLetters:
            if i in GuessedLetters:
                print(i, "is in the word.")
                
                # saves correct letters to list if not already in it
                if i not in LettersInWord:
                    LettersInWord.append(i)
            
    # finds if letters in word if random word has more letters
    else:
        for q in GuessedLetters:
            if q in RandomLetters:
                print(q, "is in the word.")
                
                # saves correct letters to list if not already in it
                if q not in LettersInWord:
                    LettersInWord.append(q)
                
# checks if any of the letters are in the right place
def LetterPlace(guessed_word, random_word):
    
    # creates list for letters in correct place if not already created
    global CorrectPlace
    try:
        CorrectPlace
    except:
        CorrectPlace = []
    
    # turns words into lists
    GuessedLetters = list(guessed_word)
    RandomLetters = list(random_word)
    
    # checks if words are in correct place if guessed word has more letters
    if len(GuessedLetters) > len(RandomLetters):
        
        for p in range(len(RandomLetters)):
            y = p + 1
            if RandomLetters[p] == GuessedLetters[p]:
                print(GuessedLetters[p], "is in the right place.")
                
                # adds word and place to list if not already in it
                CorrectPlaceCheck = (f"'{GuessedLetters[p]}' is in place {y}")
                if CorrectPlaceCheck not in CorrectPlace:
                    CorrectPlace.append(CorrectPlaceCheck)
    
    # checks if words are in correct place if random word has more letters
    else:
        for z in range(len(GuessedLetters)):
            x = z + 1
            if RandomLetters[z] == GuessedLetters[z]:
                print(GuessedLetters[z], "is in the right place.")
                
                # adds word and place to list if not already in it
                CorrectPlaceCheck1 = (f"'{GuessedLetters[z]}' is in place {x}")
                if CorrectPlaceCheck1 not in CorrectPlace:
                    CorrectPlace.append(CorrectPlaceCheck1)
                
    
# prints all known info about the word            
def PrintInfo():
    print(f"\nCorrect positions of letters: {CorrectPlace}")
    print(f"Letters in the word: {LettersInWord}")
    try:
        print(f"There are {NumberLetters} letters in the word.")
    except:
        print("You don't know the number of letters.")