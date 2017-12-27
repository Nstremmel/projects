import discord
import asyncio
import random
from time import sleep
import os

path=("C:\\Users\\Noah Stremmel\\Documents\\gold.txt")
client = discord.Client()
gold=int(open(path).readlines()[0].splitlines()[0])
aditya=int(open(path).readlines()[1].splitlines()[0])
nate=int(open(path).readlines()[2].splitlines()[0])
noah=int(open(path).readlines()[3].splitlines()[0])
ryan=int(open(path).readlines()[4].splitlines()[0])
luke=int(open(path).readlines()[5].splitlines()[0])
here=(open(path).readlines()[6].splitlines()[0])
people=('Dungeon Master','Aditya','Nate','Noah','Ryan','Luke')
turn=0
xp=(0,0,0,0,0)
levels=(0,0,0,0,0)
xp[0]=int(open(path).readlines()[7].splitlines()[0])
xp[1]=int(open(path).readlines()[8].splitlines()[0])
xp[2]=int(open(path).readlines()[9].splitlines()[0])
xp[3]=int(open(path).readlines()[10].splitlines()[0])
xp[4]=int(open(path).readlines()[11].splitlines()[0])
levels[0]=int(open(path).readlines()[12].splitlines()[0])
levels[1]=int(open(path).readlines()[13].splitlines()[0])
levels[2]=int(open(path).readlines()[14].splitlines()[0])
levels[3]=int(open(path).readlines()[15].splitlines()[0])
levels[4]=int(open(path).readlines()[16].splitlines()[0])
neededxp=(300,900,2700,6500,14000)

def goldreplace(var, linenumber):
	global gold
	if isinstance(var, str)==True:
		None
	else:
		var=round(var)
	f=open("C:\\Users\\Noah Stremmel\\Documents\\gold.txt", "r")
	f1=open("C:\\Users\\Noah Stremmel\\Documents\\Accounts\\host.txt", "w")
	counter=(0)
	for line in f:
		if counter == int(linenumber):
			f1.write(str(var)+"\n");
		else:
			f1.write(line);
		counter+=(1)
	f.close()
	os.system("del \"C:\\Users\\Noah Stremmel\\Documents\\gold.txt\"")
	f2=open("C:\\Users\\Noah Stremmel\\Documents\\gold.txt", "w")
	f1=open("C:\\Users\\Noah Stremmel\\Documents\\Accounts\\host.txt", "r")
	for line in f1:
		f2.write(line);
	f1.close()
	os.system("del \"C:\\Users\\Noah Stremmel\\Documents\\Accounts\\host.txt\"")


@client.event
async def on_ready():
	print("Bot Logged In!");

