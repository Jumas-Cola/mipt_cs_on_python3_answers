#!/usr/bin/python3

from pyrob.api import *

def esc():
	while (not wall_is_above()):
		move_up()
	while (not wall_is_on_the_left()):
		move_left()


@task
def task_8_29():
    while (wall_is_above() and not wall_is_on_the_right()):
    	move_right()
    if (not wall_is_above()):
    	esc()
    else:
    	r = True
    	while (wall_is_above() and not wall_is_on_the_left()):
    		move_left()
    	if (not wall_is_above()):
    		esc()
    	else:
    		while (not wall_is_on_the_right()):
    			move_right()


if __name__ == '__main__':
    run_tasks()
