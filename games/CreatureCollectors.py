"""
Item Rarity:

	Common - 50% chance
	Uncommon - 30% chance
	Rare - 12% chance
	Super Rare - 5% chance
	Elemental - 2% chance
	Godly - 1% chance
-----------------------
Levels:

	Common (40-50        Attack+Health+Defense)
	Uncommon (50-70      Attack+Health+Defense)
	Rare (70-100         Attack+Health+Defense)
	Super Rare (100-150  Attack+Health+Defense)
	Elemental (150-200   Attack+Health+Defense)
	Godly (200-400       Attack+Health+Defense)
-----------------------
WEAPONS (Used To Power Up Creature's Attack) (Ammo Not Needed To Use)

	Beginner - Bow 05, Magic Book 05, Beginner Sword

Common:
	Wooden - Bow 10, Staff 10, Book 10, Wooden Sword
	Stone - Bow 20, Staff 20, Book 20, Stone Sword, Stone Dagger x2
	Copper - Bow 30, Staff 30, Book 30, Copper Sword, Copper Dagger x2

Uncommon:
	Bronze - Bow 40, Crossbow 40, Staff 40, Book 40, Bronze Sword, Bronze Dagger x2
	Iron - Bow 50, Crossbow 50, Staff 50, Book 50, Iron Sword, Iron Dagger x2
	Steel - Bow 60, Crossbow 60, Staff 60, Book 60, Steel Sword, Steel Dagger x2

Rare:
	Gold - Bow 70, Crossbow 70, Staff 70, Book 70, Gold Sword, Gold Dagger x2
	Platinum - Bow 80, Crossbow 80, Staff 80, Book 80, Platinum Sword, Platinum Dagger x2

Super Rare:
	Diamond - Bow 90, Crossbow 90, Staff 90, Book 90, Diamond Sword, Diamond Dagger x2
	Titanium - Bow 100, Crossbow 100, Staff 100, Book 100, Titanium Sword, Titanium Dagger x2

Elemental:
	Fire - Fire Bow, Fire Sword
	Water - Water Bow, Water Sword
	Air - Air Bow, Air Sword
	Earth - Earth Bow, Earth Sword
	Elemental Book

Godly:
	God Sword, God Book, God Bow
-----------------------
print FILE LINES:
0: Player Defense
1: Player Hitpoints
2: Player Attack
3: Creature Name
4: Creature Attack
5: Creature Defense
6: Creature Hitpoints
7: Helm Name
8: Helm Defense
9: Platebody Name
10: Platebody Defense
11: Platelegs Name
12: Platelegs Defense
13: Weapon Name
14: Weapon Attack
15: Level
16: Total xp
17: Name Of Your Weapon/Your Class
18: Gold
19: GODLY+Elemental Rolls Unlocked
20:daily log in bonus
"""

#IMPORTS

from time import sleep
from random import randint
import time
import random
import os
import datetime
import turtle as t
import sys



