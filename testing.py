import winsound
from random import randint
from time import sleep


mylist=("")
letters=input("Put in your letters (No spaces or commas) | ")
characters=[]
characters+=letters
for i, value in enumerate(characters):
	first=("")
	second=("")
	third=("")
	first+=value
	for x in range(4):
		second=first
		if x>=i:
			second+=characters[x+1]
		else:
			second+=characters[x]
		for p in range(3):
			third=second
			if p>=x:
				third+=characters[p+2]
			else:
				third+=characters[p+1]




			if third in mylist:
				None
			else:
				mylist+=third+"."
				print(third)
			



input("")
