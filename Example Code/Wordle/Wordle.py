#Assign a new variable to a 5 letter word that you wish for the user to guess
keyWord = ""
#force the keyword to be all lowercase
keyWord = keyWord.lower()

#Check to see if the word is not 
if len(keyWord) != 5:
    #If the keyWord is not 5 letters long inform the user and halt program execution
    print("[ERROR DETECTED]")
    print("keyWord MUST BE 5 LETTERS LONG")
    #exit() function will throw an error upon activation, ignore it
    exit()

#Initialize a variable to 0 to keep track of how many guesses the user has done
attempts = 0

#Prompt the user for an initial guess, do not cast to int because the code is stored as a string as well
guess = input("Please guess the word")

#Function that will go through the user's guess and compare it against the code
#Will return a string that will be outputted to the user to provide info on the placements of the numbers in their guess
def parseGuess():
    #Tell the function that when keyWord is referenced it is the one generated earlier in the program
    global keyWord
    
    #Tell the function that when guess is referenced it is the one the user inputted
    global guess
    
    #
    #If global keyword is not used the function will assume it is a local variable and throw an error
    #
    
    #Initialize a variable to a blank string, this variable will be added onto to form the final string returned by the function
    infoString = ""
    
    #Will loop through the user's guess by accessing each character as though the string was an array
    for guessIndex in range(0, 5):
        #Check if the letter is in the right spot
        if guess[guessIndex] == keyWord[guessIndex]:
            infoString += "^"
        #If the number is in the right spot there is no need to check for misplacement
        else:
            #Initialize a variable to 0 to keep track of how many times a misplaced number is found
            #Will be used to determine misplaced number vs a number not being in the code
            successfulChecks = 0
            
            #Will loop through the keyWord to be used to compare each character to the guess
            #This for loop will only tell how many times each letter in the guess is found in the keyWord
            #It will not handle changing the infoString
            for keyWordIndex in range(0, 5):
                #Check if a letter is misplaced
                if guess[guessIndex] == keyWord[keyWordIndex]:
                    #If letter is found elsewhere in the code increment successfulChecks to tell that a misplacement has been found
                    successfulChecks += 1
            
            #After counting misplacements check if any were found
            if successfulChecks != 0:
                infoString += "O"
            #If no misplacements are found for a given letter in the guess, the letter is not in the keyWord
            else:
                infoString += "X"
    
    #After construncting the infoString have the function output it
    return infoString

        
#Begin while loop that will continue until the user gets the correct code, handles win detection on its own
while guess != keyWord:
    #Output the user's guess and the infoString from the function so that the user can refernce the info later on
    print(guess)
    print(parseGuess() + "\n")
    
    #Have the user attempt to guess again
    guess = input("Please input a guess")
    
    #Increment the number of attempts made by the user
    attempts += 1
    

#Print the code and let the user know that they have completed the game
print(keyWord)
#Add 1 to the attempts to account for the last guess
print("Congratulations! You have guessed the word in " + str(attempts + 1) + " guesses!")