#FUNCTIONS
##################################################################################################################################################################
def Roll():
	global gold
	global gift
	global price
	print ("----------------------------------")
	print ("1: Roll For A Creature - 200 Gold")
	print ("2: Roll For Armor - 150 Gold")
	print ("3: Roll For A Weapon - 150 Gold")
	print ("4: Roll For Any - 300 Gold")
	print ("5: Back to Home Menu")
	print ("----------------------------------")
	rolltype = input("Pick the number you want. ")
	print ("")
	if rolltype==("5"):
		return;
	else:
		if rolltype == ("1"):
			price=(200)
			gift = ("creature")
		elif rolltype == ("2"):
			price=(150)
			armortype = randint(1,3)
			if armortype == (1):
				gift = ("helm")
			elif armortype == (2):
				gift = ("platebody")
			elif armortype == (3):
				gift = ("platelegs")
		elif rolltype == ("3"):
			price=(150)
			gift = (weaponame)
		elif rolltype == ("4"):
			price=(300)
			material = randint(1,5)
			if material == (1):
				gift = ("creature")
			elif material == (2):
				gift = ("helm")
			elif material == (3):
				gift = ("platebody")
			elif material == (4):
				gift = ("platelegs")
			elif material == (5):
				gift = (weaponame)
		if gold < price:
			text ("You don't have enough money to roll for that!")
			return
		gold -= price
		goldreplace(gold,18)
		if Unlocked == ("unlocked"):
			roll = randint(1,100)
		else:
			roll = randint(1,97)
		if roll in range(0, 51):
			attack = randint(40,50)
			defense = randint(20,30)
			health = randint(80,100)
			text ("Congradulations! You got a common %s!" %gift)
		elif roll in range(50, 81):
			attack = randint(50,70)
			defense = randint(30,40)
			health = randint(100,140)
			text ("Congradulations! You got an uncommon %s!" %gift)
		elif roll in range(80, 93):
			attack = randint(70,100)
			defense = randint(40,50)
			health = randint(140,200)
			text ("Congradulations! You got a rare %s!" %gift)
		elif roll in range(92, 98):
			attack = randint(100,150)
			defense = randint(50,70)
			health = randint(200,300)
			text ("Congradulations! You got a super rare %s!" %gift)
		elif roll in range(97, 100):
			attack = randint(150,200)
			defense = randint(70,100)
			health = randint(300,400)
			text ("Congradulations! You got an elemental %s!" %gift)
		elif roll == (100):
			attack = randint(200,400)
			defense = randint(100,200)
			health = randint(400,800)
			text ("Congradulations! You got a GODLY %s!" %gift)
		if gift == ("creature"):
			text ("[Attack: %s]" %str(attack))
			text ("[Defense: %s]" %str(defense))
			text ("[Health: %s]" %str(health))
		if gift == ("helm"):
			attack = ("")
			health = ("")
			text ("[Defense Boost: %s]" %str(defense))
		if gift == ("platelegs"):
			attack = ("")
			health = ("")
			text ("[Defense Boost: %s]" %str(defense))
		if gift == ("platebody"):
			attack = ("")
			health = ("")
			text ("[Defense Boost: %s]" %str(defense))
		if gift == (weaponame):
			health = ("")
			defense = ("")
			text ("[Attack Boost: %s]" %str(attack))
	f = open(path, "a")
	f.write(gift+"\n")
	f.write(str(attack)+"\n")
	f.write(str(defense)+"\n")
	f.write(str(health)+"\n")
	f.close()
	print ("")
	again = input("Do you want to roll again? ").lower()
	os.system("cls")
	if again == ("yes"):
		Roll()
##################################################################################################################################################################
def battle():
	t.Turtle._screen = None
	t.TurtleScreen._RUNNING = True

	global gold
	global xp
	text ("BATTLE FOUND!")
	opponent_attack = randint(Level*20,Level*30)
	opponent_defence = randint(Level*20,Level*20)
	opponent_hitpoints = randint(Level*100,Level*150)
	player_defence = int(open(path).readlines()[0])
	player_hitpoints = int(open(path).readlines()[1])
	player_attack = int(open(path).readlines()[2])-(randint(1,Level*2))

	t.speed("fastest")
	t.penup()
	t.turtlesize(2,2,2)
	t.setheading(0)
	t.goto(-250,300)
	t.pendown()
	t.begin_fill()
	t.fd(int(player_hitpoints))
	t.right(90)
	t.fd(50)
	t.right(90)
	t.fd(int(player_hitpoints))
	t.right(90)
	t.fd(50)
	t.end_fill()
	t.penup()
	t.goto(100,300)
	t.pendown()
	t.begin_fill()
	t.setheading(0)
	t.fd(opponent_hitpoints)
	t.right(90)
	t.fd(50)
	t.right(90)
	t.fd(opponent_hitpoints)
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
		opponent_attack = randint(Level*20,Level*30)
		damage = player_attack-(opponent_defence/4000)
		opponent_hitpoints -= (damage)


		player(0,0)
		remove(100,opponent_hitpoints)


		if opponent_hitpoints < (1):
			t.bye()
			os.system("cls")
			text ("Congrats! You survived the battle.")
			sleep (.5)
			print ("")
			player_hitpoints = open(path).readlines()[1]
			text ("You get " + str(opponent_attack/2) + " gold, and " + str(battlexp) + " Experience Points!")
			xp += battlexp
			gold += opponent_attack/2
			goldreplace(gold,18)
			input("")
			print ("")
			break;




		damage = opponent_attack-(player_defence/4000)
		player_hitpoints -= (damage)


		opponent(0,0)
		remove(-250,player_hitpoints)

		if player_hitpoints < 1:
			t.bye()
			os.system("cls")
			text ("Oh dear, you are dead.")
			sleep (.5)
			print ("")
			player_hitpoints = open(path).readlines()[1]
			if gold < 10:
				text ("You have lost all your gold.")
				print ("")
				gold = (0)
				goldreplace(gold, 18)
				input("")
				break;
			else:
				text ("You have lost 10 percent of your gold.")
				print ("")
				gold -= .1*gold
				goldreplace(gold, 18)
				input("")
				break;
		player_turn=(True)
		continue
	os.system("cls")
	return;
