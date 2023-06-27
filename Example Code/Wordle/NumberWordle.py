#Needed to randomly generate code
import random

#Assign a new variable a blank string, use string so that each individual character can be accessed later
#Also helps handle 0's
code = "" 

#Initialize a variable to 0 to keep track of how many guesses the user has done
attempts = 0

#Generate 3 random numbers, convert them to strings and concatenate them to the code variable
for i in range(0, 3):
    #Use 0 through 9 instead of generating between 0 and 999 to eliminate 1 or 2 digit codes
    #Alternatively could generate between 100 and 999 to eliminate the need for the while loop, must remember to cast to string
    code += str(random.randint(0, 9))

#Prompt the user for an initial guess, do not cast to int because the code is stored as a string as well
guess = input("Please guess the code")

#Function that will go through the user's guess and compare it against the code
#Will return a string that will be outputted to the user to provide info on the placements of the numbers in their guess
def parseGuess():
    #Tell the function that when code is referenced it is the one generated earlier in the program
    global code
    
    #Tell the function that when guess is referenced it is the one the user inputted
    global guess
    
    #
    #If global keyword is not used the function will assume it is a local variable and throw an error
    #
    
    #Initialize a variable to a blank string, this variable will be added onto to form the final string returned by the function
    infoString = ""
    
    #Will loop through the user's guess by accessing each character as though the string was an array
    for guessIndex in range(0, 3):
        #Check if the number is in the right spot
        if guess[guessIndex] == code[guessIndex]:
            infoString += "^"
        #If the number is in the right spot there is no need to check for misplacement
        else:
            #Initialize a variable to 0 to keep track of how many times a misplaced number is found
            #Will be used to determine misplaced vs a number not being in the code
            successfulChecks = 0
            
            #Will loop through the code to be used to compare each character to the guess
            #This while loop will only tell how many times each number in the guess is found in the code
            #It will not handle changing the infoString
            for codeIndex in range(0, 3):
                #Check if a number is misplaced
                if guess[guessIndex] == code[codeIndex]:
                    #If number is found elsewhere in the code increment successfulChecks to tell that a misplacement has been found
                    successfulChecks += 1
            
            #After counting misplacements check if any were found
            if successfulChecks != 0:
                infoString += "O"
            #If no misplacements are found for a given number in the guess the number is not in the code
            else:
                infoString += "X"
    
    #After construncting the infoString have the function output it
    return infoString

        
#Begin while loop that will continue until the user gets the correct code, handles win detection on its own
while guess != code:
    #Output the user's guess and the infoString from the function so that the user can refernce the info later on
    print(guess)
    print(parseGuess() + "\n")
    
    #Have the user attempt to guess again
    guess = input("Please input a guess")
    
    #Increment the number of attempts made by the user
    attempts += 1
    

#Print the code and let the user know that they have completed the game
print(code)
#Add 1 to the attempts to account for the last guess
print("Congratulations! You have guessed the code in " + str(attempts + 1) + " guesses!")
    