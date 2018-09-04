#!/usr/bin/python3

from pyrob.api import *

def stairway(n, dir):
	for i in range(n):
		if dir == 'd':
			fill_cell()
			move_down()
			fill_cell()
			move_right()
		elif dir == 'u':
			fill_cell()
			move_up()
			fill_cell()
			move_left()
	if dir == 'd':
		fill_cell()
		move_left(2)
		fill_cell()
		move_left()
	elif dir=='u':
		move_down(2)
		move_right()


@task(delay=0.05)
def task_4_11():
    move_down()
    move_right()
    stairway(12,'d')
    
    stairway(10,'u')

    stairway(8,'d')

    stairway(6,'u')

    stairway(4,'d')

    stairway(2,'u')
    fill_cell()
    move_down()



if __name__ == '__main__':
    run_tasks()
