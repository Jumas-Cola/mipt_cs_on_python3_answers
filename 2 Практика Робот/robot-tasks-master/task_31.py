#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    width = 0
    while not wall_is_on_the_left():
    	move_left()
    	width+=1
    while True:
    	while not wall_is_on_the_right():
    		if not wall_is_beneath():
    			move_down()
    		move_right()
    	if not wall_is_beneath():
    			move_down()
    	l = 0
    	while not wall_is_on_the_left():
    		if not wall_is_beneath():
    			move_down()
    			l=0
    		move_left()
    		l+=1
    	if l==width:
    		break


if __name__ == '__main__':
    run_tasks()
