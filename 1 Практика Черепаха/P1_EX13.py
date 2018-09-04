from turtle import *

def circle(dir,seg):
	for i in range(360):
		forward(seg)
		if dir=='l':
			left(1)
		if dir=='r':
			right(1)

def curve(dir,seg):
	for i in range(180):
		forward(seg)
		if dir=='l':
			left(1)
		if dir=='r':
			right(1)

shape('turtle')

fillcolor('yellow')

penup()
goto(0,50)
pendown()

begin_fill()
circle('r',1)
end_fill()

penup()
goto(-20,30)
pendown()

fillcolor('blue')

begin_fill()
circle('r',0.2)
end_fill()

penup()
goto(20,30)
pendown()

begin_fill()
circle('r',0.2)
end_fill()

penup()
goto(0,5)
pendown()
width(10)
goto(0,-12)

penup()
right(90)
goto(35,-15)
pendown()
color('red')
curve('r',0.6)



