#!/usr/bin/python3

from pyrob.api import *

def f():
	while not wall_is_on_the_right():
		fill_cell()
		move_right()
	fill_cell()	

@task
def task_5_10():
	while not wall_is_beneath():
		f()
		move_down()
		while not wall_is_on_the_left():
			move_left()
	f()
	while not wall_is_on_the_left():
		move_left()	
	
if __name__ == '__main__':
	run_tasks()
