import turtle


def dragon(order, size, dir):
	if order == 0:          # The base case is just a straight line
		turtle.forward(size)
	else:
		if dir == 'r':
			turtle.right(45)
			dragon(order - 1, size/2**0.5, 'r')
			turtle.left(90)
			dragon(order - 1, size/2**0.5, 'l')
			turtle.right(45)
		elif dir == 'l':
			turtle.left(45)
			dragon(order - 1, size/2**0.5, 'r')
			turtle.right(90)
			dragon(order - 1, size/2**0.5, 'l')
			turtle.left(45)

turtle.speed('fastest')
order = 9
dragon(order, 250, 'r')


