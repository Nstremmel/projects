from time import sleep
from random import randint
import random
import os
import turtle as t

#setup
t.speed("fastest")
t.pensize(3)
t.penup()
t.goto(-200,300)
t.pendown()
x=250
y=0
nty=[0,2,4,6,9,11,13,15,16,18,20,22,41,43,45,47,48,50,52,54,57,59,61,63,25,27,29,31,32,34,36,38]
plz=[1,3,5,7,8,10,12,14,17,19,21,23,40,42,44,46,49,51,53,55,56,58,60,62]
white=[1,3,5,7,8,10,12,14,17,19,21,23]
red=[40,42,44,46,49,51,53,55,56,58,60,62]
pieces=list(range(64))

#creating board
def square(x,color):
	t.fillcolor(color)
	t.begin_fill()
	for i in range(4):
		t.fd(x)
		t.right(90)
	t.end_fill()

for i in range(8):
	for i in range(8):
		if y in nty:
			square(50,"white")
		else:
			square(50,"black")
		if y in plz:
			pieces[y]=t.clone()
		t.fd(50)
		y+=1
	t.penup()
	t.goto(-200,x)
	t.pendown()
	x-=50



#asigning
for i, value in enumerate(pieces):
	if i in plz:
		value.penup()
		value.fd(25)
		value.right(90)
		value.fd(25)
		value.turtlesize(1,1,1)
		value.shape("turtle")
		if i in white:
			value.color("white")
		else:
			value.color("red")
			value.right(180)

#functions
def right():
	i.fd(50)
	i.right(90)
	i.fd(50)
	i.setheading(90)
def left():
	i.fd(50)
	i.left(90)
	i.fd(50)
	i.setheading(90)
def move():
	i.color("blue")
	t.onkey(right,"Right")
	t.onkey(left,"Left")
	t.listen()




#Gameplay
##########################################################################################################################
# input ("To pick who goes first, choose a player 1 and player 2. Press ENTER when you are finished.")
# sleep (.2)
# choice = randint(1,2)
# print ("")
# print ("Player " + str(choice) + ", you will go first. (You are Red)")

while True:
	sleep(.1)
	for i in pieces:
		if i in red:
			print("check")
			t.onclick(move)
			t.listen()
			sleep(.5)