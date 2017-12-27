import winsound
from random import randint


phrase=input("Enter your phrase to turn it into a song. ").lower()
letters=("abcdefghijklmnopqrsxtuvwxyz")
characters=[]
characters+=phrase
for i, value in enumerate(characters):
	if value==' ':
		winsound.Beep(37,50)


	elif value in letters:
		frequency=randint(37,500)+int(letters.find(value)*4)
		rate=i*4+randint(25,200)
		winsound.Beep(frequency,rate)

#   #rest
#         freq = 37
#     #low c
#         freq = 262
#     #d
#         freq = 294
#     #e
#         freq = 330
#    #f
#         freq = 349
#   #g
#         freq = 392
#    #a
#         freq = 440
# #b
#         freq = 494
# #high c
#         freq = 523
        
