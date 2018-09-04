import turtle

turtle.shape('turtle')
seg=0.001
for i in range(360*8):
	turtle.forward(seg)
	turtle.left(1)
	seg+=0.0005
	
