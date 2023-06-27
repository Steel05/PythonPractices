#Needed to generate the random range as well as have the computer guess random numbers
import random

#Prompt the user for a number for the computer to guess and cast to an int
#Alternatively could cast to string on every guess and leave targetNum as a string
#However casting on every guess is less efficient
targetNum = int(input("Please input a number"))

#Generate a maximum value that the computer can guess
#Done by generating a random number from 0 to the targetNum and then adding the targetNum to it
#This ensures that the maxNum will be in between the targetNum and 2 times the targetNum
maxNum = random.randint(0, targetNum) + targetNum

#Let the user know what exactly the computer will be doing and what the randomly generated range was
print(f"The computer will try to guess {targetNum} within the range of (0, {maxNum})\n\n")

#Initialize a variable to serve as the holding place for each guess
#Initialize it to targetNum - 1 to ensure that no matter what the while loop will run
#Any mathematical augmentation to the targetNum will result in the same effect
guess = targetNum - 1

#Initialize a variable to keep track of how many guesses the computer has made
attempts = 0

#Create while loop that will run until the computer guesses the number
while guess != targetNum:
    #Have the computer guess a number
    guess = random.randint(0, maxNum)
    #Increment attempts
    attempts += 1
    #Print the guess so the user can see what the computer did
    print(guess)

#Inform the user that the computer has completed its task and say how many attempts it took
print(f"\nThe computer got the number in {attempts} attempts")