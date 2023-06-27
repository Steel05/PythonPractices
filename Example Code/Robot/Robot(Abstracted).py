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
    #Get user input
	command = input("Enter command: ")
    #Split up the direction and steps
    command = command.split(' ')
    
    #Stores the tuple for the direction
    direction = directions[command[0].upper()]
    #Stores the steps as an integer
    steps = int(command[1])
    
    #Calculates the final movement to be applied to the robot
    finalMove = [direction[0] * steps, direction[1] * steps]
    
    #Updates the x component of the robot's position
    robotPose[0] += finalMove[0]
    #Updates the y component of the robot's position
    robotPose[1] += finalMove[1]
    
    #Inform the user of the robot's current position
    #Use tuple for automatic parentheses so it is more familiar to user as a coordinate
	print("\n" + tuple(robotPose))