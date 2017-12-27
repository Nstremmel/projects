from time import sleep
import os
import random
from random import randint
import turtle as t
t.speed("fastest")
t.shape("square")
t.shapesize(.2,.2,.2)
t.pensize(10)
t.penup()
t.goto(-100,100)
counter=100
def make():
	global counter
	for i in range(10):
		t.clone()
		t.fd(30)
		counter-=(30)
		t.goto(-100,counter)

make()
def change(x,y):
	t.color("blue")
t.onclick(change)
t.listen()



