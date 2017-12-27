import turtle as t
from time import sleep
from random import randint
import random


def sides(x):
	for i in range(x):
		t.clone()
		t.fd(70)

def score(x,y):
	global i
	myarray2[i].write(myarray[i])
	global points
	if value=='BOMB':
		t.speed("fastest")
		t.home()
		t.turtlesize(7,7,7)
		t.shape("square")
		t.goto(-310,355)
		t.setheading(270)
		amount=9
		for i in range(5):
			for i in range(2):
				sides(amount)
				t.left(90)
			amount-=2
		t.clone()
		t.goto(-175 ,0)
		t.pencolor("white")
		t.pendown()
		t.write("Game Over", align="left", font=("Fantasy", 50))
		t.pencolor("black")
		t.penup()
		t.goto(2424,24242)
		sleep(3)
		t.bye()

	points+=i
	t.reset()
	t.penup()
	t.goto(0,250)
	t.write(str(points))



t.speed("fastest")
t.penup()


points=0
myarray=list(range(1,101))
myarray2=list(range(1,101))

t.goto(-275,200)
y=200
z=0
for i in range(10):
	for i in range(10):
		number=randint(1,100)
		if number in range(0,36):
			myarray[z]=1
		elif number in range(35,61):
			myarray[z]=2
		elif number in range(60,76):
			myarray[z]=3
		elif number in range(75,86):
			myarray[z]=4
		elif number in range(85,89):
			myarray[z]=5
		else:
			myarray[z]="BOMB"

		myarray2[z]=t.clone()
		myarray2[z].shape("square")
		myarray2[z].fillcolor("white")
		myarray2[z].turtlesize(2,2,2)
		t.fd(60)
		z+=1
	y-=50
	t.goto(-275,y)


for i in range(10):
        print(str(myarray[i]))




while True:
	for i, value in enumerate(myarray):
		myarray2[i].onclick(score)
		#sleep(1)
		t.listen()




