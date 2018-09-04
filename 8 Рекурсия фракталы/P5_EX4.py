import turtle


def koch(order, size):
	if order == 0:          # The base case is just a straight line
		turtle.forward(size)
	else:
		koch(order - 1, size / 3)
		turtle.left(60)
		koch(order - 1, size / 3)
		turtle.right(120)
		koch(order - 1, size / 3)
		turtle.left(60)
		koch(order - 1, size / 3)

turtle.speed('fastest')
order = 2

for i in range(3):
	koch(order, (order+1)*100)
	turtle.right(120)


