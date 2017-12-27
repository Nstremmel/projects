import turtle as t
from time import sleep
from random import randint
import random
import os

t.speed("fastest")
x=1

while True:
	#t.pensize(x)
	t.circle(30)
	t.fd(30+x)
	t.right(150)
	x+=2