##################################################################################################################################################################
def Invintory():
	print ("-------------------------------")
	print ("1: Look At Your Invintory")
	print ("2: Equip Items")
	print ("3: Look At Your Stats")
	print ("4: Back to Home Menu")
	print ("-------------------------------")
	choice = input("What would you like to do? ")
	os.system("cls")
	if choice == ("1"):
		text ("The items in your invintory are:")
		Items()
	elif choice == ("2"):
		text ("Your currently equipped items are:")
		print ("\n")
		text ("["+creatureslot+"]")
		text (creatureattack+" attack, "+creaturedefense+" defense, and "+creaturehitpoints+" hitpoints.")
		print ("")
		text ("["+helmslot+"]")
		text (helmdefense+" defense.")
		print ("")
		text ("["+platebodyslot+"]")
		text (platebodydefense+" defense.")
		print ("")
		text ("["+platelegsslot+"]")
		text (platelegsdefense+" defense.")
		print ("")
		text ("["+weaponslot+"]")
		text (weaponattack+" attack.")
		print ("\n")
		print ("The items in your invintory are:")
		Items()
		itemnumber=input ("Type the number of the item you want to equip. ")
		if "creature" in open(path).readlines()[20+((int(itemnumber)-1)*4)].splitlines()[0]:
			player_hitpoints=open(path).readlines()[23+((int(itemnumber)-1)*4)].splitlines()[0]
			player_attack=open(path).readlines()[21+((int(itemnumber)-1)*4)].splitlines()[0]+weaponattack
			player_defence=open(path).readlines()[22+((int(itemnumber)-1)*4)].splitlines()[0]+helmdefense+platelegsdefense+platebodydefense
		elif "sword" or "staff" or "bow" in open(path).readlines()[20+((int(itemnumber)-1)*4)].splitlines()[0]:
			player_attack=open(path).readlines()[21+((int(itemnumber)-1)*4)].splitlines()[0]+creatureattack
		elif "platelegs" in open(path).readlines()[20+((int(itemnumber)-1)*4)].splitlines()[0]:
			player_defence=open(path).readlines()[22+((int(itemnumber)-1)*4)].splitlines()[0]+platebodydefense+helmdefense+creaturedefense
		elif "platebody" in open(path).readlines()[20+((int(itemnumber)-1)*4)].splitlines()[0]:
			player_defence=open(path).readlines()[22+((int(itemnumber)-1)*4)].splitlines()[0]+platelegsdefense+helmdefense+creaturedefense
		elif "helm" in open(path).readlines()[20+((int(itemnumber)-1)*4)].splitlines()[0]:
			player_defence=open(path).readlines()[22+((int(itemnumber)-1)*4)].splitlines()[0]+platelegsdefense+platebodydefense+creaturedefense

		goldreplace(player_defence,)
		goldreplace(player_hitpoints)
		goldreplace(player_attack)
		goldreplace()

	elif choice == ("3"):
		if weaponame==("bow"):
			clas=("Ranger")
		elif weaponame==("staff"):
			clas=("Mage")
		elif weaponame==("sword"):
			clas=("Knight")
		text("%s\'s information:" %userguess)
		text("[Class: %s]" %clas)
		text("[Level: %s]" %Level)
		text("[Total Experience: %s]" %xp)
		text("[Gold: %s]" %gold)
		text("[Attack: %s]" %int(open(path).readlines()[2]))
		text("[Defense: %s]" %int(open(path).readlines()[0]))
		text("[Hitpoints: %s]" %int(open(path).readlines()[1]))
	elif choice==("4"):
		return;




	input("")
	os.system("cls")
