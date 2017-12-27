

fib=["1", "1"]
for i in range(100000):
	fib+=' '
	fib[-1]=str(int(fib[-2])+int(fib[-3]))
	if "314159" in fib[-1]:
		print(len(fib))
		print(fib[-1])


