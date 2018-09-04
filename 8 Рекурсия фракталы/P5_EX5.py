import turtle


def mink(order, size):
    if order == 0:          # The base case is just a straight line
        turtle.forward(size)
    else:
        mink(order - 1, size / 8)
        turtle.left(90)
        mink(order - 1, size / 8)
        turtle.right(90)
        mink(order - 1, size / 8)
        turtle.right(90)
        mink(order - 1, size / 8)
        mink(order - 1, size / 8)
        turtle.left(90)
        mink(order - 1, size / 8)
        turtle.left(90)
        mink(order - 1, size / 8)
        turtle.right(90)
        mink(order - 1, size / 8)

turtle.speed('fastest')
order = 2

mink(order, 500)


