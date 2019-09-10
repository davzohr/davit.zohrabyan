#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
	a=0
	while not wall_is_on_the_right() and not a==3:
		move_right()
		if cell_is_filled():
			a=a+1
		else:
			a=0	
		
if __name__ == '__main__':
	run_tasks()
