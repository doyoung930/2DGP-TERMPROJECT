
import turtle
count = 6
while (count > 0):
	turtle.penup()
	turtle.goto(100*count,0)
	turtle.pendown()
	turtle.goto(100 * count ,500)
	count = count - 1

	
count = 6
while (count > 0):
	turtle.penup()
	turtle.goto(100,(count-1)*100)
	turtle.pendown()
	turtle.goto(600 ,(count-1) *100)
	count = count - 1

	
exitonclick()