##################################################################################################################################################################
def goldreplace(var, linenumber):
	global gold
	if isinstance(var, str)==True:
		None
	else:
		var=round(var)
	f=open("C:\\Users\\Noah Stremmel\\Documents\\Accounts\\"+userguess+".txt", "r")
	f1=open("C:\\Users\\Noah Stremmel\\Documents\\Accounts\\host.txt", "w")
	counter=(0)
	for line in f:
		if counter == int(linenumber):
			f1.write(str(var)+"\n");
		else:
			f1.write(line);
		counter+=(1)
	f.close()
	os.system("del \"C:\\Users\\Noah Stremmel\\Documents\\Accounts\\"+userguess+".txt\"")
	f2=open("C:\\Users\\Noah Stremmel\\Documents\\Accounts\\"+userguess+".txt", "w")
	f1=open("C:\\Users\\Noah Stremmel\\Documents\\Accounts\\host.txt", "r")
	for line in f1:
		f2.write(line);
	f1.close()
	os.system("del \"C:\\Users\\Noah Stremmel\\Documents\\Accounts\\host.txt\"")
##################################################################################################################################################################
def Shop():
	global gold
	print ("----------------------")
	print ("1. Buy Something")
	print ("2. Sell Something")
	print ("3. Upgrade Something")
	print ("4. Back To Home Menu")
	print ("----------------------")
	choice=input("")
	os.system("cls")
	if choice==("1"):
		text ("1: Unlock the ability to get Elemental and GODLY Rolls - 750 Gold")
		text ("2: ???????????????????????????????")
		print ("")
		choice1=input("")
		os.system("")
		if choice1==("1"):
			if gold<750:
				text ("You Don't have enough gold to do that!")
				print ("")
				Shop()
			gold-=750
			goldreplace(gold,18)
			Unlocked="unlocked"
			goldreplace(Unlocked,19)
	elif choice==("2"):
		Items()
		print ("")
		item=input('Type the number of the item you want to sell. ')
		price=open(path).readlines()[(23)+((int(item)-1)*4)].splitlines()[0]
		if str(price)==(""):
			price=open(path).readlines()[(22)+((int(item)-1)*4)].splitlines()[0]
		sell=input("Do you want to sell this item for %s gold pieces?  (Type \"Yes\" or \"No\") " %str(int(price)*2)).lower()
		if sell==("yes"):
			gold+=int(price*2)
			goldreplace(gold,18)
			f=open("C:\\Users\\Noah Stremmel\\Documents\\Accounts\\"+userguess+".txt", "r")
			f1=open("C:\\Users\\Noah Stremmel\\Documents\\Accounts\\host.txt", "w")
			counter=(-1)
			for line in f:
				counter+=1
				if counter == (21)+((int(item)-1)*4):
					continue
				if counter == (22)+((int(item)-1)*4):
					continue
				if counter == (23)+((int(item)-1)*4):
					continue
				if counter == (24)+((int(item)-1)*4):
					continue
				f1.write(line);
			f.close()
			os.system("del \"C:\\Users\\Noah Stremmel\\Documents\\Accounts\\"+userguess+".txt\"")
			f2=open("C:\\Users\\Noah Stremmel\\Documents\\Accounts\\"+userguess+".txt", "w")
			f1=open("C:\\Users\\Noah Stremmel\\Documents\\Accounts\\host.txt", "r")
			for line in f1:
				f2.write(line);
			f1.close()
			os.system("del \"C:\\Users\\Noah Stremmel\\Documents\\Accounts\\host.txt\"")
			os.system("cls")
			Shop()
	elif choice==("3"):
		None

	os.system("cls")
