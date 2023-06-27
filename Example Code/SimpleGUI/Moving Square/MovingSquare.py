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
#Initialize a variable to store how far the square will move when a key is pressed
squareMoveBy = 5

#Function used to determine which key the user pressed
def InputHandler(key):
    #Must use global to tell the code to use the position array created at the beginning of the program
    #If global is not used the program will create a different array and perform operations on that array
    global squarePosition
    
    #Check if the user is pressing one of the arrow keys
    #Up
    if key == 38:
        #Use negative moveBy for y components because SimpleGUI has (0, 0) in the top left
        squarePosition[1] += -squareMoveBy
    #Down
    elif key == 40:
        #Use negative moveBy for y components because SimpleGUI has (0, 0) in the top left
        squarePosition[1] -= -squareMoveBy
    #Left
    elif key == 37:
        squarePosition[0] -= squareMoveBy
    #Right
    elif key == 39:
        squarePosition[0] += squareMoveBy

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
frame = simplegui.create_frame("Moving Square", frameSize, frameSize)
#Set the function the frame will call every time a key is pressed down
frame.set_keydown_handler(InputHandler)
#Set the function the frame will call every time it wants to draw an image
frame.set_draw_handler(draw)
#Start the frame
frame.start()
