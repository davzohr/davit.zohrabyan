import turtle as t
t.shape('turtle')
n=11
t.left(90*(1-3/n))
for i in range(n):
	t.forward(200)
	t.left(180*(1-1/n))
	
input()

