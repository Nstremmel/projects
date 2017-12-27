import turtle as t
from time import sleep
from random import randint
import random

aliens=[]
counter=(1)
counter1=(1)
counter2=(1)
t.speed("fastest")
t.forward(200)
t.left(180)
t.forward(400)
t.home()
t.penup()

def make():
	t.goto(-150,100)
	first=t.clone()
	aliens.append(first)
	first.color('Red')
	t.forward(50)
	second=t.clone()
	aliens.append(second)
	second.color("Orange")
	t.forward(50)
	third=t.clone()
	aliens.append(third)
	third.color("Yellow")
	t.forward(50)
	fourth=t.clone()
	aliens.append(fourth)
	fourth.color('Green')
	t.forward(50)
	fifth=t.clone()
	aliens.append(fifth)
	fifth.color('Blue')
	t.forward(50)
	sixth=t.clone()
	aliens.append(sixth)
	sixth.color('Indigo')
	t.forward(50)
	last=t.clone()
	aliens.append(last)
	last.color("Violet")

make()
t.goto(0,150)
t.write("Space Invaders", font=("Arial", 50, "normal"), align="center")
t.home()
t.left(90)






def left():
	t.speed("fastest")
	t.setheading(180)
	t.forward(5)

def right():
	t.speed("fastest")
	t.setheading(0)
	t.forward(5)

def space():
	global aliens
	t.speed("fastest")
	t.setheading(90)
	bullet=t.clone()
	bullet.shape("circle")
	bullet.turtlesize(.3,.3,.3)
	bullet.speed("slowest")
	bullet.forward(100)
	for i in aliens:
		if round(bullet.xcor())==i.xcor():
			i.goto(-2345,0)
			aliens.remove(i)
	bullet.ht()
	if aliens==[]:
		t.goto(0,-100)
		t.write("Level Beaten!", font=("Ariel", 30, "normal"), align="center")
		sleep(2)
		respawn()


def move():
	t.speed("slowest")
	distance=randint(2,4+counter1)*5
	for i in aliens:
		i.forward(distance)
		i.left(180)
	x=random.choice(aliens)
	bomb=x.clone()
	bomb.speed(counter2)
	bomb.shape("circle")
	bomb.color("red")
	bomb.turtlesize(.3,.3,.3)
	bomb.setheading(270)
	bomb.forward(100)
	bomb.ht()
	if round(bomb.xcor())==round(t.xcor()):
		t.bye()
	sleep(counter)
def home(x,y):
	t.home()
	t.left(90)

def respawn():
	global counter
	global counter1
	global counter2
	counter-=(.1)
	counter1+=(1)
	counter2+=(.3)
	t.home()
	make()
	t.home()
	t.left(90)




t.onclick(home)
t.onkey(space,"space")
t.onkeypress(left,"Left")
t.onkeypress(right,"Right")
t.onkey(respawn, "r")
t.listen()
sleep(1)
while len(aliens)>0:
	if abs(round(t.xcor()))>200:
		t.home()
	move()
#sleep(2)
#t.bye()