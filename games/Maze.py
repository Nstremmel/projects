from random import randint
from time import sleep
import os
import sys
import random


path=("C:\\Users\\nstremmel\\Git\\Sublime\\Documents\\Maze.txt")

###################################################################################

#Maze is 47 by 13
#45 spaces inside 
def encounter():
	global gold
	t.Turtle._screen = None
	t.TurtleScreen._RUNNING = True
	text ("BATTLE FOUND!")
	t.speed("fastest")
	t.penup()
	t.turtlesize(2,2,2)
	t.setheading(0)
	t.goto(-250,300)
	t.pendown()
	t.begin_fill()
	t.fd(int(player.hitpoints))
	t.right(90)
	t.fd(50)
	t.right(90)
	t.fd(int(player.hitpoints))
	t.right(90)
	t.fd(50)
	t.end_fill()
	t.penup()
	t.goto(100,300)
	t.pendown()
	t.begin_fill()
	t.setheading(0)
	t.fd(creature1.hitpoints)
	t.right(90)
	t.fd(50)
	t.right(90)
	t.fd(creature1.hitpoints)
	t.right(90)
	t.fd(50)
	t.end_fill()
	t.penup()
	t.goto(-300,-0)
	t.pensize(15)
	t.setheading(0)
	t.pendown()
	t.fd(600)
	t.setheading(270)
	t.fd(300)
	t.right(90)
	t.fd(600)
	t.right(90)
	t.fd(300)
	t.penup()
	t.goto(-150,-250)
	third=t.clone()
	t.write("Special Attack", font=("Ariel", 20, "normal"), align="center")
	t.fd(200)
	first=t.clone()
	t.write("Normal Attack", font=("Ariel", 20, "normal"), align="center")
	t.right(90)
	t.fd(300)
	t.left(90)
	second=t.clone()
	t.write("Defensive Move", font=("Ariel", 20, "normal"), align="center")
	t.right(180)
	t.fd(200)
	t.write("Flee", font=("Ariel", 20, "normal"), align="center")
	t.setheading(90)
	fourth=t.clone()
	t.goto(200,100)
	t.shape("turtle")
	t.turtlesize(5,5,5)
	enemy=t.clone()
	enemy.color("red")
	enemy.left(90)
	t.goto(-200,100)
	t.color("blue")
	t.right(90)
	arrows=[first,second,third,fourth]

	def move():
		for i in arrows:
			i.ht()
		sleep(.3)
		for i in arrows:
			i.st()
		sleep(.5)

	def attack(x,y):
		x.speed("slowest")
		x.fd(250)
		sleep(.5)
		x.speed(5)
		x.fd(75)
		sleep(.5)
		x.speed(3)
		x.right(180)
		x.fd(315)
		x.right(180)


	def player(x,y):
		attack(t,0)
	def opponent(x,y):
		attack(enemy,0)

	def remove(a,b):
		t.speed("fastest")
		t.goto(a+b,300)
		t.setheading(180)
		t.pendown()
		t.pencolor("white")
		t.pensize(30)
		t.fd(damage)
		t.penup()
		t.goto(-200,100)
		t.right(180)
		t.pencolor("blue")
#	third.onclick(hi)
#	fourth.onclick(hi)
#	t.listen()

	#while True:
	#	move()



	
	player_turn=(True)
	while (True):
		sleep(1)
		# first.onclick(None)
		# second.onclick(defence_increase)
		# third.onclick(attack_increase)
		# fourth.onclick(Flee)
		# t.listen()
		

		creature1.hitpoints -= player.power-(creature1.defence/5)


		player(0,0)
		remove(100,opponent.hitpoints)


		if opponent_hitpoints < (1):
			t.bye()
			os.system("cls")
			text ("Congrats! You survived the battle.")
			sleep (.5)
			print ("")
			player.hitpoints = int(open(path).readlines()[19].splitlines()[0])
			text ("You get " + str(creature1.level*10) + " gold.")
			gold+=creature1.level*10
			linereplace(17,str(gold))
			print("")
			input("Press ENTER to continue.")
			break;




		player.hitpoints -= creature1.power-(player.defence/5)


		opponent(0,0)
		remove(-250,player.hitpoints)

		if player_hitpoints < 1:
			t.bye()
			os.system("cls")
			text ("Oh dear, you are dead.")
			sleep (.5)
			print ("")
			player_hitpoints = int(open(path).readlines()[19].splitlines()[0])
			if gold < 10:
				text ("You have lost all your gold.")
				print ("")
				gold = (0)
				linereplace(17,str(gold))
				input("Press ENTER to continue.")
				break;
			else:
				text ("You have lost 10 percent of your gold.")
				print ("")
				gold -= .1*gold
				linereplace(17,str(gold))
				input("Press ENTER to continue.")
				break;
		player_turn=(True)
		continue
	os.system("cls")

def linereplace(line, var):
	f=open(path, "r")
	f1=open("C:\\Users\\nstremmel\\Git\\Sublime\\Documents\\host.txt", "w")
	counter=0
	for i in f:
		if counter==int(line):
			f1.write(var)
		else:
			f1.write(i)
		counter+=1
	f.close()
	f2=open(path, "w")
	f1=open("C:\\Users\\nstremmel\\Git\\Sublime\\Documents\\host.txt", "r")
	for line in f1:
		f2.write(line)
	f1.close()
	f2.close()
	os.system("del \"C:\\Users\\nstremmel\\Git\\Sublime\\Documents\\host.txt\"")

