import turtle

notShawn = turtle.Turtle()

count = 0
while count < 20:
	notShawn.forward(5)
	notShawn.penup()
	notShawn.forward(5)
	notShawn.pendown()
	count = count + 1	

turtle.exitonclick()

# go to the lower left of the screen
notshawn.penup()
notshawn.goto(-100, -55)
# when get there, draw me a circle
notshawn.pendown()
notshawn.circle(10)


