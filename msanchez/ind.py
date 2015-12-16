import random
import turtle

coloor = turtle.Turtle()

pbp = 55
length = 50.0

colors = ['pink','blue','purple','orange','green']
while pbp >0:
        coloor.color(random.choice(colors))
        coloor.forward(length)
	coloor.left(10)
	coloor.forward(length)
	coloor.left(10)
	coloor.forward(length)
	length = length - 5
	pbp = pbp -1
exitonclick()
