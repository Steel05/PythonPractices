#Needed for the computer to generate the random target number
import random

#Inform the users of the rules of the game
print(f"""Welcome to Higher or Lower\n
The rules are simple:
Type any number into the prompt and the computer will tell you
if the target number is higher or lower than the number you entered\n
""")

#Have the computer generate a random target number
targetNum = random.randint(0, 10) #100000
#Initialize a variable to 0 to keep track of the number of attempts it takes the user
attempts = 0
#Initialize a variable to false to that the while loop will run
result = False

#Function that will go through the user's guess and compare it against the code
#Will return a string that will be outputted to the user to provide info on the placements of the numbers in their guess

#Function that will handle the entire guessing process as well as the output of higher or lower
#Will return a boolean that will be used to continue the while loop
def Guess():
    #Tell the function that when targetNum is referenced it is the one generated earlier in the program
    global targetNum
    
    #Tell the function that when attempts is referenced it is the one declared earlier in the program
    global attempts
    
    #
    #If global keyword is not used the function will assume it is a local variable and throw an error
    #
    
    #Set the guess to a null value
    guess = None
    
    #Loop to ensure valid guess
    while guess == None:
        #Handles invalid guesses
        try:
            #Prompt the user for a guess
            guess = int(input("Please guess a number"))
        #Shows in event of invalid guess
        except:
            print("[ERROR] Invalid guess\nPlease try again")
            
    print()
        
    #Increment the number of attempts
    attempts += 1
    #Print the guess the user made so that they can reference it later in the game
    print(guess)
    
    #If the number is the targetNum have the function output true to stop the while loop
    #Guard clause for rest of the function
    if guess == targetNum:
        #Early return of True will stop function here and remove need for excess checks
        return True
    
    #If the number is NOT the targetNum check if the targetNum is higher than the guessed number
    if guess < targetNum:
        #If the targetNum is higher than the guessed number print that info
        #This is to allow the user to reference the information later in the game
        print("Higher\n")
    else:
        #If the targetNum is not higher than the guessed number print that info
        #This is to allow the user to reference the information later in the game
        print("Lower\n")
            
    #Regardless of if the guessed number is higher or lower than the targetNum have the function output false
    #This is allows the while loop to continue and the game to keep running
    return False
    
#Create while loop that will run until the computer guesses the number
while not result:
    result = Guess()

#Inform the user that they have completed the game and how many attempts it took
print(f"""Congratulations!
You guessed the number in {attempts} guesses!
Thanks for playing!""")