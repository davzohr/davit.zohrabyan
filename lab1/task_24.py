#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
	move_down(n=2)
	for i in range(3):
		move_right()
		fill_cell()
	move_left()
	move_down()
	fill_cell()
	move_up(n=2)
	fill_cell()
	move_left()

if __name__ == '__main__':
	run_tasks()
