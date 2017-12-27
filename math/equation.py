from random import randint
from time import sleep
import os
import sys
from twilio.rest import Client
import random




# def send_sms(content):

# 	account_sid = 'AC17ca2519a557c64074c2c3ce6ee07c82'
# 	auth_token = '3e1ad535eca53901d8178aa0bf28c8eb'
# 	client = Client(account_sid, auth_token)

# 	client.messages.create(from_='(605) 644-6942', to='(605) 695-4246', body=content)






mylist=[]
possibilities=['operator','number']
operators=['+','-','/','*']
lengths=[7,9]
length=random.choice(lengths)
for i in range(length):
	mylist+=' '


mylist[0]=randint(2,50)
mylist[-1]=randint(2,50)
mylist[round((length-1)/2)]='='
mylist[round(((length-1)/2)+1)]=randint(2,50)
mylist[round(((length-1)/2)-1)]=randint(2,50)


while True:
	spot=randint(0,length-1)
	if mylist[spot]=='=':
		continue
	mylist[spot]='x'
	if mylist[-2]=='x':
		continue
	break


x=0
while x<length-1:
	if mylist[x]!=' ':
		x+=1
		continue
	if mylist[x-1] in operators:
		mylist[x]=randint(2,50)
	else:
		mylist[x]=random.choice(operators)
	x+=1


for i in range(len(mylist)):
   mylist[i] = str(mylist[i])
problem=''.join(mylist)
#send_sms("Hey Joel! I made a program that randomly generates an algebraic equation to simplify. (Sometimes, it is impossible)")
#send_sms("[%s]" %problem)
print(problem)
answer=input("Solve this algebraic equation. ")



import operator
ops = { "+": operator.add, "-": operator.sub, "*": operator.multiply, "/": operator.divide} # etc.

print (ops["+"](1,1)) # prints 2 

while True:
	if mylist[x] != int: