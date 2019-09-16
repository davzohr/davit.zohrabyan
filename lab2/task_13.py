import turtle as t
from math import pi
def arc():
	for i in range(180):
		t.forward(70*pi/180)
		t.right(1)
t.shape('turtle')
t.left(90)
t.penup()
t.goto(100,0)
t.pendown()
t.color('black','yellow')
t.begin_fill()
t.circle(100)
t.end_fill()
t.penup()
t.goto(-30,50)
t.pendown()
t.color('black','blue')
t.begin_fill()
t.circle(10)
t.end_fill()
t.penup()
t.goto(45,50)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()
t.penup()
t.goto(0,35)
t.pendown()
t.pensize(8)
t.color('black')
t.backward(40)	
t.penup()
t.goto(70,0)
t.pendown()
t.right(180)
t.color('red')
arc()
	
input()





