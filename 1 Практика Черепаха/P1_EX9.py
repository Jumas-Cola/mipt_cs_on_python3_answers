import turtle
import math

def plot_n_angle(n,a):
	for i in range(n):
		turtle.forward(a)
		turtle.left(360/n)

turtle.shape('turtle')

R = 15
for n in range(3,12):
	turtle.left(90+(360/(2*n)))
	a = R*2*math.sin(2*math.pi/(2*n))
	plot_n_angle(n,a)
	turtle.right(90+(360/(2*n)))
	turtle.penup()
	turtle.forward(15)
	turtle.pendown()
	R+=15

