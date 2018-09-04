#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
	x=0
	while not (wall_is_on_the_right() and not wall_is_on_the_left()):
		if not wall_is_above() and wall_is_beneath():
			while not wall_is_above():
				move_up()
				if cell_is_filled():
					x+=1
				else:
					fill_cell()
			while not wall_is_beneath():
				move_down()
		else:
			fill_cell()
		move_right()
	mov('ax',x)


if __name__ == '__main__':
    run_tasks()