@client.event
async def on_message(message):
	global gold, aditya, nate, noah, ryan, luke, here, turn
	if message.author==client.user:
		return
	#############################################################################	
	if message.content.startswith('cringe'):
		await client.send_message(message.channel, ":nerd: :nerd: :nerd: ")
	#############################################################################	
	elif message.content.startswith('!ranks'):
		await client.send_message(message.channel, "Aditya: "+str(aditya))
		await client.send_message(message.channel, "Nate: "+str(nate))
		await client.send_message(message.channel, "Noah: "+str(noah))
		await client.send_message(message.channel, "Ryan: "+str(ryan))
		await client.send_message(message.channel, "Luke: "+str(luke))
	#############################################################################	
	elif message.content.startswith('!addpoint'):
		if (message.content[12:])=='aditya':
			aditya+=int(message.content[9:12])
			goldreplace(aditya, 1)
		elif (message.content[12:])=='nate':
			nate+=int(message.content[9:12])
			goldreplace(nate, 2)
		elif (message.content[12:])=='noah':
			noah+=int(message.content[9:12])
			goldreplace(noah, 3)
		elif (message.content[12:])=='ryan':
			ryan+=int(message.content[9:12])
			goldreplace(ryan, 4)
		elif (message.content[12:])=='luke':
			luke+=int(message.content[9:12])
			goldreplace(luke, 5)
		await client.send_message(message.channel, str(message.content[12:]).title()+" has gained "+str(message.content[9:12])+" points. Good Job!")
	#############################################################################	
	elif message.content.startswith('!takepoint'):
		if (message.content[13:])=='aditya':
			aditya-=int(message.content[10:13])
			goldreplace(aditya, 1)
		elif (message.content[13:])=='nate':
			nate-=int(message.content[10:13])
			goldreplace(nate, 2)
		elif (message.content[13:])=='noah':
			noah-=int(message.content[10:13])
			goldreplace(noah, 3)
		elif (message.content[13:])=='ryan':
			ryan-=int(message.content[10:13])
			goldreplace(ryan, 4)
		elif (message.content[13:])=='luke':
			luke-=int(message.content[10:13])
			goldreplace(luke, 5)
	#############################################################################
	elif message.content.startswith('!+'):
		gold+=(int(message.content[2:]))
		await client.send_message(message.channel, "Your gold has been updated!")
		goldreplace(gold, 0)
	#############################################################################	
	elif message.content.startswith('!-'):
		gold-=(int(message.content[2:]))
		await client.send_message(message.channel, "Your gold has been updated!")
		goldreplace(gold, 0)
	#############################################################################	
	elif message.content.startswith('!gold'):
		await client.send_message(message.channel, "Your team has "+str(gold)+" gold.");
	#############################################################################	
	elif message.content.startswith('!godsnotreal'):
		await client.send_message(message.channel, "Yay atheism!!!");
	#############################################################################	
	elif message.content.startswith('!ty'):
		await client.send_message(message.channel, "@everyone, please thank Elijah, Luke, and Nate for creating such a wonderful story for us.");		
	#############################################################################	
	elif message.content.startswith('!discord'):
		await client.send_message(message.channel, "Wow, isn\'t this discord server awesome? :wink: ")
	#############################################################################
	elif message.content.startswith('!here'):
		here+=(message.content[6:].title())+', '
		goldreplace(here, 6)
		await client.send_message(message.channel, message.content[6:].title()+' is here!')
	#############################################################################
	elif message.content.startswith('!attendance'):
		await client.send_message(message.channel, "The following people attendend this week's session:")
		await client.send_message(message.channel, str(here))
	#############################################################################
	elif message.content.startswith('!dunno'):
		await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/296428228170481664/359121654695067648/best.png");
	#############################################################################
	elif message.content.startswith('!d'):
		if message.content=='!d20':
			None
		else:
			await client.send_message(message.channel, "You rolled a "+str(random.randint(1,int(message.content[2:])))+"!")
	#############################################################################
	elif message.content.startswith('!lit'):
		await client.change_nickname('295645595069054978', 'lit my fam')
	#############################################################################
	elif message.content.startswith('!turn'):
		await client.send_message(message.channel, str(people[turn]))
	#############################################################################
	elif message.content.startswith('!passturn'):
		if turn==5:
			turn=0
		else:
			turn+=1
		await client.send_message(message.channel, 'Turn has been passed to: '+str(people[turn]))
	#############################################################################
	elif message.content.startswith('!commandsplz'):
		await client.send_message(message.author, 'Commands:')
		await client.send_message(message.author, '!ty\n!discord\n!godsnotreal\ncringe\n!dunno\n!spells\n!turn\n!passturn\n!d(number)\n!commandsplz\n!here\n!attendance\n!ranks\n!gold\n')
	#############################################################################
	elif message.content.startswith('!spells'):
		await client.send_message(message.channel, 'https://roll20.net/compendium/dnd5e/Rules:Spells%20by%20Level#content')
	#############################################################################
	elif message.content.startswith('!levels'):
		for i, value in enumerate(xp):
			if levels[i]==0:
				if xp[i]>=neededxp[0]:
					levels[i]+=1
			elif levels[i]==1:
				if xp[i]>=neededxp[1]:
					levels[i]+=1
			elif levels[i]==2:
				if xp[i]>=neededxp[2]:
					levels[i]+=1
		goldreplace(levels[0],12)
		goldreplace(levels[1],13)
		goldreplace(levels[2],14)
		goldreplace(levels[3],15)
		goldreplace(levels[4],16)
		await client.send_message(message.channel, 'Aditya: Level '+str(levels[0])+' with '+str(xp[0])+'XP')
		await client.send_message(message.channel, 'Nate: Level '+str(levels[1])+' with '+str(xp[1])+'XP')
		await client.send_message(message.channel, 'Noah: Level '+str(levels[2])+' with '+str(xp[2])+'XP')
		await client.send_message(message.channel, 'Ryan: Level '+str(levels[3])+' with '+str(xp[3])+'XP')
		await client.send_message(message.channel, 'Luke: Level '+str(levels[4])+' with '+str(xp[4])+'XP')
	##############################################################################
	elif message.content.startswith('!xp'):
		if (message.content[7:])=='aditya':
			xp[0]+=int(message.content[3:6])
			goldreplace(xp[0], 7)
		elif (message.content[7:])=='nate':
			nate+=int(message.content[3:6])
			goldreplace(xp[1], 8)
		elif (message.content[7:])=='noah':
			noah+=int(message.content[3:6])
			goldreplace(xp[2], 9)
		elif (message.content[7:])=='ryan':
			ryan+=int(message.content[3:6])
			goldreplace(xp[3], 10)
		elif (message.content[7:])=='luke':
			luke+=int(message.content[3:6])
			goldreplace(xp[4], 11)
		await client.send_message(message.channel, str(message.content[7:]).title()+" has gained "+str(message.content[3:6])+"XP. Good Job!")
	##############################################################################
client.run('MzUzNzAzNTc2MjMwNjkwODE2.DJYd6g.yVaB5wvURsS73EK5C2AUIunPZsU')


#j0-05YVxH6Wj-lj9xr-38aaB_d1Ez-SH  client secret
#MzUzNzAzNTc2MjMwNjkwODE2.DJYd6g.yVaB5wvURsS73EK5C2AUIunPZsU   token
#353703576230690816 client id

