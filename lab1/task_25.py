#!/usr/bin/python3

from pyrob.api import *

def f():
	fill_cell()
	for i in range(2):
		move_right()
		fill_cell()
	move_left()
	move_down()
	fill_cell()
	move_up(n=2)
	fill_cell()
	move_down()
	move_right()	

@task
def task_2_2():
	move_down(n=2)
	f()
	while not wall_is_on_the_right():
		move_right(n=2)
		f()
	move_up()
	move_left(n=2)				
		

if __name__ == '__main__':
	run_tasks()
