from time import sleep
from random import randint
while (True):
	onetwo = input("Do you want to play one player or two player rock paper scissors?.....Type \"One\" or \"Two\" ").lower()
	if onetwo == ("one"):
		print ("")
		print ("Welcome to one player rock paper scissors!")
		print ("")
		while (True):
			while (True):
				sleep (.5)
				ask = input("Type rock paper or scissors :) ").lower()
				if ask == ("rock"):
					player = ("rock")
					break;
				elif ask == ("paper"):
					player = ("paper")
					break;
				elif ask == ("scissors"):
					player = ("scissors")
					break;
				else:
					print ("")
					print ("You didn't type in rock, paper, or scissors. Try again.")
					print ("")
					continue;
			sleep (1)
			print ("")
			random = (randint(1,3))
			sleep (.5)
			if random == (1):
				if player == ("rock"):
					print ("You picked rock and the computer also picked rock. Try again.")
					print ("")
					continue;
				if player == ("paper"):
					print ("You picked paper and the computer picked rock. You win!")
					print ("")
					break;
				if player == ("scissors"):
					print ("You picked scissors and the computer picked rock. You lose.")
					print ("")
					break;
			elif random == (2):
				if player == ("rock"):
					print ("You picked rock and the computer picked paper. You lose.")
					print ("")
					break;
				if player == ("paper"):
					print ("You picked paper and the computer also picked paper. Try again.")
					print ("")
					continue;
				if player == ("scissors"):
					print ("You picked scissors and the computer picked paper. You win!")
					print ("")
					break;
			elif random == (3):
				if player == ("rock"):
					print ("You picked rock and the computer picked scissors. You win!")
					print ("")
					break;
				if player == ("paper"):
					print ("You picked paper and the computer picked scissors. You lose.")
					print ("")
					break;
				if player == ("scissors"):
					print ("You picked scissors and the computer also picked scissors. Try again.")
					print ("")
					continue;
		again = input("Do you want to play again?...Type Yes or No ").lower()
		if again == ("yes"):
			print ("")
			continue;
		elif again == ("no"):
			break
			print ("")
			input("Thanks for playing rock paper scissors! Press enter to exit the game.");
	elif onetwo == ("two"):
		print ("")
		print ("Welcome to two player rock paper scissors!")
		print ("")
		while (True):
			import getpass
			ask1 = getpass.getpass("Player one, type in either rock paper or scissors. You won't be able to see what you type but it is actually there.").lower()
			if ask1 == ("rock"):
				player1 = ("rock");
			elif ask1 == ("paper"):
				player1 = ("paper");
			elif ask1 == ("scissors"):
				player1 = ("scissors");
			else:
				print ("")
				print ("I don't think you typed in rock, paper, or scissors. Try again.")
				print ("")
				continue;
			print ("")
			sleep (.5)
			ask2 = getpass.getpass("Player two, type in either rock paper or scissors. You won't be able to see what you type but it is actually there.").lower()
			print ("")
			if ask2 == ("rock"):
				player2 = ("rock")
			elif ask2 == ("paper"):
				player2 = ("paper")
			elif ask2 == ("scissors"):
				player2 = ("scissors")
			else:
				print ("")
				print ("I don't think you typed in rock, paper, or scissors. Try again.")
				print ("")
				continue;
			if player1 == ("rock"):	
				if player2 == ("rock"):
					print ("You both picked rock. Try again.")
					print ("")
					continue;
				if player2 == ("paper"):
					print ("Player 1 picked rock and player 2 picked paper. Player 2 wins!")
					print ("")
					break;
				if player2 == ("scissors"):
					print ("Player 1 picked rock and player 2 picked scissors. Player 1 wins!")
					print ("")
					break;
			elif player1 == ("paper"):
				if player2 == ("rock"):
					print ("Player 1 picked paper and player 2 picked rock. Player 1 wins!")
					print ("")
					break;
				if player2 == ("paper"):
					print ("You both picked paper. Try again.")
					print ("")
					continue;
				if player2 == ("scissors"):
					print ("Player 1 picked paper and player 2 picked scissors. Player 2 wins!")
					print ("")
					break;
			elif player1 == ("scissors"):
				if player2 == ("rock"):
					print ("Player 1 picked scissors and player 2 picked rock. Player 2 wins!")
					print ("")
					break;
				if player2 == ("paper"):
					print ("Player 1 picked scissors and player 2 picked paper. Player 1 wins!")
					print ("")
					break;
				if player2 == ("scissors"):
					print ("You both picked scissors. Try again.")
					print ("")
					continue;
		ask3 = input("Do you want to play again?...Type Yes or No ").lower()
		print ("")
		if ask3 == ("yes"):
			sleep (.5)
			continue;
		else:
			break;
	else:
		print ("")
		print ("I don't think that you typed one or two. Try again.")
		print ("")
		continue;
print ("")
sleep (1)
input("Thanks for player rock paper scissors! Press enter to exit the game.")

	 