import turtle


def levi(order, size):
    if order == 0:          # The base case is just a straight line
        turtle.forward(size)
    else:
    	turtle.left(45)
    	levi(order - 1, size)
    	turtle.right(90)
    	levi(order - 1, size)
    	turtle.left(45)

turtle.speed('fastest')
order = 9

levi(order, 10)


