#Needed for the computer to guess random numbers
import random

#Prompt the user for a number for the computer to guess and cast to an int
targetNum = int(input("Please input a number"))

#Let the user know what exactly the computer will be doing
print(f"The computer will try to guess {targetNum} within the range of (0, 10000)\n\n")

#Initialize a variable to serve as the holding place for each guess
#Initialize it to targetNum - 1 to ensure that the while loop will run
#Any mathematical augmentation to the targetNum will result in the same effect
guess = targetNum - 1

#Initialize a variable to keep track of how many guesses the computer has made
attempts = 0

#Create while loop that will run until the computer guesses the number
while guess != targetNum:
    #Have the computer guess a number
    guess = random.randint(0, 10000)
    #Increment attempts
    attempts += 1
    #Print the guess so the user can see what the computer did
    print(guess)

#Inform the user that the computer has completed its task and say how many attempts it took
print("\nThe computer got the number in {attempts} attempts")