def replace(row, x, character):
	characters=[]
	characters+=open(path).readlines()[row]
	characters[x]=str(character)
	linereplace(row, str(''.join(characters)))

def text(x):
	for i in x:
		sys.stdout.write(i)
		sys.stdout.flush()
		sleep(.005)
	print ("")

def pause(x):
	sleep(x)
	os.system("cls")

def roll():
	global row, x, treasure, gold
	roll=randint(1,100)
	row=int(open(path).readlines()[14].splitlines()[0])
	x=int(open(path).readlines()[15].splitlines()[0])
	print("")
	if str(row)+" "+str(x)==treasure:
		earnings=randint(300,500)
		print("Congradulations! You have beaten this level of The Maze and earned yourself "+str(earnings)+" gold pieces!")
		gold+=earnings
		#hide the sleep after reset is added
		sleep(5)
		exit()
		#add reset system
	
	if roll in range(0,61):
		replace(row,x,"@")
	elif roll in range(60,81):
		os.system("cls")
		text("You run into a "+random.choice(creatures1)+"!")
		replace(row,x,"C")
		#encounter()
		sleep(3)
	elif roll in range(80,99):
		text("You found "+str(randint(30,66))+" gold pieces!")
		replace(row,x,"@")
		sleep(1.5)
	elif roll in range(98,101):
		text("Congradulations! You found "+random.choice(followers)+"! This is a pet that will help you in The Maze.")
		replace(row,x,"@")
		sleep(2)


##############################################################################################
odds=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45]
followers=["Henry the Dog", "Sprout the parvum lignum", "Gerald the Cat"]
creatures1=["rat", "bat", "mouse", "spider"]
creatures2=["Barbarian", ""]
##############################################################################################


try:
	test=int(open(path).readlines()[14].splitlines()[0])
except:
	text("Oh...")
	pause(1)
	text("You seem new here...")
	pause(2)
	text("This is The Maze.")
	pause(2)
	text("Here, I'll show you around!    (Press ENTER when ready or type \"skip\" to skip the tutorial) ")
	tutorial=input("").lower()
	if tutorial!="skip":
		os.system("\"C:\\Users\\Andy\\Documents\\Sublime\\games\\tutorial.py\"")
	f=open(path, "a")
	f.write("13\n")
	f.write("23\n")
	f.write(str(randint(1,12))+" "+str(random.choice(odds))+"\n")
	f.write("0\n")
	f.write("1\n")
	f.write("10\n")
	f.write("1\n")
	f.write("1\n")
	replace(13,23,"@")
	f.close()

##############################################################################################



os.system("cls")
while True:
	class player:
		power=int(open(path).readlines()[18].splitlines()[0])
		hitpoints=int(open(path).readlines()[19].splitlines()[0])
		defence=int(open(path).readlines()[20].splitlines()[0])
		level=int(open(path).readlines()[21].splitlines()[0])
	class creature1:
		power=0.5
		hitpoints=5
		defence=0
		level=1
	row=int(open(path).readlines()[14].splitlines()[0])
	x=int(open(path).readlines()[15].splitlines()[0])
	treasure=str(open(path).readlines()[16].splitlines()[0])
	print(treasure)
	gold=int(open(path).readlines()[17].splitlines()[0])
	print("--------------------------")
	print("| 1. Shop                 |")
	print("| 2. Adventure            |")
	print("| 3. Check Stats          |")
	print("--------------------------")
	choice=str(input("Type the number corresponding to what you want to do. "))
	os.system("cls")

	if choice=="2":
		while True:
			for i in range(14):
				print (open(path).readlines()[i])


			print("You are at the @ symbol.")
			print("------------------------")
			print("U = Go Up")
			print("D = Go Down")
			print("L = Go Left")
			print("R = Go Right")
			print("------------------------")
			move=input("Where would you like to move? (Or type exit to stop adventuring) ").lower()
			if move=="u":
				if (open(path).readlines()[row-1])[x]==" ":
					linereplace(14,str(row-1)+"\n")
					roll()
				else:
					text("You cannot go up any farther!")
					sleep(1)
			elif move=="d":
				try:
					if (open(path).readlines()[row+1])[x]==" ":
						linereplace(14,str(row+1)+"\n")
						roll()
					else:
						text("You cannot go down farther!")
						sleep(1)
				except:
					text("You cannot go down farther!")
					sleep(1)
			elif move=="l":
				if (open(path).readlines()[row])[x-2]==" ":
					linereplace(15,str(x-2)+"\n")
					roll()
				else:
					text("You cannot go any more to the left!")
					sleep(1)
			elif move=="r":
				if (open(path).readlines()[row])[x+2]==" ":
					linereplace(15,str(x+2)+"\n")
					roll()
				else:
					text("You cannot go any more to the right!")
					sleep(1)
			elif move=="exit":
				break
				os.system("cls")
			os.system("cls")


		
