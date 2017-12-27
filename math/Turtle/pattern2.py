from time import sleep
from random import randint
import random
import turtle as t
t.speed("fastest")


for i in range(276):
	t.circle(30)
	t.right(90)
	t.fd(i*1.5)
	t.right(1)
t.penup()
t.home()
t.setheading(90)
t.pendown()
x=0
for i in range(152):
	t.fd(i*2)
	t.right(90)
	t.fd(i*2)
	t.right(90)
	t.fd(i*2)
	t.right(90)
	t.fd(i*2)
	t.setheading(90)
	t.left(x)
	x+=90
t.bye()