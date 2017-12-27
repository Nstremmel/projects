from time import sleep
import os



keyboard=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
test="qwertyuiopasdfghjklzxcvbnm"
while True:
	characters=[]
	choice=input("Would you like to encode a message or decode a message? (Type 1 for encode and 2 for decode) | ")
	print("")

	
	if choice=="1":
		userinput=input("Put your message in here to have it be encoded. ").lower()
		characters+=userinput
		for i, value in enumerate(characters):
			if value=='m':
				characters[i]='q'
			elif value in keyboard:
				x=test.find(value)
				characters[i]=keyboard[int(x)+1]
			else:
				continue
	else:
		userinput=input("Put your message in here to have it be decoded. ").lower()
		characters+=userinput
		for i, value in enumerate(characters):
			if value=='q':
				characters[i]='m'
			elif value in keyboard:
				x=test.find(value)
				characters[i]=keyboard[int(x)-1]
			else:
				continue


	print("".join(characters))
	print("")
	input("Press ENTER To Continue")
	os.system("cls")
