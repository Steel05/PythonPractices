#Initialize a variable to store x and y position of the robot
#Use list so that each can component can be accessed and edited directly
robotPose = [0, 0]

#Initialize a variable to store the possible directions
#Use dictionary to hold both name of direction as well as a tuple for its appropriate direction
directions = {"RIGHT" : (1, 0), "LEFT" : (-1, 0), "DOWN" : (0, -1), "UP" : (0, 1)}

#Define the maximum number of moves the user is allowed
moves = 2

print(f"""Welcome to the robot simulator
The robot can move in 4 directions:
Up, down, left, and right
to command the robot type in this format:
[DIRECTION] [STEPS]
The command must seperate the direction and steps with a space""")

#For loop to perform all the moves
for i in range(moves):
    # Initialize blank variables to hold the inputted direction and steps
    direction = None
    steps = None
    
    #While loop to get valid command and won't pass until one is inputted
    while steps == None and direction == None:
        #Get user input
        command = input("Enter command: ")
        #Split up the direction and steps
        command = command.split(' ')
        
        #Try statement to handle invalid commands
        try:
            #Attempts to store the tuple for the direction
            #Moves to except if unable to
            direction = directions[command[0].upper()]
            #Attempts to store the steps as an integer
            #Moves to except if unable to
            steps = int(command[1])
		#Runs if invalid command is inputted
        except:
            #Informs user of invalid command
            print("[ERROR] Invalid Command")
    
    #Calculates the final movement to be applied to the robot
    finalMove = [direction[0] * steps, direction[1] * steps]
    
    #Updates the x component of the robot's position
    robotPose[0] += finalMove[0]
    #Updates the y component of the robot's position
    robotPose[1] += finalMove[1]
    
    #Inform the user of the robot's current position
    #Use tuple for automatic parentheses so it is more familiar to user as a coordinate
	print("\n" + tuple(robotPose))