##################################################################################################################################################################
def text(x):
	for i in x:
		sys.stdout.write(i)
		sys.stdout.flush()
		sleep(.005)
	print ("")
##################################################################################################################################################################
def Items():
	counter = (21)
	counter1 = (1)
	while (True):
		try:
			name = open(path).readlines()[counter].splitlines()[0]
			attack = open(path).readlines()[counter+1].splitlines()[0]
			defense = open(path).readlines()[counter+2].splitlines()[0]
			hitpoints = open(path).readlines()[counter+3].splitlines()[0]
			if attack == (""):
				text (str(counter1) + ": " + name + " with %s defense." %defense)
			elif defense == (""):
				text (str(counter1) + ": " + name + " with %s attack." %attack)
			else:
				text (str(counter1) + ": " + name + " with " + attack + " attack, " + defense + " defense, and " + hitpoints + " hitpoints.")
			sleep (.4)
			counter+=(4)
			counter1+=(1)
			continue
		except IndexError:
			break;
##################################################################################################################################################################





while True:
	text("Type in two digits. The first will be the color of the background,")
	text("and the second will be the color of the text.")
	print ("")
	print ("			0 = Black	    8 = Gray")
	print ("			1 = Blue        9 = Light Blue")
	print ("			2 = Green       A = Light Green")
	print ("			3 = Aqua        B = Light Aqua")
	print ("			4 = Red         C = Light Red")
	print ("			5 = Purple      D = Light Purple")
	print ("			6 = Yellow      E = Light Yellow")
	print ("			7 = White       F = Bright White")
	print ("")
	os.system("color " + str(input("")))
	os.system("cls")

	change=input("Do you want a different color scheme? ").lower()
	os.system("cls")
	if change=="no":
		break;

#EXECUTION
incorrect = (True)
member = input("Do you already have an account? ").lower()
print ("")
if member == ("no"):
	username = input("What do you want your username to be? ")
	password = input("What do you want your password to be? ")
	os.system("cls")
	print ("")
	clas = input("Do you want your creature to use Magic, Range, or Mele in combat?...Type \"Magic\", \"Range\", or \"Mele\". ").lower()
	if clas == ("magic"):
		weaponame = ("staff")
	elif clas == ("range"):
		weaponame = ("bow")
	else:
		weaponame = ("sword")
	f = open("C:\\Users\\Noah Stremmel\\Documents\\Users.txt", "a")
	f.write(username+password+"\n")
	f.close()
	#WRITING STARTER INFORMATION INTO print FILE
	f1 = open("C:\\Users\\Noah Stremmel\\Documents\\Accounts\\" + username + ".txt", "w")
	f1.write("50\n")
	f1.write("60\n")
	f1.write("60\n")
	f1.write("Begginer creature\n")
	f1.write("30\n")
	f1.write("20\n")
	f1.write("60\n")
	f1.write("Begginer helm\n")
	f1.write("10\n")
	f1.write("Begginer platebody\n")
	f1.write("10\n")
	f1.write("Begginer platelegs\n")
	f1.write("10\n")
	f1.write("Begginner " + weaponame + "\n")
	f1.write("30\n")
	f1.write("1\n")
	f1.write("0\n")
	f1.write(weaponame+"\n")
	f1.write("0\n")
	f1.write("locked\n")
	f1.write(str(datetime.datetime.today().weekday()-1)+"\n")
	f1.write("Bigginer creature\n")
	f1.write("30\n")
	f1.write("20\n")
	f1.write("60\n")
	f1.write("Begginer helm\n")
	f1.write("\n")
	f1.write("10\n")
	f1.write("\n")
	f1.write("Begginer platebody\n")
	f1.write("\n")
	f1.write("10\n")
	f1.write("\n")
	f1.write("Begginer platelegs\n")
	f1.write("\n")
	f1.write("10\n")
	f1.write("\n")
	f1.write("Begginner " + weaponame + "\n")
	f1.write("30\n")
	f1.write("\n")
	f1.write("\n")
	f1.close()
	print ("")
	text ("Your account is all set up!")
	text ("[You have been given a starter creature, starter armor, and a starter %s]" %weaponame)
	print ("")
