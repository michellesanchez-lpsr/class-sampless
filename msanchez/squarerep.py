import turtle

def drawSquareR (myTurtle):
	myTurtle.color('red')
	count = 0
	while count < 4:
		myTurtle.forward(20)
		myTurtle.right(90)
		count = count + 1

def drawSquareB (myTurtle):
	myTurtle.color('blue')
	myTurtle.penup()
	myTurtle.forward(20)
	myTurtle.pendown()
	count = 0
        while count < 4:
                myTurtle.forward(20)
                myTurtle.right(90)
                count = count + 1
def drawSquareY (myTurtle):
	myTurtle.color('yellow')
	myTurtle.penup()
	myTurtle.forward(20)
	myTurtle.right(90)
	myTurtle.forward(20)
	myTurtle.pendown()
	count = 0
        while count < 4:
                myTurtle.forward(20)
                myTurtle.right(90)
                count = count + 1
def drawSquareG (myTurtle):
	myTurtle.color('green')
	myTurtle.penup()
        myTurtle.forward(20)
        myTurtle.right(90)
        myTurtle.forward(20)
        myTurtle.pendown()
	count = 0
        while count < 4:
                myTurtle.forward(20)
                myTurtle.right(90)
                count = count + 1
def drawColorss (myTurtle):
	drawSquareR(myTurtle)
	drawSquareB(myTurtle)
	drawSquareY(myTurtle)
	drawSquareG(myTurtle)

def drawReapeat (myTurtle):
	count = 0
	while count < 5:
		drawColorss(shawn)
		myTurtle.left(90)
		myTurtle.penup()
		myTurtle.forward(5)
		myTurtle.left(90)
		myTurtle.pendown()
		count = count + 1

shawn = turtle.Turtle()

shawn.speed(3)
drawReapeat(shawn)

turtle.exitonclick()
