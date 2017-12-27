import turtle as t
from time import sleep
from random import randint
import random
t.speed("fastest")
colors=["red","yellow","green","blue"]
first=t.clone()
t.fd(100)
second=t.clone()
t.goto(0,-100)
third=t.clone()
t.fd(100)
fourth=t.clone()
turtles=[first,second,third,fourth]
for i in turtles:
	i.shape("square")
	i.shapesize(5,5,5)
while True:	
	first.color(colors[0])
	second.color(colors[3])
	third.color(colors[1])
	fourth.color(colors[2])
	colors[0],colors[1],colors[2],colors[3]=colors[3],colors[0],colors[1],colors[2]



