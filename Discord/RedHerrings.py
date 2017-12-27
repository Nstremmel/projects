import discord
import asyncio
import random
from time import sleep
import os

path=("C:\\Users\\Andy\\Documents\\Sublime\\Documents\\clan.txt")
path1=("C:\\Users\\Andy\\Documents\\Sublime\\Documents\\competition.txt")
client = discord.Client()
ball=('My sources say yes.', 'Not in a million years!', 'Why ask me when Axegila knows all?', 'Ask again later.', 'Possibly...', 'It is certain!', 'For sure!', 'Who knows? I\'m just a code writen by Old Poet!')
momma=('Yo momma is so fat, I took a picture of her last Christmas and it\'s still printing.', 'Yo mamma is so fat she doesn\'t need the internet because she\'s already world wide.', 'Yo momma is so fat she needs cheat codes for Wii Fit.', 'Yo mamma is so ugly that when she went into a haunted house, she came out with a job application.', 'Yo momma is so fat, she has more rolls than a bakery.', 'Yo mama so fat, she sat on an iPhone and turned it into an iPad.')
colors=["A","B","C","D","E","F","0","1","2","3","4","5","6","7","8","9"]
players=[]
numbers=[]
objects=[]

def goldreplace(var, linenumber):
	if isinstance(var, str)==True:
		None
	else:
		var=round(var)
	f=open("C:\\Users\\Andy\\Documents\\Sublime\\Documents\\clan.txt", "r")
	f1=open("C:\\Users\\Andy\\Documents\\Sublime\\Documents\\host.txt", "w")
	counter=(0)
	for line in f:
		if counter == int(linenumber):
			f1.write(str(var)+"\n");
		else:
			f1.write(line);
		counter+=(1)
	f.close()
	os.system("del \"C:\\Users\\Andy\\Documents\\Sublime\\Documents\\clan.txt\"")
	f2=open("C:\\Users\\Andy\\Documents\\Sublime\\Documents\\clan.txt", "w")
	f1=open("C:\\Users\\Andy\\Documents\\Sublime\\Documents\\host.txt", "r")
	for line in f1:
		f2.write(line);
	f1.close()
	os.system("del \"C:\\Users\\Andy\\Documents\\Sublime\\Documents\\host.txt\"")


@client.event
async def on_ready():
	print("Bot Logged In!");

