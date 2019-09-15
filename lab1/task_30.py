#!/usr/bin/python3

from pyrob.api import *

def left():
	while not wall_is_on_the_left():
		move_left()	

@task(delay=0.01)
def task_9_3():
	a=1
	b=1
	c=1
	while not wall_is_on_the_right():
		move_right()
		a+=1
	left()
	while not wall_is_beneath():	
		for i in range(a-1):
			if c==b or c==(a-b+1):
				move_right()
				c+=1
			else:
				fill_cell()
				move_right()
				c+=1
		b+=1
		c=1	
		if not b==2:
			fill_cell()	
		move_down()
		left()
	for i in range(a-2):
		move_right()
		fill_cell()
	left()
		
		
		
if __name__ == '__main__':
	run_tasks()
