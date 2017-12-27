player1=(20)
player2=(20)
while (True):
	player = input("What player is losing health? ")
	print ("")
	amount = input("How much health is lost? ")
	if player == ("1"):
		player1 -= int(amount)
	elif player == ("2"):
		player2 -= int(amount)
	print ("")
	if player2 <= 0:
		print ("Player 1 has won!")
		player1 = (20)
		player2 = (20)
	elif player1 <= 0:
		print ("Player 2 has won!")
		player1 = (20)
		player2 = (20)
	else:
		print ("Player 1 has " + str(player1) + " health left.")
		print ("Player 2 has " + str(player2) + " health left.")
	print ("")

