import discord
import asyncio
import random
from time import sleep
import os

client = discord.Client()
path=("C:\\Users\\Andy\\Documents\\Sublime\\Documents")

players=[]


def goldreplace(var, linenumber, myid):
	if isinstance(var, str)==True:
		None
	else:
		var=round(var)
	f=open("C:\\Users\\Andy\\Documents\\Sublime\\Documents\\"+myid+".txt", "r")
	f1=open("C:\\Users\\Andy\\Documents\\Sublime\\Documents\\host.txt", "w")
	counter=(0)
	for line in f:
		if counter == int(linenumber):
			f1.write(str(var)+"\n");
		else:
			f1.write(line);
		counter+=(1)
	f.close()
	os.system("del \"C:\\Users\\Andy\\Documents\\Sublime\\Documents\\"+myid+".txt\"")
	f2=open("C:\\Users\\Andy\\Documents\\Sublime\\Documents\\"+myid+".txt", "w")
	f1=open("C:\\Users\\Andy\\Documents\\Sublime\\Documents\\host.txt", "r")
	for line in f1:
		f2.write(line);
	f1.close()
	os.system("del \"C:\\Users\\Andy\\Documents\\Sublime\\Documents\\host.txt\"")



@client.event
async def on_ready():
	print("Bot Logged In!")


@client.event
async def on_message(message):
	if message.content==("!points"):
		try:
			points=int(open("C:\\Users\\Andy\\Documents\\Sublime\\Documents\\"+message.author.id+".txt").readlines()[0].splitlines()[0])
		except:
			t=open("C:\\Users\\Andy\\Documents\\Sublime\\Documents\\"+message.author.id+".txt", "w")
			t.write("0\n")
			t.close()
			points=int(open("C:\\Users\\Andy\\Documents\\Sublime\\Documents\\"+message.author.id+".txt").readlines()[0].splitlines()[0])
		await client.send_message(message.channel, str(message.author)+" has "+str(points)+" points.")
	elif message.content.startswith("!give"):
		try:
			points=int(open("C:\\Users\\Andy\\Documents\\Sublime\\Documents\\"+message.author.id+".txt").readlines()[0].splitlines()[0])
		except:
			t=open("C:\\Users\\Andy\\Documents\\Sublime\\Documents\\"+message.author.id+".txt", "w")
			t.write("0\n")
			points=int(open("C:\\Users\\Andy\\Documents\\Sublime\\Documents\\"+message.author.id+".txt").readlines()[0].splitlines()[0])
		points+=int(message.content[29:])
		goldreplace(points,0,message.author.id)
	elif message.content.startswith("!take"):
		try:
			points=int(open("C:\\Users\\Andy\\Documents\\Sublime\\Documents\\"+message.author.id+".txt").readlines()[0].splitlines()[0])
		except:
			t=open("C:\\Users\\Andy\\Documents\\Sublime\\Documents\\"+message.author.id+".txt", "w")
			t.write("0\n")
			points=int(open("C:\\Users\\Andy\\Documents\\Sublime\\Documents\\"+message.author.id+".txt").readlines()[0].splitlines()[0])
		points-=int(message.content[29:])
		goldreplace(points,0,message.author.id)






client.run("MzUzNzAzNTc2MjMwNjkwODE2.DJYd6g.yVaB5wvURsS73EK5C2AUIunPZsU")


#373951307091935232 - client id
