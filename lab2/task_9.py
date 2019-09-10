import turtle as t
t.shape('turtle')
n=3
x=30
for i in range(10):
	t.left((n-2)*90/n)
	for i in range(n):
		t.left(360/n)
		t.forward(x)
	t.right((n-2)*90/n)	
	t.penup()
	t.forward(10)
	t.pendown()
	n+=1
	x+=10
input()
	
