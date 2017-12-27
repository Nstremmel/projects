import turtle as t
from time import sleep
from random import randint
import random
import os

t.speed("fastest")
colors=["Red","Orange","Yellow","Blue","Green","Indigo","Violet"]
x=30
while True:
	for i in range(randint(20,30)):
		t.fd(randint(10,40))
		t.right(randint(10,x))
		t.color(random.choice(colors))
	x+=5