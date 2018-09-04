import turtle


def plot_star(n, l):
	for i in range(n):
		turtle.forward(l)
		turtle.left(180-180/n)

turtle.shape('turtle')
plot_star(11,150)
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
plot_star(5,150)