#Needed for drawing images
import simplegui

#Initialize a variable to store the size of the frame
frameSize = 512

#Initialize an array to hold the 2 values for the position of the square
#Use an array so that each component can be edited individually
#Position will be in the center of the square
squarePosition = [256, 256]
#Initialize a variable to store the desired length of a side length for the square
squareSideLength = 50
#Initialize a blank array with 4 elements to hold the points of the square
squarePoints = [None] * 4
#Initialize a variable to store how fast the square will move
squareMoveSpeed = 10
#Initialize an array to hold the 2 values for the velocity of the square
#Use an array so that each component can be edited individually
#Each component will represent the speed of the square in the given axis
squareVelocity = [0, 0]

#Function used to determine which key the user pressed
def DownInputHandler(key):
    #Must use global to tell the code to use the velocity array created at the beginning of the program
    #If global is not used the program will create a different array and perform operations on that array
    global squareVelocity
    
    #Check if the user is pressing one of the arrow keys and adjust the squares velocity accordingly
    #Up
    if key == 38:
        squareVelocity[1] += squareMoveSpeed
    #Down
    elif key == 40:
        squareVelocity[1] -= squareMoveSpeed
    #Left
    elif key == 37:
        squareVelocity[0] -= squareMoveSpeed
    #Right
    elif key == 39:
        squareVelocity[0] += squareMoveSpeed

#Function used to determine which key the user released
def UpInputHandler(key):
    #Must use global to tell the code to use the velocity array created at the beginning of the program
    #If global is not used the program will create a different array and perform operations on that array
    global squareVelocity
    
    #Check if the user released one of the arrow keys and adjust the square's velocity accordingly
    #Up
    if key == 38:
        squareVelocity[1] -= squareMoveSpeed
    #Down
    elif key == 40:
        squareVelocity[1] += squareMoveSpeed
    #Left
    elif key == 37:
        squareVelocity[0] += squareMoveSpeed
    #Right
    elif key == 39:
        squareVelocity[0] -= squareMoveSpeed

#Function used to draw to the frame 
def draw(canvas):
    #Must use global to tell the code to use the points array created at the beginning of the program
    #If global is not used the program will create a different array and perform operations on that array
    global squarePoints
    #Must use global to tell the code to use the position array created at the beginning of the program
    global squarePosition
    
    #Move the square based upon the velocity
    squarePosition[0] += squareVelocity[0]
    #Use subtraction because SimpleGUI has (0, 0) in the top left
    squarePosition[1] -= squareVelocity[1]
    
    #Calculate the points of the square
    squarePoints[0] = (squarePosition[0] - (squareSideLength / 2), squarePosition[1] - (squareSideLength / 2))
    squarePoints[1] = (squarePosition[0] + (squareSideLength / 2), squarePosition[1] - (squareSideLength / 2))
    squarePoints[2] = (squarePosition[0] + (squareSideLength / 2), squarePosition[1] + (squareSideLength / 2))
    squarePoints[3] = (squarePosition[0] - (squareSideLength / 2), squarePosition[1] + (squareSideLength / 2))
    
    #Draw the square
    canvas.draw_polygon(squarePoints, 2, "Yellow", "Blue")

#Create a frame to draw the square to
frame = simplegui.create_frame("Moving Square", frameSize, frameSize)
#Set the function the frame will call every time a key is pressed down
frame.set_keydown_handler(DownInputHandler)
#Set the function the frame will call every time a key is released
frame.set_keyup_handler(UpInputHandler)
#Set the function the frame will call every time it wants to draw an image
frame.set_draw_handler(draw)
#Start the frame
frame.start()
