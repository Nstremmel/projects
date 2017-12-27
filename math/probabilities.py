import random
from time import sleep

while (True):
	number = input("What number do you want to test? ")
	timestested = input("How many times do you want to test for this number to show up? ")
	numberadd = (0)
	counter = (0)
	inputvar = ("")
	while (counter < int(timestested) + 1):
		mylist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
		numberadd += (1)
		inputvar += random.choice(mylist)
		if number in inputvar:
			inputvar = ("")
			counter += (1)
	print ("It took " + str(numberadd) + " numbers to be added in order to have " + str(number) + " show up " + str(timestested) + " time(s).")
	print ("")