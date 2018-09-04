import turtle

def circle(dir,seg):
	for i in range(360):
		turtle.forward(seg)
		if dir=='l':
			turtle.left(1)
		if dir=='r':
			turtle.right(1)

turtle.shape('turtle')
n = 12
seg = 0.5
turtle.right(90)
for i in range(n):
	circle('l',seg)
	circle('r',seg)
	seg+=0.1


