import turtle

def curve(dir,seg):
	for i in range(180):
		turtle.forward(seg)
		if dir=='l':
			turtle.left(1)
		if dir=='r':
			turtle.right(1)

turtle.shape('turtle')
n = 5
seg = 0.5
turtle.left(90)
for i in range(n):
	seg = 0.8
	circle('r',seg)
	seg = 0.1
	circle('r',seg)


