inv2 = ("")
from time import sleep
start = input('Before we begin, there is no way to save the game, you may have to go though it again in order to go back to where you curently were. Is this ok?.......type \"Yes\" or \"No\" ').lower()
if start == "yes":
	print ("Great, lets get started!")

	print ("")

else:
	print ("Thats fine, have a good day!")
	sleep(1)
	import sys 
	sys.exit();
	
name = input("What should your charactor's name be? ")

if name == (""):
	name = ("Person that doesn't want to be named for some strange reason...");

print ("")

clas = input("What should your charactor's class be?.........type \"Range\" for a ranger, \"Mage\" for a magician, or \"Mele\" for a fighter. ").lower()

print ("")

print ("*The combat master starts talking* Hello %s! I am the combat master. Welcome to the world known as Rhilon. It's a very nice place, or at least it used to be...You see, it has been corrupted. Here at this castle we think of nature as a giver of peace, and power. But along with good, there is always some evil. In this case, natural disasters. There are 4 worlds or essences in Rhilon, the water essence, air essence, the earth essence, and the fire essence. Together known as the 4 elements. We have someone named Briallen to come help us fix this corruption. He still isn't here yet unfortunatly. Anyway, we need to train you to help defend this castle. I will assign you to a master, and you shall be his apprentice. You can meet him in the practice room. Just go the stairs and take a right." %(name))
sleep (4)
print ("")

print ("*You go up the stairs and find a practice room. After meeting your master, Seren, he teaches you how to fight creatures and then sends you back to the combat master.*")
sleep (.5)
print ("")

print ("*The combat master sees you and starts talking* Oh, you're back! I hope you enjoyed your fighting lesson! Now there is one more thing I should adress; when you accomplish a task, such as killing a monster, you will earn experience points. Depending on the number of experience points you have, you will become stronger and gain some perks. Ok, so now, we need someone to go to the back of the castle an...*Someone shouts from a balcony in the second floor of the castle* Monsters are attacking the castle! We must defend it immediatly! *Another person yells* They broke the gates open! *As large, murderous creatures enter the castle, you go and hide behind some crates. Out of the corner of your eye you can see the combat master fighting the creatures epically.*")
sleep (3)
print ("")

print ("*After the dust seems to settle, yet another person screams* Wait! Seren is gone! The monsters probably took him, went on the roof, and escaped from there. *The combat master responds* We can't follow them now. Our only hope is Briallen to help us fix all of this. But where is he? *Another random person speaks* I got news that he couldn't come to help us because he had some \"important business to attend to\". Whatever that means...")
sleep (2)
print ("")

print ("*The combat master looks at you with a undecided face. He then starts to speak* Well who is going to go on this quest to save Seren? %s, you are the only one that can do this. If you could sucessfully retreive Seren, we would be eternally grateful to you. Seren is one of our leading teachers and we need him." %(name))
sleep (1)
print ("")

decision = input("Will you go on this Journey for your dear master, Seren?.........\"Yes\" or \"No\" ").lower()

if decision == "yes" :
	print ("")
	print ("Hooray, your awesome now.");
else:
	print ("")
	print ("Too bad, your going to do it anyway.");
sleep (1)
print ("")

print ("*Combat master talks to you* I have contact with others that you will meet throughout your journey. They are located in different castles you will find. Always go to those castles. I can send word to them that you will be coming. You will need the help they offer you. For now, you can pack and get ready for your journey. Here are some supplies. *He hands you a backpack with some supplies and weapons in it* You might meet poeople that need help and offer you side-quests. If you complete a quest you will gain experience points and possibly other rewards. Lastly, if you die during your journey, you will get sent back to the infirmary at the last castle you visited. There they will be able to give you an elixir to heal you as best they can. Travel safe! *On your way out of the castle, you hear the combat master whisper to himself: \"I sure hope this works. I'm coming for you Briallen.\"*")
sleep (.5)
print ("")

cont1 = input("Are you ready to start your journey? (Press Enter to continue) ")

if cont1 == "Yes" : 
	print ("");


gold = (500)
inv = ("Your backpack contains: 2 health potions, 4 fish, " + str(gold) + " Gold, ")

inv1 = ("stuff")

if clas == "mage" :
	inv1 = ("Level 5 mage robes, a magic wand, and a magic book.");

elif clas == "range" :
	inv1 = ("Level 5 range armor, a shortbow with inchanted arrows so you never run out of ammo, and a crossbow with inchanted bolts so your never run out of ammo.");

else :
	inv1 = ("A short sword, two daggers, and level 5 mele armor.");

Invintory = (inv + inv1)

print ("")

print ("If you ever want to know what items you have with you at the time, just type \"invintory\" when your prompted to. Try it now!")

print ("")

invintest = input("").lower()

print ("")

