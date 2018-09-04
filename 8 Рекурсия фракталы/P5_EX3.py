import turtle


def koch(order, size):
    if order == 0:          # The base case is just a straight line
        turtle.forward(size)
    else:
        koch(order-1, size/3)   # Go 1/3 of the way
        turtle.left(60)
        koch(order-1, size/3)
        turtle.right(120)
        koch(order-1, size/3)
        turtle.left(60)
        koch(order-1, size/3)



turtle.speed('fastest')
koch(3, 100)