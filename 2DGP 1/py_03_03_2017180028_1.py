import turtle


	
def draw_i(a, b):
	turtle.penup()
	turtle.goto(a,b)
	turtle.pendown()
	turtle.goto(a,b-150)

	
def draw_d(a,b):
	turtle.penup()
	turtle.goto(a,b)
	turtle.pendown()
	turtle.goto(a+80,b)
	turtle.goto(a, b)
	turtle.goto(a,b-60)
	turtle.goto(a+80,b-60)
	turtle.penup()

	
def draw_o(a,b):
	turtle.penup()
	turtle.goto(a,b)
	turtle.pendown()
	turtle.goto(a, b-30)
	turtle.goto(a+50, b-30)
	turtle.goto(a-70, b-30)

	
def draw_circle1(a, b, c):
	turtle.penup()
	turtle.goto(a,b)
	turtle.pendown()
	turtle.circle(c)

	
def draw_ye2(a,b):
	turtle.penup()
	turtle.goto(a,b)
	turtle.pendown()
	turtle.goto(a+30,b)
	turtle.goto(a+30,b+60)
	turtle.goto(a+30,b-50)
	turtle.penup()
	turtle.goto(a,b+20)
	turtle.pendown()
	turtle.goto(a+30,b+20)


	
draw_circle1(-300, 30, 30)
draw_i (-240,120)
draw_d (-200, 90)
draw_o (-150,30)
draw_circle1(-30, 70, 25)


	
draw_ye2(0,90)
draw_circle1(10, 0, 30)
exitonclick()