if invintest == "invintory":
	print (str(Invintory));

print ("")
sleep (.5)
print ("*You step out onto the fertile soil of the castle lawn. The sun is shining, and though you're nervous about this quest, you feel a since a calm.*")
sleep (.5)
print ("")

print ("*After setting out on the path leading from the castle, the path wanders onto the shoreline of the island you are on. The sand crunches underneath your sandals as waves roll over your feet. You look to your right and notice that there is a black gate stretching all down the coastline. Behind the gate is a forest full of dense, black, dead trees.* You think to yourself: There could be gold in there. Some monsters too. Should I climb the gate and go in, or stay safe on the path?")
sleep (1)
print ("")

choice2 = input("Do you go in the forest, or stay on the path?.......Type \"forest\" or \"path\" ").lower()

print ("")

if choice2 == "forest":
	sleep (.5)
	print ("*Taking the risk, you climb slowly over the black gate and into the forest. Making your way farther in, it gets darker. The darker it gets, the more fatigued you get. Eventually you go and sit down under a tree. Your vision goes black.*")
	print ("")
	sleep (3)
	print ("*You start to see light, and then sit up. Immediatly you recognize that your in the castle infirmiry. The combat master leans over you, his face full of dissapointment. Out of nowhere the combat master starts to yell at you.* %s! You need to get back on the trail! And I better not be seeing you back here again." %(name))
	print ("")
	sleep (.5)
	print ("*You Exit the castle...again, and head down the same path as last time.*")
	print ("");
sleep (.5)
print ("*A little while longer down the path you see a man with ripped clothes on the shoreline that is crying. He looks very poor.* Do you want to talk to him? -  This may lead to a sidequest.")

print ("")

choice3 = input("Talk to the man?.......Type \"yes\" or \"no\" ").lower()

if choice3 == "yes":
	print ("")
	print ("*You walk carefully up to him and start to speak* Excuse me sir?")
	print ("")
	sleep (2)
	print ("Man: Hello? Who is that?")
	print ("")
	sleep (1.5)
	print ("You: My name is %s. Do you need help?" %(name))
	print ("")
	sleep (1.5)
	print ("Man: Oh, hello. I'm Adam. Yes, some help would be great, you see, I used to own a potion shop in the town of drine just up the road from here. Last night, the store was robbed and I lost everything I owned. I hardly survived. The robber came in with a bow and arrow and shot me in the side. *You take a glance at his side and see the wound*")
	print ("")
	sleep (2)
	print ("You: Adam I am so sorry. Is there anything I can do to help?")	
	print ("")
	sleep (1.5)
	print ("Adam: If you got back the money that was robbed from me, I would be overjoyed and thankful for your help forever!")
	print ("")
	sleep (1.5)
	print ("You: I guess I can try. But where do I find him?")
	print ("")
	sleep (1.5)
	print ("Adam: Thank you so much! I heard he lives on an island that way. *He points to the ocean* Save travels %s!" %(name))
	print ("")
	sleep (2)
	if clas == "range":
		print ("*There is a wooden boat on the shore. You hop in and start paddling out to the island with your hands. Eventually you get to the island and are greeted by 5 rats. You take out your bow and magical arrow. You miss a couple of shots since this is the first time you fought anything, but end up killing all the rats.*");
	elif clas == "mage":
		print ("*There is a wooden boat on the shore. You hop in and start paddling out to the island with your hands. Eventually you get to the island and are greeted by 5 rats. You take out your spellbook and wand. Looking through the book you realize it contains spells of the 4 elements. You cast a water spell over the 5 rats and they die of not being able breath.*");
	else:
		print ("*There is a wooden boat on the shore. You hop in and start paddling out to the island with your hands. Eventually you get to the island and are greeted by 5 rats. You pull out your short sword and find it hard to stab them since they keep squirming around. One bites your hand.* Ow! you burst out. *Eventually you stab all the rats.*");
	print ("")
	sleep (.5)
	print ("*You get out of the boat and head twards the house on the island. You kick down the wooden door of the house and walk in* Alright, I know you robbed the potion store last night! Give me the stollen money!, you say with strong force. *A voice echos from deep inside the house* Ha. You think I'll just give you back the money? It's not that easy... *The man walks into the room* Lets fight!, he roars.")
	print ("")
	input("Press Enter when your ready to start the fight.")
	print ("")
	sleep (.5)
	if clas == "range":
		print ("*You grab your crossbow and get into a fighting stance.* I will defeat you!, you yell. I'm not so sure about that!, he responds. *He takes out a two-handed iron sword and charges at you. Your fingers fumbled trying to load the crossbow. You know you couldn't fire it in time and had to dodge out of the way. Before you knew it, he turned and started charging again. This time you fired the crossbow right at his shoulder. It fired and he stumbled to the floor. Blood rushing out of him, you take his sword.*");
	elif clas == "mage" :
		print ("*You grab your wand and book and get into a fighting stance.* I will defeat you!, you yell. I'm not so sure about that!, he responds. *He takes out a two-handed iron sword and charges at you. Fumbling through your spellbook, you realize you won't have time to fire a spell and have to dodge out of the way. Before you know it, he turns around and starts charging again. This time you find a fire spell and shoot it at him. He can't dodge the attack and it ends up hitting him. He lies on the ground and you pick up his sword.*");
	else:
		print ("*You grab your short sword in one hand and a dagger in the other.* I will defeat you!, you yell. I'm not so sure about that!, he responds. *He takes out a two-handed iron sword and charges at you. You barely parry the attack and he pushes you back with his sword. He charges again. This time you dodge the attack, turn around quickly, and stab him in the back with your dagger. He lands on the ground and you pick up his sword*");
	print ("")
	sleep (1)
	print ("Where is the money? Tell me or you die, you ask. It's in the room to the left, under the bed, he confesses. *You go into the room and collect the money. From there you go out of the building, into the boat and back to Adam.*")
	print ("")
	sleep (1)
	print ("Here is your money Adam, you say as your give it to him. I can't tell you how much this means to me, Thank you so much. Here, I'll give you 100 gold for your trouble, and you earn 1000 experience points as well.")
	print ("")
	sleep (.5)
	print ("When you earn experience points and or gold, it gets listed when you look at what is in your invintory. Try it now!")
	print ("")
	invintest2 = input("").lower()
	gold = (600)
	inv = ("Your backpack contains: 2 health potions, 4 fish, An iron two-handed sword, 1000 experience points, " + str(gold) + " Gold, ")
	Invintory = (inv + inv1)
	if invintest2 == "invintory":
		print (str(Invintory));
	print ("")
	sleep (.5)
	print ("*After completing your task and saying goodbye to Adam, you follow the path into the next town, Drine.*")
