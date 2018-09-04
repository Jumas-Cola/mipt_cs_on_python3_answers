#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
	size = 0
	while not wall_is_on_the_right():
		move_right()
		size+=1
	size += 1
	for i in range(1,size+1):
		for j in range(1,size+1):
			if not (i==j or size==i+j-1):
				fill_cell()
			print(i,j)
			if not (i==j and j==size):
				if (j==size) and not wall_is_beneath():
					move_down()
					continue
				if i%2!=0:
					move_left()
				else:
					move_right()
			

		
	   


if __name__ == '__main__':
    run_tasks()
