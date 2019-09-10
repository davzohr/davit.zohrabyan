#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
	if wall_is_above():
		if wall_is_on_the_right():
			move_left(n=9)
			move_down(n=9)	
		else:
			move_right(n=9)
			move_down(n=9)
	else:
		if wall_is_on_the_right():
			move_up(n=9)
			move_left(n=9)	
		else:
			move_up(n=9)
			move_right(n=9)

if __name__ == '__main__':
	run_tasks()
