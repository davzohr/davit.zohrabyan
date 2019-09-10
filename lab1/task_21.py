#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
	move_right()
	move_down()
	a=0
	while not wall_is_beneath():
		move_down()
		a=a+1
	b=a-1
	while a>1:	
		for i in range(a):
			move_up()
			fill_cell()
		move_right()
		move_down()
		a=a-1
		for i in range(a):
			fill_cell()
			move_down()
		move_right()
		a=a-1
	move_up()
	fill_cell()
	move_down()
	for i in range(b):
		move_left()	

if __name__ == '__main__':
	run_tasks()
