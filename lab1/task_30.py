#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
	a=1
	while not wall_is_on_the_right():
		move_right()
		a=a+1
	e=a/2+1
	c=a-1
	a=a-2
	b=1
	d=b
	for i in range(a):
		move_left()
		fill_cell()
	move_left()
	while not c<e:
		move_down()
		for i in range(b):
			fill_cell()
			move_right()
		move_right()
		for i in range(a-2*b):
			fill_cell()
			move_right()
		while not wall_is_on_the_right():
			move_right()
			fill_cell()
		while not wall_is_on_the_left():
			move_left()
		c=c-1	
		b=b+1
	while not wall_is_beneath():
		move_down()
	a=1	
	while not wall_is_on_the_right():
		move_right()
		a=a+1	
	e=a/2+1
	c=a-1
	a=a-2
	b=1
	d=b
	for i in range(a):
		move_left()
		fill_cell()
	move_left()
	while not c<e:
		move_up()
		for i in range(b):
			fill_cell()
			move_right()
		move_right()
		for i in range(a-2*b):
			fill_cell()
			move_right()
		while not wall_is_on_the_right():
			move_right()
			fill_cell()
		while not wall_is_on_the_left():
			move_left()
		c=c-1	
		b=b+1
	a=a+2
	f=a//2
	move_up()
	for i in range(f):
		fill_cell()
		move_right()
	while not wall_is_on_the_right():
		move_right()
		fill_cell()
	while not wall_is_beneath():
		move_down()
	while not wall_is_on_the_left():
		move_left()				

					
			
	 
			
		
		
if __name__ == '__main__':
	run_tasks()
