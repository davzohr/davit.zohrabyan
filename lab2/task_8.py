import turtle as t
from math import sin, pi

t.shape('turtle')
n=3
r=0
for i in range(10):
	r+=10
	t.penup()
	t.forward(10)
	t.pendown()
	t.left(180-(n-2)*90/n)
	a=r*2*sin(pi/n)
	for i in range(n):
		t.forward(a)
		t.left(360/n)
	t.right(180-(n-2)*90/n)
	n+=1	
input()
	