else:
	print ("")
	sleep (.5)
	print ("You ignore the man and make your way to the next town, Drine.");
sleep (1)
print ("")
print ("(If you look on the map of the island on either side of the game, you can see where the town is relative to the rest of the island) This is the first essence/element that the combat master told you about.")
print ("")
print ("*After a while you can make out the town in the distance. You walk through the gates of the town and see the mass ammount of people trading at different trade stalls. You decide you should look and see if there is anything you want to buy.*")
print ("")
sleep (.5)
print ("*You walk up to a food/drink stand. You take a look at the sign on the stall listing what they are selling.*")
print ("")
sleep (2)
print ("Bread Loaf - Heals 30 - 40 Gold")
sleep (.4)
print ("Fish - Heals 20 - 30 Gold")
sleep (.4)
print ("Bacon - Heals 5 - 10 Gold")
sleep (.4)
print ("Ham Sandwich - Heals 30 - 40 Gold")
sleep (.4)
print ("Doughnut - Heals 20 - 30 Gold")
sleep (.4)
print ("Cake - Heals 50 - 60 Gold")
sleep (.4)
print ("Apple -  Heals 10 - 15 Gold")
sleep (.4)
print ("Water Bottle - Heals 10 - 15 Gold")
sleep (.4)
print ("Tea - Heals 15 - 20 Gold")
sleep (.4)
print ("Coffee - Heals 15 - 20 Gold")
sleep (.4)
print ("")
while (True):
	print ("")
	print ("If you want to buy something, type in the name of the food and or drink......Make sure you spell it exactly how it is listed! If You don\'t want to buy anything, press enter to continue.")
	print ("")
	food = input ("").lower()
	if food == ("bread loaf"):
		gold -= 40
		inv2 += ("A bread loaf, ")
		print ("")
		print ("*You buy a loaf of bread*");
	elif food == ("fish"):
		gold -= 30
		inv2 += ("A fish, ")
		print ("")
		print ("*You buy a fish*");
	elif food == ("bacon"):
		gold -= 10
		inv2 += ("A piece of bacon, ")
		print ("")
		print ("*You buy a piece of bacon....thats what I would by too*");
	elif food == ("ham sandwich"):
		gold -= 40
		inv2 += ("A ham sandwich, ")
		print ("")
		print ("*You buy a sandwich*");
	elif food == ("doughnut"):
		gold -= 30
		inv2 += ("A doughnut, ")
		print ("")
		print ("*You buy a doughnut*")
	elif food == ("cake"):
		gold -= 60
		inv2 += ("A cake, ")
		print ("")
		print ("*You buy a cake*");
	elif food == ("apple"):
		gold -= 15
		inv2 += ("An apple, ")
		print ("")
		print ("*You buy an apple*");
	elif food == ("water bottle"):
		gold -= 15
		inv2 += ("A water bottle, ")
		print ("")
		print ("*You buy a watter bottle*");
	elif  food == ("tea"):
		gold -= 20
		inv2 += ("A cup of tea, ")
		print ("")
		print ("*You buy a cup of tea*");
	elif food == ("coffee"):
		gold -= 20
		inv2 += ("A cup of coffee, ")
		print ("")
		print ("*You buy a cup of coffee*");
	else:
		print ("*You don't buy anything*")
		break;
	print ("")
	if gold < 200:
		print ("")
		print ("Hey! Stop buying food, you don't have much gold left!")
		print ("")
		break;
	ask = input ("Do you want to buy anything else?...type Yes or No. ").lower()
	if  ask == ("yes"):
		continue;
	else:
		break;	

