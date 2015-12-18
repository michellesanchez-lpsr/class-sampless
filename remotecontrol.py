import turtle
import random
from Tkinter import *

def regular_pentagon(myTurtle):
        side_count3 = 0
        while side_count3 < 5:
                myTurtle.forward(100)
                myTurtle.left(73)
                side_count3 = side_count3 + 1


coloor = ['red','blue',' brown','pink','orange','purple','yellow','purple']

# create the root Tkinter window and a Frame to go in it
root = Tk()
frame = Frame(root)

# create our turtle
shawn = turtle.Turtle()

# make some simple buttons
fwd = Button(frame, text='fwd', command=lambda: shawn.forward(50))
left = Button(frame, text='left', command=lambda: shawn.left(90))
back = Button(frame, text='back', command=lambda: shawn.backward(50))
right = Button(frame, text='right', command=lambda: shawn.right(90))
penup = Button(frame, text='penup', command=lambda: shawn.penup())
pendown = Button(frame, text='pendown', command=lambda: shawn.pendown())
color = Button(frame, text='random color', command=lambda: shawn.color(random.choice(coloor)))
polygon1 =  Button(frame, text='pentagon', command=lambda: regular_pentagon(shawn))

# put it all together
fwd.pack(side=LEFT)
left.pack(side=LEFT)
back.pack(side=LEFT)
right.pack(side=LEFT)
penup.pack(side=LEFT)
pendown.pack(side=LEFT)
color.pack(side=LEFT)
polygon1.pack(side=LEFT)
frame.pack()

turtle.exitonclick()
