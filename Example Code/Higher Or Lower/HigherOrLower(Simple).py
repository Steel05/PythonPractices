#Needed for the computer to generate the random target number
import random

#Inform the users of the rules of the game
print(f"""Welcome to Higher or Lower\n
The rules are simple:
Type any number into the prompt and the computer will tell you
if the target number is higher or lower than the number you entered\n
""")

#Have the computer generate a random target number
targetNum = random.randint(0, 100000)

#Initialize a variable to 1 to keep track of the number of attempts it takes the user
#Start at 1 to account for initial guess
attempts = 1

#Prompt user for initial guess
guess = int(input("Please enter your guess: "))

#Use while loop which will run until the user guesses the correct number
while guess != targetNum:
    #Print the users guess to help them keep track of the numbers they have entered
    print(guess)
    
    #Check if the guessed number is lower or higher than the target number
    #Checking if the numbers are equivalent is handled by the while loop
    if guess < targetNum:
        #Inform the user that the number is higher than their guess
        print("Higher")
    else:
        #Inform the user that the number is lower than their guess
        print("Lower")
        
    #Blank line to help with readability        
    print()
    
    #Prompt the user for another guess
    guess = int(input("Please enter your guess: "))
    
    #Increment attempts
    attempts += 1
   
#Print targetNum to account for while loop not running
print(targetNum)

#Inform the user that they have completed the game and how many attempts it took
print(f"""Congratulations!
You guessed the number in {attempts} guesses!
Thanks for playing!""")