print ("*You leave the food stand*");
print ("")
print ("When you spend money and buy things, it shows up in your invintory. You can look at your invintory now or press enter to continue.")
print ("")
if choice3 == ("yes"):
	inv = ("Your backpack contains: 2 health potions, 4 fish, An iron two-handed sword, " + str(gold) + " Gold, ");
else:
	inv = ("Your backpack contains: 2 health potions, 4 fish, " + str(gold) + " Gold, ");
Invintory = (inv + inv2 + inv1)
invintest4 = input("").lower()
if invintest4 == ("invintory"):
	print (str(Invintory));
sleep (1)
print ("")
print ("When you are ever hurt from a fight, or just hungry (which you will be after a while), you can eat some food to make you better.")
sleep (1)
print ("")
print ("*You move onto the next trading stall. They are selling potions.*")
sleep (.5)
print ("")
print ("*You look at the sign to see what potions are for sale*")
sleep (2)
print ("")
print ("Health potion - Heals to full health - 90 gold")
sleep (.4)
print ("Strength potion - Makes you stronger in battle - 40 gold")
sleep (.4)
print ("Potion of defence - Makes you harder to hit in battle - 40 gold")
sleep (.4)
print ("Poison potion - Poisons whoever drinks it - 30 gold")
sleep (1)
print ("")
while (True):
	potion = input("Would you like to buy a potion? If so, type in the name of the potion you want...Make sure you spell it exactly as listed! If you don't want anything, press enter to continue. ").lower()
	if gold < 150:
		print ("")
		print ("Hey! Stop buying stuff, you don't have much gold left!")
		break;
	if potion == ("health potion"):
		gold -= 90
		inv2 += ("A health potion, ")
		print ("")
		print ("*You buy the potion*");
	elif potion == ("strength potion"):
		gold -= 40
		inv2 += ("A strength potion, ")
		print ("")
		print ("*You buy the potion*");
	elif potion == ("potion of defence"):
		gold -= 40
		inv2 += ("A defence potion, ")
		print ("")
		print ("*You buy the potion*");
	elif potion == ("poison potion"):
		gold -= 30
		inv2 += ("A poison potion, ")
		print ("")
		print ("*You buy the potion*");
	else:
		print ("Don't want anything? Thats fine.")
		break;
	print ("")
	ask1 = input ("Do you want to buy anything else?...Type \"Yes\" or \"No\" ").lower()
	if ask1 == ("yes"):
		continue;
	else:
		break;
print ("")
Invintory = (inv + inv2 + inv1)
inv = ("Your backpack contains: 2 health potions, 4 fish, " + str(gold) + " Gold, ")
print ("")
sleep (.5)
print ("")
invintest5 = input("Feel free to look at your invintory now, or press Enter to continue. ").lower()
if invintest5 == ("invintory"):
	print (str(Invintory))
	print ("");
else:
	print ("");
sleep (.4)
print ("*Next, you walk to a armor stand* When your in battle, you have 100 hitpoints. When you have armor, you get hurt less when you get attacked. For instance, if you had level 20 armor, and whatever you are fighting has an attack strength of 30, you would take the difference of the two, and that is how many hitpoints you would lose every time you were attacked.")
sleep (5)
print ("")
print ("*You take a look at what is being sold*")
sleep (2)
print ("")
if clas == ("range"):
	print ("Level 10 range armor - 100 gold")
	sleep (.4)
	print ("Level 20 range armor - 250 gold")
	sleep (.4)
	print ("Level 30 range armor - 500 gold");
elif clas == ("mage"):
	print ("Level 10 mage robes - 100 gold")
	sleep (.4)
	print ("Level 20 mage robes - 250 gold")
	sleep (.4)
	print ("Level 30 range armor - 500 gold");
else:
	print ("Level 10 mele armor - 100 gold")
	sleep (.4)
	print ("Level 20 mele armor - 250 gold")
	sleep (.4)
	print ("Level 30 mele armor - 500 gold");
sleep (.4)
print ("")



print ("")
input("Part one of World Essence is over. Press Enter to exit the game.")

