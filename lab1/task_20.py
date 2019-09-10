#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
	a=1
	b=0
	while not wall_is_beneath():
		move_down()
		b=b+1
	for i in range(b):
		move_up()
	while not wall_is_on_the_right():
		move_right()
		a=a+1
	a=a-3
	move_left()
	fill_cell()
	while b>2:
		for i in range(a):
			move_left()
			fill_cell()
		move_down()
		b=b-1
		for i in range(a):
			move_right()
		fill_cell()
	fill_cell()
	for i in range(a):
		move_left()
		fill_cell()
	move_down()
				


if __name__ == '__main__':
	run_tasks()
