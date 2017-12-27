
import random
from random import randint
from twilio.rest import Client



def send_sms(content):

	account_sid = 'AC17ca2519a557c64074c2c3ce6ee07c82'
	auth_token = '3e1ad535eca53901d8178aa0bf28c8eb'
	client = Client(account_sid, auth_token)

	client.messages.create(from_='(605) 644-6942', to='(605) 695-2356', body=content)






wordList = []
poem = ""

f = open("C:\\Users\\Noah Stremmel\\Documents\\sublimeFiles\\noah-joel\\wordsAA.txt.txt")
for line in f.readlines():
    wordList.append(line.strip())

wordsAdded = 0

while (wordsAdded < 10):
    index = randint(0, len(wordList)-1)
    currentRandomWord = wordList[index]      
    poem = poem + currentRandomWord + " " 
    wordsAdded = wordsAdded + 1



file = open('C:\\Users\\Noah Stremmel\\Documents\\sublimeFiles\\noah-joel\\billy.html.css', 'w')
save_path = ("C:\\Users\\Noah Stremmel\\Documents\\sublimeFiles\\noah-joel\\billy.html.css")
file.write(str(poem))
file.close()

print(poem)


send_sms(poem)