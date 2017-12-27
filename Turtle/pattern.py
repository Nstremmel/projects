import turtle as t
from time import sleep
from random import randint
t.speed("fastest")
while True:
	for i in range(4):
		for i in range(10):
			t.forward(10)
			t.left(90)
			t.forward(10)
			t.right(90)
		t.left(90)
	t.left(randint(1,10))
	


	#sleep(2)
#t.bye()