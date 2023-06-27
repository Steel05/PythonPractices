#Needed for drawing images
import simplegui
#Needed for generating a random position
import random

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

#Function used to randomly move the sqare
def RandomizeSquare():
    #Must use global to tell the code to use the position array created at the beginning of the program
    #If global is not used the program will create a different array and perform operations on that array
    global squarePosition
    #Must use global to tell the code to use the side length variable created at the beginning of the program
    #If global is not used the program will create a different variable and perform operations on that variable
    global squareSideLength
    
    #Set the side length of the square to a randomly generated value
    #Adjust side length before position because the side length is used to ensure the square is never off screen
    squareSideLength = random.randint(15, 100)
    
    #Set the x coordinate of the position to a randomly generated value
    #Use calculated values to ensure that the square stays within the frame
    squarePosition[0] = random.randint(int(squareSideLength / 2), frameSize - int(squareSideLength / 2))
    #Set the y coordinate of the position to a randomly generated value
    #Use calculated values to ensure that the square stays within the frame
    squarePosition[1] = random.randint(int(squareSideLength / 2), frameSize - int(squareSideLength / 2))

#Function used to move the square to where the user clicks
def MoveToClick(position):
    #Must use global to tell the code to use the position array created at the beginning of the program
    #If global is not used the program will create a different array and perform operations on that array
    global squarePosition
    
    #Set the x coordinate of the square's position to the x coordinate of the click position
    squarePosition[0] = position[0]
    #Set the y coordinate of the square's position to the y coordinate of the click position
    squarePosition[1] = position[1]
    
#Function used to draw to the frame
def draw(canvas):
    #Must use global to tell the code to use the points array created at the beginning of the program
    #If global is not used the program will create a different array and perform operations on that array
    global squarePoints
    
    #Calculate the points of the square
    squarePoints[0] = (squarePosition[0] - (squareSideLength / 2), squarePosition[1] - (squareSideLength / 2))
    squarePoints[1] = (squarePosition[0] + (squareSideLength / 2), squarePosition[1] - (squareSideLength / 2))
    squarePoints[2] = (squarePosition[0] + (squareSideLength / 2), squarePosition[1] + (squareSideLength / 2))
    squarePoints[3] = (squarePosition[0] - (squareSideLength / 2), squarePosition[1] + (squareSideLength / 2))
    
    #Draw the square
    canvas.draw_polygon(squarePoints, 2, "Yellow", "Blue")

#Create a frame to draw the square to
frame = simplegui.create_frame("Random Square", frameSize, frameSize)
#Create a button for moving the square
frame.add_button("Randomize Square", RandomizeSquare)
#Set the function the frame will call every time the user clicks within the frame
frame.set_mouseclick_handler(MoveToClick)
#Set the function the frame will call every time it wants to draw an image
frame.set_draw_handler(draw)
#Start the frame
frame.start()