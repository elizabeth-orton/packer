#i made this in cmu sandbox
## background
app.background = gradient('navy', 'black')
Star(20, 30, 8, 8, fill='white',roundness=30)
Star(380, 50, 8, 8, fill='white',roundness=30)
Star(370, 360, 8,8, fill='white',roundness=30)
Star(130, 210, 8,8, fill='white',roundness=30)
##ferris wheel
circle = Circle(200, 200, 177, border='white', fill=None, borderWidth = 6)
upright1 = Line(200, 200, 200, 25, fill='white',lineWidth=4)
horizontal1 = Line(200, 200, 375, 200, fill='white',lineWidth=4)
upright2 = Line(200, 200, 200, 375, fill='white', lineWidth=4)
horizontal2 = Line(200, 200, 25, 200, fill='white',lineWidth=4)
diagonal1 = Line(200, 200, 325, 75,  fill='white',lineWidth=4)
diagonal2 = Line(200, 200, 325, 325, fill='white',lineWidth=4)
diagonal3 = Line(200, 200, 75, 325, fill='white',lineWidth=4)
diagonal4 = Line(200, 200, 75, 75, fill='white',lineWidth=4)
trolley1 = Rect(upright1.x2-17.5, upright1.y2+3, 35, 40, fill='purple')
trolley2 = Rect(diagonal1.x2-17.5, diagonal1.y2+3, 35, 40, fill='purple')
trolley3 = Rect(horizontal1.x2-17.5, horizontal1.y2+3, 35, 40, fill='purple')
trolley4 = Rect(diagonal2.x2-17.5, diagonal2.y2+3, 35, 40, fill='purple')
trolley5 = Rect(upright2.x2-17.5, upright2.y2+3, 35, 40, fill='purple')
trolley6 = Rect(diagonal3.x2-17.5, diagonal3.y2+3, 35, 40, fill='purple')
trolley7 = Rect(horizontal2.x2-17.5,horizontal2.y2+3,35,40,fill='purple')
trolley8 = Rect(diagonal4.x2-17.5,diagonal4.y2+3,35,40,fill='purple')
light1 = Circle(200,100,5,fill=gradient('white','green','black'),opacity=75)
light2=Circle(300,200,5,fill=gradient('white','red','black'),opacity=75)
light3=Circle(200,300,5,fill=gradient('white','blue','black'),opacity=75)
light4=Circle(100,200,5,fill=gradient('white','yellow','black'),opacity=75)
ferrisWheel= Group(circle, upright1, horizontal1, upright2, horizontal2, diagonal1, diagonal2, diagonal3, diagonal4,light1,light2,light3,light4)
Line(50, 400, 200, 200, lineWidth=20, fill='white')
Line(350, 400, 200, 200, lineWidth=20,fill='white')
Circle(200, 200, 50, fill='white')
##rotate the ferris wheel
def onMouseMove(x,y):
    ferrisWheel.rotateAngle = angleTo(200, 200, x, y)
    trolley1.left = upright1.x2-17.5
    trolley2.left = diagonal1.x2-17.5
    trolley3.left = horizontal1.x2-17.5
    trolley4.left = diagonal2.x2-17.5
    trolley5.left = upright2.x2-17.5
    trolley6.left = diagonal3.x2-17.5
    trolley7.left = horizontal2.x2-17.5
    trolley8.left = diagonal4.x2-17.5
    trolley1.top = upright1.y2+5
    trolley2.top = diagonal1.y2+5
    trolley3.top = horizontal1.y2+5
    trolley4.top = diagonal2.y2+5
    trolley5.top = upright2.y2+5
    trolley6.top = diagonal3.y2+5
    trolley7.top = horizontal2.y2+5
    trolley8.top = diagonal4.y2+5
