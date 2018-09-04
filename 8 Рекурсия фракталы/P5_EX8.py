import turtle


def kantor(order, size):
	if order == 0:          # The base case is just a straight line
		turtle.forward(size)
	else:
		turtle.forward(size)

		turtle.penup()
		turtle.right(90)
		turtle.forward(10)
		turtle.right(90)
		turtle.forward(size)
		turtle.right(180)
		turtle.pendown()

		kantor(order - 1, size/3)
		turtle.penup()
		turtle.forward(size/3)
		turtle.pendown()
		kantor(order - 1, size/3)

		turtle.penup()
		turtle.left(90)
		turtle.forward(10)
		turtle.right(90)
		turtle.pendown()



turtle.speed('fastest')
order = 4
kantor(order, 300)


