import turtle as t
from time import sleep
from random import randint
import random
t.speed("fastest")
t.fillcolor("black")
t.shape("circle")
t.shapesize(.3, .3, .3)
t.pensize(5)

t.penup()
t.goto(-50,100)
t.pendown()
t.forward(100)
t.right(120)
t.begin_fill()
t.forward(200)
t.left(120)
t.forward(100)
t.left(120)
t.forward(10)
t.left(60)
t.forward(90)
t.end_fill()
t.left(180)
t.forward(90)
t.left(120)
t.begin_fill()
t.forward(110)
t.right(120)
t.forward(20)
t.right(120)
t.forward(20)
t.right(120)
t.end_fill()
t.forward(100)


t.ht()
t.penup()
t.home()
t.right(90)

while True:
	for i in range(8):
		t.st()
		sleep(.8)
		t.ht()
		t.forward(10)
	t.goto(0,0)


#sleep(2)
#t.bye()