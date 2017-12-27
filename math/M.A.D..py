#SYSTEM DOESN'T WORK WITH 0'S
while (True):
	#finding mean + input
	number = []
	while (True):
		ask = input("Enter a number in the data set. When you entered them all, press ENTER to continue. ")
		if ask == (""):
			break;
		amount = input("How many of that number do you have in the data set? ")
		counter1 = (0)
		while (int(amount)>counter1):
			number += str(ask)
			counter1 += (1)
	counter2 = len(number)
	mean = sum(list(map(int, number)))/int(counter2)
	number = (list(map(int, number)))

	#finding mad + output
	absolute=(0)
	counter3=0
	while (counter3<len(number)):
		absolute += (abs(number[counter3]-3))
		counter3 += (1)
	mad=absolute/len(number)
	print ("The mad is " + str(mad) + "!")
	print ("")

