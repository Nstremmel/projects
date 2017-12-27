import os





while True:	
	query=str(input("Type a string of numbers to look for. "))
	numbers=int(input("How many fibonatchi numbers do you want to look at? "))
	fib=["1", "1"]
	for i in range(numbers):
		fib+=' '
		fib[-1]=str(int(fib[-2])+int(fib[-3]))
		if query in fib[-1]:
			print("Your string was found in the "+str(len(fib))+"th fibonatchi number.")
			print(fib[-1])
	input("Press ENTER to continue.")
	os.system("cls")

