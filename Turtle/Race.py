import turtle as t
from time import sleep
counter = (0)
def square(x,y):
	global counter
	counter+=(1)
	for i in range(4):
		t.clone()
		t.forward(5)
		t.left(5)
	if counter==18:
		print ("Winner!")
		return;
	t.onclick(square)
	t.mainloop()
square(3,5)

sleep(2)
t.bye()