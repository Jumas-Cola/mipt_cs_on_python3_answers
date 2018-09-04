import turtle

def circle(dir):
	for i in range(360):
		turtle.forward(1)
		if dir=='l':
			turtle.left(1)
		if dir=='r':
			turtle.right(1)

turtle.shape('turtle')
n = 3
for i in range(n):
	circle('l')
	circle('r')
	turtle.left(180/n)


