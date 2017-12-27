import turtle as t
from time import sleep
from random import randint
import random
t.speed("fastest")
colors=["Red","Orange","Yellow","Blue","Green","Indigo","Violet"]
shapes=["turtle", "circle", "square", "triangle", "classic"]
while True:
	t.color(random.choice(colors))
	t.goto(randint(-200,200),randint(-200,200))
	t.shape(random.choice(shapes))
	t.clone()

	#sleep(2)
#t.bye()