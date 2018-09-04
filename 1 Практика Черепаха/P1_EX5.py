import turtle

turtle.shape('turtle')
l=40
for i in range(10):
	for j in range(4):
		turtle.forward(l)
		turtle.left(90)
	turtle.right(180-45)
	turtle.penup()
	turtle.forward(12)
	turtle.pendown()
	turtle.left(180-45)
	l+=17

