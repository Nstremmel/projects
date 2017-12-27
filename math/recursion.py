while (True):
	ask = input("Pick AN INTEGER to find the factorial of. ")
	ask = int(ask)
	answer1 = (ask)
	counter=(1)
	if ask > (50000):
		print ("")
		print ("That number is too large! Pick a different one.")
		print ("")
		continue;
	if ask < (1):
		print ("")
		print ("That number is too small! Pick a different one.")
		print ("")
		continue;


#main process starts here		
	while (counter < ask):
		answer1 *= int(ask-(counter))
		counter += (1)
#and it ends here

	print ("")
	print ("The factorial is: " + str(answer1))
	print ("")



