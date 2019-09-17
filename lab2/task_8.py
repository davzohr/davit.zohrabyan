import turtle as t
from math import sin, pi

def polygon(r,n):
	a=r*2*sin(pi/n)
	for i in range(n):
		t.forward(a)
		t.left(360/n)

t.shape('turtle')
r=0
n=3
for i in range(10):
	r+=30
	t.penup()
	t.forward(30)
	t.pendown()
	t.left(180-(n-2)*90/n)
	polygon(r,n)
	t.right(180-(n-2)*90/n)
	n+=1	
input()
	
