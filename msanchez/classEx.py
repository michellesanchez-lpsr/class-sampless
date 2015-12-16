# Sample pattern

import turtle
# myTurtle is a turtle object 
def makeTriangle(myTurtle,side):
        myTurtle.forward(side)
        myTurtle.left(120)
        myTurtle.forward(side)
	myTurtle.left(120)
        myTurtle.forward(side)
	myTurtle.left(120)	

# make your turtle
kipp = turtle.Turtle()
kipp.forward(150)
kipp.right(180)

# kipp makes triangles centered at a pointthat shifts
# and decreasesin size with each loop
length = 100
while length > 0:
        makeTriangle(kipp, length)
	kipp.forward(3)
	
	length = length + 1
turtle.exitonclick()
	
