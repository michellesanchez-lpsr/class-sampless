import turtle


def drawTriangle (myTurtle):
        side_count = 0
        while side_count < 3:
                myTurtle.forward(10)
                myTurtle.right(120)
                side_count = side_count + 1

def drawlineoftriangles (myturtle):
        trry = 0
        while trry < 8:
                if trry >= 4:
                        myTurtle.forward(10)
                        myTurtle.right(120)
                        myTurtle.forward(10)
                        myTurtle.right(120)
                        myTurtle.forward(10)
                        myTurtle.right(120)
                        myTurtle.penup()
                        myTurtle.forward(30)
                        myTurtle.pendown()
                        trry = trry + 1

shawn = turtle.Turtle
drawlineoftriangles(shawn)
turtle.exitonclick()


