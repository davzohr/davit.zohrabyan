#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
	a=0
	while not a==1:
		while not wall_is_beneath():
			move_down()
		while not wall_is_on_the_right():
			move_right()
		while wall_is_beneath() and not wall_is_on_the_left():	
			move_left()
		if wall_is_beneath():
			a+=1
			
		
	


if __name__ == '__main__':
	run_tasks()
