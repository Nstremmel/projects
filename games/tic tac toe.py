from random import randint
from time import sleep

print ("Welcome to Tic Tac Toe!")
print ("")
sleep(.3)
input ("To pick who goes first, choose a player 1 and player 2. Press ENTER when you are finished.")
sleep (.2)
choice = randint(1,2)
first = choice
print ("")
print ("Player " + str(choice) + ", you will go first. (You are Os)")
print ("")
sleep (.2)
top = [".", " ", ".", " ", "."]
middle = [".", " ", ".", " ", "."]
bottom = [".", " ", ".", " ", "."]
while (True):
	area = input("Player " + str(choice) + ", type tl, tm, tr, ml, m, mr, bl, bm, or br. (t = top, m = middle, b = bottom, l = left, r = right) ")
	print ("")
	if area == ("stop"):
		break;
	if choice == first:
		xo = ("O")
	else:
		xo = ("X")
	if area == ("tl"):
		top[0]=(xo)
	elif area == ("tm"):
		top[2]=(xo)
	elif area == ("tr"):
		top[4]=(xo)
	elif area == ("ml"):
		middle[0]=(xo)
	elif area == ("m"):
		middle[2]=(xo)
	elif area == ("mr"):
		middle[4]=(xo)
	elif area == ("bl"):
		bottom[0]=(xo)
	elif area == ("bm"):
		bottom[2]=(xo)
	elif area == ("br"):
		bottom[4]=(xo)
	print(*top, sep='')
	print(*middle, sep='')
	print(*bottom, sep='')
	print ("")
	if all(x == (xo) for x in (top[0], top[2], top[4])):
		break;
	elif all(x == (xo) for x in (top[0], middle[0], bottom[0])):
		break;
	elif all(x == (xo) for x in (top[2], middle[2], bottom[2])):
		break;
	elif all(x == (xo) for x in (top[4], middle[4], bottom[4])):
		break;
	elif all(x == (xo) for x in (top[0], middle[2], bottom[4])):
		break;
	elif all(x == (xo) for x in (top[4], middle[2], bottom[0])):
		break;
	elif all(x == (xo) for x in (middle[0], middle[2], middle[4])):
		break;
	elif all(x == (xo) for x in (bottom[0], bottom[2], bottom[4])):
		break;
	choice = (3-int(choice))
print ("Player " + str(choice) + " Wins!!!!!")
input("Press ENTER to exit the game.")


