import turtle as t
from time import sleep
from random import randint
import random
import os

t.left(50)
t.penup()
t.goto(350,0)
t.pendown()
x=90
t.speed("fastest")
while True:
	for i in range(4):
		#t.pensize(5)
		t.circle(30)
		t.fd(10)
	t.fd(5)
	t.right(x)
	x-=(2)