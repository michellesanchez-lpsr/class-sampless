import turtle
# this draws one rhombus
def drawDiamond(myTurtle):
        count = 0
        myTurtle.left(30)
        while count <2:
                myTurtle.begin_fill()
                myTurtle.forward(40)
                myTurtle.left(120)
                myTurtle.forward(40)
                myTurtle.left(60)
                myTurtle.end_fill()
                count = count + 1
# now we make the side of the cube
# the sides of the cube are exactly the same as the first rhombus that we drew


def drawSide1(myTurtle):
	myTurtle.right(150)
	myTurtle.color("light blue")
	myTurtle.fillcolor("light blue")
	myTurtle.begin_fill()
	drawDiamond(myTurtle)
	myTurtle.end_fill()
# this wil finish with a cube
# this will make the 3rd rhombus to complete the cube
def drawSide2(myTurtle):
	myTurtle.right(150)
	myTurtle.color("pink")
	myTurtle.fillcolor("pink")
	myTurtle.begin_fill()
	drawDiamond(myTurtle)
	myTurtle.end_fill()
# this funtion alligns the turtle and makes a new cube
# This will be row # 1 of our problem
def allignTurtle(myTurtle):
	count = 0	
	while count < 4:
		myTurtle.forward(40)
		myTurtle.left(60)
		myTurtle.forward(40)
		myTurtle.right(120)
		myTurtle.right(90)	
		drawRhombus(myTurtle)
		drawSide1(myTurtle)
		drawSide2(myTurtle)
		count = count + 1
# go to the top to make a second row
def drawRhombus(myTurtle):
	myTurtle.color("black")
        myTurtle.fillcolor("black")
        myTurtle.begin_fill()
        drawDiamond(myTurtle)
        myTurtle.end_fill()


def goRow2(myTurtle):
	myTurtle.penup()
	myTurtle.left(30)
	myTurtle.backward(243)
	myTurtle.right(90)
	myTurtle.forward(60)
	myTurtle.pendown()
	myTurtle.right(90)
def row2(myTurtle):
	count = 0
	while count < 4:
		drawRhombus(myTurtle)
		drawSide1(myTurtle)
		drawSide2(myTurtle)
		myTurtle.forward(40)
                myTurtle.left(60)
		myTurtle.forward(40)                
                myTurtle.right(120)
                myTurtle.right(90)
		count = count + 1
	drawRhombus(myTurtle)
	drawSide1(myTurtle)
	drawSide2(myTurtle)

def goRow3(myTurtle):
        myTurtle.penup()
        myTurtle.left(30)
        myTurtle.backward(243)
        myTurtle.right(90)
        myTurtle.forward(60)
        myTurtle.pendown()
        myTurtle.right(90)

def row3(myTurtle):
        count = 0
        while count < 5:
                drawRhombus(myTurtle)
                drawSide1(myTurtle)
                drawSide2(myTurtle)
                myTurtle.forward(40)
                myTurtle.left(60)
                myTurtle.forward(40)
                myTurtle.right(120)
                myTurtle.right(90)
                count = count + 1		           

shawn = turtle.Turtle()
shawn.speed(0)
drawDiamond(shawn)
drawSide1(shawn)
drawSide2(shawn)
allignTurtle(shawn)
goRow2(shawn)
row2(shawn)
goRow3(shawn)
row3(shawn)
drawRhombus(shawn)
turtle.exitonclick()


