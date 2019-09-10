#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
	a=0
	while not wall_is_beneath():
		move_down()
	while wall_is_beneath():
		move_right()
		a=a+1
	move_down()
	while a>0:
			move_left()
			a=a-1


if __name__ == '__main__':
	run_tasks()