@client.event
async def on_message(message):
	global players
	global numbers
	zamorak1=int(open(path).readlines()[0].splitlines()[0])
	bandos=int(open(path).readlines()[1].splitlines()[0])
	armadyl=int(open(path).readlines()[2].splitlines()[0])
	saradomin=int(open(path).readlines()[3].splitlines()[0])
	####################################################
	zamorak2=int(open(path).readlines()[4].splitlines()[0])
	sliske=int(open(path).readlines()[5].splitlines()[0])
	seren=int(open(path).readlines()[6].splitlines()[0])
	zaros=int(open(path).readlines()[7].splitlines()[0])
	####################################################
	if message.content.startswith('!colorpicker'):
		color=('')
		for i in range(6):
			color+=random.choice(colors)
		await client.send_message(message.channel, "Your random color is https://www.google.com/search?q=%23"+color+"&source=lnms&sa=X&ved=0ahUKEwidq66FnZTXAhXH1IMKHW8rDy4Q_AUICSgA&biw=1440&bih=769&dpr=1")
	#####################################################
	elif message.content.startswith('!8ball'):
		await client.send_message(message.channel, str(random.choice(ball)))
	#####################################################
	elif message.content.startswith('!momma'):
		await client.send_message(message.channel, str(random.choice(momma)))
	#####################################################
	elif message.content.startswith('!enter'):
		f=open(path1).read()
		print(message.content[6:8])
		if str(message.content[6:8]) in str(f[:2]):
			await client.send_message(message.channel, "<@"+message.author.id+">, that number has already been taken. Try a different one.")
		elif str(message.author.id) in f:
			await client.send_message(message.channel, "<@"+message.author.id+">, you already entered the competition...")
		else:
			players.append(str(message.author))
			numbers.append(str(message.content[6:8]))
			f1=open(path1, "a")
			f1.write(str(message.content[6:8])+str(message.author.id)+"\n")
			f1.close()
			await client.send_message(message.channel, "<@"+message.author.id+">, You successfully entered the competition. Good luck!")
	#####################################################
	elif message.content.startswith('!winner'):
		if message.author.id=='199630284906430465':
			with open(path1) as f:
				lines=(sum(1 for _ in f))-1
			number=random.randint(0,lines)
			winner=str(open(path1).readlines()[number].splitlines()[0])
			await client.send_message(message.channel, "<@"+winner[2:]+"> has won the competition with number "+winner[:2]+"! Congrats!")
	#####################################################
	elif message.content.startswith("!clearcompetition"):
		if message.author.id=='199630284906430465':
			os.system("del \"C:\\Users\\Andy\\Documents\\Sublime\\Documents\\competition.txt\"")
			f=open(path1, "w")
			f.close()
			players=[]
			numbers=[]
			await client.send_message(message.channel, "The competition has been cleared!")
	#####################################################
	elif message.content.startswith("!players"):
		await client.send_message(message.author, "The people currently entered in the competition are:")
		for i, value in enumerate(players):
			await client.send_message(message.author, str(value)+" with number "+str(numbers[i]))
	####################################################
	elif message.content.startswith("!nudes"):
		for i in range(5):
			await client.send_message(message.author, ":eggplant:")
		await client.send_message(message.author, "Your Welcome.")
	####################################################
	elif message.content.startswith("!throw"):
		await client.send_message(message.channel,"You throw "+str(message.content[7:])+" into the deep, dark, empty void.")
		objects.append(str(message.content[7:]))
	#########################################
	elif message.content.startswith("!catch"):
		if len(objects)==0:
			caught="nothing"
		else:
			caught=str(random.choice(objects))
		await client.send_message(message.channel, "You catch a "+caught+" out of the void that someone threw earlier!")
	####################################################
	# elif message.content.startswith("!change"):
	# 	await client.change_nickname(Member, "🎄"+str(message.author[:5]).title()+"🎄")



























	# elif message.content.startswith('!zamorak1'):
	# 	await client.send_message(message.channel, "You have killed "+str(zamorak1)+" K'ril Tsutsaroth.")
	# elif message.content.startswith('!bandos'):
	# 	await client.send_message(message.channel, "You have killed "+str(bandos)+" General Graardor.")
	# elif message.content.startswith('!armadyl'):
	# 	await client.send_message(message.channel, "You have killed "+str(armadyl)+" Kree'arra.")
	# elif message.content.startswith('!saradomin'):
	# 	await client.send_message(message.channel, "You have killed "+str(saradomin)+" Commander Zilyana.")
	# elif message.content.startswith('!zamorak2'):
	# 	await client.send_message(message.channel, "You have killed "+str(zamorak2)+" Twin Furies.")
	# elif message.content.startswith('!sliske'):
	# 	await client.send_message(message.channel, "You have killed "+str(sliske)+" Gregorovic.")
	# elif message.content.startswith('!seren'):
	# 	await client.send_message(message.channel, "You have killed "+str(seren)+" Helwyr.")
	# elif message.content.startswith('!zaros'):
	# 	await client.send_message(message.channel, "You have killed "+str(zaros)+" Vindicta and Gorvek.")
	# ######################################################
	# elif message.content.startswith('zamorak1+'):
	# 	zamorak1+=int(message.content[8:])
	# elif message.content.startswith('bandos+'):
	# 	bandos+=int(message.content[6:])
	# elif message.content.startswith('armadyl+'):
	# 	armadyl+=int(message.content[7:])
	# elif message.content.startswith('saradomin+'):
	# 	saradomin+=int(message.content[9:])
	# elif message.content.startswith('zamorak2+'):
	# 	zamorak2+=int(message.content[8:])
	# elif message.content.startswith('sliske+'):
	# 	sliske+=int(message.content[6:])
	# elif message.content.startswith('seren+'):
	# 	seren+=int(message.content[5:])
	# elif message.content.startswith('zaros+'):
	# 	zaros+=int(message.content[5:])
	# ######################################################
	# elif message.content.startswith('zamorak1-'):
	# 	zamorak1-=int(message.content[9:])
	# elif message.content.startswith('bandos-'):
	# 	bandos-=int(message.content[7:])
	# elif message.content.startswith('armadyl-'):
	# 	armadyl-=int(message.content[8:])
	# elif message.content.startswith('saradomin-'):
	# 	saradomin-=int(message.content[10:])
	# elif message.content.startswith('zamorak2-'):
	# 	zamorak2-=int(message.content[9:])
	# elif message.content.startswith('sliske-'):
	# 	sliske-=int(message.content[7:])
	# elif message.content.startswith('seren-'):
	# 	seren-=int(message.content[6:])
	# elif message.content.startswith('zaros-'):
	# 	zaros-=int(message.content[6:])




		
	# gods=[zamorak1,bandos,armadyl,saradomin,zamorak2,sliske,seren,zaros]
	# for i, value in enumerate(gods):
	# 	goldreplace(value,i)










client.run('MzUzNzAzNTc2MjMwNjkwODE2.DJYd6g.yVaB5wvURsS73EK5C2AUIunPZsU')

#j0-05YVxH6Wj-lj9xr-38aaB_d1Ez-SH  client secret
#MzUzNzAzNTc2MjMwNjkwODE2.DJYd6g.yVaB5wvURsS73EK5C2AUIunPZsU   token
#353703576230690816 client id
#https://discordapp.com/oauth2/authorize?&client_id=353703576230690816&scope=bot&permissions=0%EF%BB%BF