while incorrect == True:
	counter = (0)
	userguess = input("Username: ")
	if userguess == ("stop"):
		break;
	passguess = input("Password: ")
	print ("")
	while (True):
		try:
			if userguess+passguess+"\n" == open("C:\\Users\\Noah Stremmel\\Documents\\Users.txt").readlines()[counter]:
				incorrect = (False)
				break;
			counter+=(1)
			continue
		except IndexError:
			text ("[Your Username or Password is incorrect.]")
			print ("")
			break;
os.system("cls")
text ("Welcome to your account, %s!" %(userguess))
path=("C:\\Users\\Noah Stremmel\\Documents\\Accounts\\" + userguess + ".txt")
#GATHERING PREVIOUS INFORMATION FROM FILE
creatureslot = open(path).readlines()[3].splitlines()[0]
creatureattack = open(path).readlines()[4].splitlines()[0]
creaturedefense = open(path).readlines()[5].splitlines()[0]
creaturehitpoints = open(path).readlines()[6].splitlines()[0]
helmslot = open(path).readlines()[7].splitlines()[0]
helmdefense = open(path).readlines()[8].splitlines()[0]
platebodyslot = open(path).readlines()[9].splitlines()[0]
platebodydefense = open(path).readlines()[10].splitlines()[0]
platelegsslot = open(path).readlines()[11].splitlines()[0]
platelegsdefense = open(path).readlines()[12].splitlines()[0]
weaponslot = open(path).readlines()[13].splitlines()[0]
weaponattack = open(path).readlines()[14].splitlines()[0]
Level = int(open(path).readlines()[15].splitlines()[0])
xp = int(open(path).readlines()[16].splitlines()[0])
weaponame = open(path).readlines()[17].splitlines()[0]
gold = int(open(path).readlines()[18].splitlines()[0])
Unlocked = open(path).readlines()[19].splitlines()[0]
check = open(path).readlines()[20].splitlines()[0]
battlexp = Level*1000
while (True):
	check = open(path).readlines()[20].splitlines()[0]
	if str(datetime.datetime.today().weekday())==(check):
		lock=True
	else:
		lock=False
	print ("")
	print ("                          [Type the number corresponding to what you want to do]")
	print ("                                   ----------------------------------")          
	print ("                                   |1: Manage Your Invintory/Stats  |")
	print ("                                   |2: Roll For An Item/Creature    |")
	print ("                                   |3: Go Find A Battle             |")
	print ("                                   |4: Go to the Shop               |")
	print ("                                   |5: Log Out                      |")
	if lock==False:
		print ("                                   |6: Collect Daily Gold           |")
	print ("                                   ----------------------------------")
	print ("")
	choice = input("                                                   ")
	print ("")
	os.system("cls")
	if choice == ("1"):
		Invintory()
	elif choice == ("2"):
		Roll()
	elif choice == ("3"):
		battle()
	elif choice == ("4"):
		Shop()
	elif choice == ("5"):
		break;
	elif choice == ("6"):
		lock=True
		goldreplace(datetime.datetime.today().weekday(), 20)
		gold+=350
		text ("You have been given 350 gold!")
		goldreplace(gold, 18)


#CHECKS

#if xp > Level*500*(Level+1):
	#level up!







input("Press ENTER to exit the game.")
