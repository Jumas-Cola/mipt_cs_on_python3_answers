#!/usr/bin/python3

from pyrob.api import *

def fill_cross():
	fill_cell()
	move_up()
	fill_cell()
	move_down()
	move_left()
	fill_cell()
	move_right(2)
	fill_cell()
	move_down()
	move_left()
	fill_cell()
	move_up()


@task(delay=0.02)
def task_2_4():
	move_down()
	move_right()
	for j in range(2):
		for i in range(9):
			fill_cross()
			move_right(4)
		fill_cross()
		move_down(4)
		for i in range(9):
			fill_cross()
			move_left(4)
		fill_cross()
		move_down(4)
	for i in range(9):
		fill_cross()
		move_right(4)
		fill_cross()
	move_left(36)
	move_up()
	move_left()


if __name__ == '__main__':
    run_tasks()
