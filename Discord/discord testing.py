import discord

client=discord.Client()


@client.event
async def on_ready():
	print("Bot Logged In!");

@client.event
async def on_message(message):
	if message.content.startswith('!commandsplz'):
		await client.send_message(message.author,'test')




		
client.run('MzUzNzAzNTc2MjMwNjkwODE2.DJYd6g.yVaB5wvURsS73EK5C2AUIunPZsU')