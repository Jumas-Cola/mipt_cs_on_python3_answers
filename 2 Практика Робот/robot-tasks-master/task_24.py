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


@task
def task_2_1():
    move_down()
    move_right()
    move_down()
    move_right()
    fill_cross()
    move_up()
    move_left()


if __name__ == '__main__':
    run_tasks()
