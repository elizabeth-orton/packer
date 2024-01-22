# Feed Kitty
# Source: CMU CS Academy  https://academy.cs.cmu.edu/collection/1210/3/exercise 

# background
app.background = rgb(170, 185, 55)
Circle(200, 200, 150, fill='white')

# ears
Polygon(261, 158, 305, 132, 280, 195, fill=rgb(145, 170, 110),
        border=rgb(53, 31, 22), borderWidth=6)
Polygon(139, 158, 95, 132, 120, 195, fill=rgb(145, 170, 110),
        border=rgb(53, 31, 22), borderWidth=6),
Polygon(227, 129, 305, 133, 264, 160, border=rgb(55, 30, 20), borderWidth=6)
Polygon(173, 129, 95, 133, 136, 160, border=rgb(55, 30, 20), borderWidth=6)

# face and body
Oval(200, 276, 120, 130, border=rgb(55, 30, 20), borderWidth=6)
Circle(200, 200, 80, border=rgb(55, 30, 20), borderWidth=8)

# plate
Oval(200, 323, 140, 45, fill='beige', border=rgb(55, 30, 20), borderWidth=3)
Oval(200, 312, 200, 50, fill='white', border=rgb(55, 30, 20), borderWidth=4)
Oval(200, 317, 150, 30, fill=None, border=rgb(170, 185, 55), borderWidth=3)

# hands
Oval(165, 285, 30, 35, border=rgb(55, 30, 20), borderWidth=5, rotateAngle=-20)
Oval(235, 285, 30, 35, border=rgb(55, 30, 20), borderWidth=5, rotateAngle=20)

# eyes and tears
Oval(163, 193, 75, 100, fill='beige', border=rgb(55, 30, 20), borderWidth=4,
     rotateAngle=5)
Oval(237, 193, 75, 100, fill='beige', border=rgb(55, 30, 20), borderWidth=4,
     rotateAngle=-5)
leftEye = Oval(165, 185, 45, 55, border=rgb(55, 30, 20), borderWidth=4)
rightEye = Oval(235, 185, 45, 55, border=rgb(55, 30, 20), borderWidth=4)
leftTear = Oval(150, 240, 25, 15, fill='lightCyan', border=rgb(85, 130, 125))
rightTear = Oval(250, 240, 25, 15, fill='lightCyan', border=rgb(85, 130, 125))

# message
message = Label('pleeeease', 200, 90, fill=rgb(170, 185, 55), size=25, bold=True)

# food
foodPile = Oval(200, 320, 10, 5, fill='lightSalmon')
food = Circle(200, 30, 10, fill='lightSalmon', border='black', borderWidth=4)

def onMousePress(mouseX, mouseY):
    # The cat is not happy until the pile of food has a height of 30 pixels.
    # Until then, increase the width and height of the pile.
    ### (HINT: Make sure to set the bottom of the foodPile to 325!)
    ### Place Your Code Here ###
    foodPile.bottom=325
    if foodPile.height<30:
        foodPile.height = foodPile.height+2
        foodPile.width = foodPile.width+3
    # When the food has a height of at least 30 pixels, change the message
    # text and hide the tears.
    ### Place Your Code Here ###
    if foodPile.height==30 or foodPile.height>30:
        message.value='meow'
        leftTear.visible=False
        rightTear.visible=False

def onMouseMove(mouseX, mouseY):
    # Moves the food as the mouse moves.
    food.centerX = mouseX
    food.centerY = mouseY

    # Makes the eyes follow the food.
    leftEye.centerX = 155 + (mouseX / 20)
    leftEye.centerY = 180 + (mouseY / 20)
    rightEye.centerX = 225 + (mouseX / 20)
    rightEye.centerY = 180 + (mouseY / 20)