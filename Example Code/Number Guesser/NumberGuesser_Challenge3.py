#Needed to generate the random range as well as have the computer guess random numbers
import random

#Prompt the user for a number for the computer to guess and cast to an int
targetNum = int(input("Please input a number"))

#Generate a maximum value that the computer can guess
#Done by generating a random number from 0 to the targetNum and then adding the targetNum to it
#This ensures that the maxNum will be in between the targetNum and 2 times the targetNum
maxNum = random.randint(0, targetNum) + targetNum

#Let the user know what exactly the computer will be doing and what the randomly generated range was
print(f"The computer will try to guess {targetNum} within the range of (0, {maxNum})\n\n")

#Initialize a variable to serve as the holding place for each guess
#Initialize it to targetNum - 1 to ensure that the while loop will run
guess = targetNum - 1

#Initialize a variable to keep track of how many guesses the computer has made
attempts = 0

#Initialize a variable to 0 to keep track of the highest number the computer guesses
#Set to 0 to ensure that any number guessed will be higher
#Any number less than or equal to 0 will work
highest = 0

#Initialize a variable to the maxNum to keep track of the lowest number the computer guesses
#Set to maxNum to ensure that any number guessed will be lower
#Any number greater than or equal to maxNum will work
lowest = maxNum

#Initialize a variable to a blank list to hold all of the previously guessed numbers
guessed = []

#Create while loop that will run until the computer guesses the number
while guess != targetNum:
    #Have the computer guess a number
    guess = random.randint(0, maxNum)
    
    #Create while loop that will run until the computer picks a number not previously guessed before
    while guess in guessed:
        guess = random.randint(0, maxNum)
    
    #Increment attempts
    attempts += 1
    
    #Add the guess number to the list of guessed numbers
    guessed.append(guess)
    
    #Print the guess so the user can see what the computer did
    print(guess)
    
    #Check if the guessed the number is higher than the previously highest guessed number
    if guess > highest:
        #If the guess is higher, adjust the highest number to the guess
        highest = guess
        
    #Use else if because there is no need to check if the number is lower if it is the new highest number
    elif guess < lowest:
        #If the guess is lower, adjust the lowest number to the guess
        lowest = guess
    
#Inform the user that the computer has completed its task and say how many attempts it took
print(f"\nThe computer got the number in {attempts} attempts")
#Inform the user of the highest and lowest number the computer guessed
print(f"The highest number guessed was {highest}, and the lowest number guessed was {lowest}")