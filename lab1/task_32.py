#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
	a=0
	b=0
	while not b==1:
		while not wall_is_on_the_right() and wall_is_above():
			if cell_is_filled():
				a=a+1
				move_right()
			else:
				fill_cell()
				move_right()	
		if wall_is_on_the_right():
			b=b+1
		else:	
			move_up()
			while not wall_is_above():
				if cell_is_filled():
					a=a+1
					move_up()
				else:
					fill_cell()
					move_up()
			if cell_is_filled():
				a=a+1
			else:
				fill_cell()
			while not wall_is_beneath():
				move_down()
			move_right()	
	mov('ax',a)		

if __name__ == '__main__':
	run_tasks()
