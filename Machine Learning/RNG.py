#IMPORTS
import calendar
import time
from os import system

#FUNCTIONS
def generate_k_random_numbers(x0, m, generated, n, k):
	if n == k:
		return generated
	else:
		a = 675789
		b = 24539

		xn = (a*x0 + b) % m
		generated.append(xn)
		# print("At n = {}: Xn = {}".format(n, xn))

		n += 1

		return generate_k_random_numbers(x0=xn, m=m, generated=generated, n=n, k=k)
#########################################################################################
def main(k,m):

	
	generated = []
	current_time = calendar.timegm(time.gmtime())

	# print("Current time is {}".format(current_time))
	# print("Generating {} random numbers between 0 and {}".format(k, m))

	generated = generate_k_random_numbers(x0=current_time, m=m, generated=generated, n=0, k=k)
	#print("Generated sequence: \n{}.".format(generated))
	return int(generated[0])

#########################################################################################
#BODY
# while True:
# 	amount=int(input("How many numbers would you like to generate? "))
# 	between=int(input("Generate a number between 0 and what number? "))
# 	system("cls")
# 	main(amount,between)
# 	print("")
