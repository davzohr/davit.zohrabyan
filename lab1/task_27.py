#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
	a=1
	b=1
	move_right()
	fill_cell()
	while not wall_is_on_the_right():
		move_right()
		b=b-1
		if b==0:
			fill_cell()
			a=a+1
			b=a
	pass	
			


if __name__ == '__main__':
	run_tasks()
 
