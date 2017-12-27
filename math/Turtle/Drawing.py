import turtle as t
from time import sleep
t.speed("fastest")




def left():
	t.setheading(180)
	t.forward(20)

def up():
	t.setheading(90)
	t.forward(20)

def right():
	t.setheading(0)
	t.forward(20)

def down():
	t.setheading(270)
	t.forward(20)

def space():
	t.pendown()
	t.setheading(0)
	for i in range(4):
		t.fd(40)
		t.right(90)
	t.setheading(0)

def clear(x,y):
	t.reset()
	t.speed("fastest")

t.onkeypress(left,"Left")
t.onkeypress(up,"Up")
t.onkeypress(right,"Right")
t.onkeypress(down,"Down")
t.onkey(space,"space")
t.onclick(clear)
t.listen()
#sleep(2)
#t.bye()