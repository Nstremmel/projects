import turtle as t
import random
from time import sleep
import os
t.speed("fastest")
colors=["Orange", "Red", "White", "Yellow", "Blue", "Green"]
for i in range(3):
	colors.append("Orange")
	colors.append("Red")
	colors.append("White")
	colors.append("Yellow")
	colors.append("Blue")
	colors.append("Green")
def cube(x,y):
	global side
	global colors
	t.write("This is the "+side+" side of the cube.")
	t.write("Use your arrow keys to look at the other sides of the cube.", align="left", font="Fantasy, 30")
	t.speed("fastest")
	t.pencolor("white")
	t.goto(-100,50)
	t.pencolor("black")
	counter = (0)
	while (counter<4):
		if counter==2:
			t.pencolor("white")
			t.goto(-100,-50)
			t.pencolor("black")
		t.begin_fill()
		color = (random.choice(colors))
		if counter==(0):
			tl=(color)
		elif counter==1:
			tr=color
		elif counter==2:
			bl=color
		elif counter==3:
			br=color
		for i in colors:
			if color==i:
				colors.remove(color)
				break;
		t.fillcolor(color)
		t.forward(100)
		for i in range(4):
			t.left(90)
			t.forward(100)
		t.end_fill()
		counter+=(1)
	t.onkey(left,"Left")
	t.onkey(up,"Up")
	t.onkey(right,"Right")
	t.onkey(down,"Down")
	t.listen()

def intro():
	t.write("Use your arrow keys to look at the sides of the cube.", align="left", font="Fantasy, 30")
	sleep (2)
	side=("front")
	cube(0,0)


def left():
	#side+=(1)
	cube()
	#side-=(1)
	side=("left")
def up():
	cube()
	side=("top")
def right():
	cube()
	side=("right")
def down():
	cube()
	side=("bottom")




print ("Welcome To...The 2 by 2 Rubix Cube!")
sleep (1)
print ("")
print ("MIXING UP THE CUBE...")
sleep (2)
os.system("cls")
intro()





sleep(2)
turtle.bye()

