#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
	if wall_is_above():
		while wall_is_above()and not wall_is_on_the_left():
			move_left()
		if wall_is_on_the_left():
			if wall_is_above():
				while wall_is_above():
					move_right()
				while not wall_is_above():
					move_up()
				while not wall_is_on_the_left():
					move_left()
			else:
				while not wall_is_above():
					move_up()
				while not wall_is_on_the_left():
					move_left()
		else:
			while not wall_is_above():
				move_up()
			while not wall_is_on_the_left():
				move_left()					
	else:
		while not wall_is_above():
			move_up()
		while not wall_is_on_the_left():
			move_left()

if __name__ == '__main__':
	run_tasks()
