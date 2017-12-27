import os
from time import sleep
from random import randint











while (True):
	os.system("color 0b")
	counter3 = (1)
	if ('yup') in open("C:\\Users\\Noah Stremmel\\Documents\\account.txt").read():
	    account = ("yes");
	else:
		account = ("no");
	login = input("Do you want to login to your account?...Type Yes or No. ").lower()
	if login == ("admin"):
		#stuff for admin here!
		print ("")
		print ("Welcome Noah Stremmel to your private admin account!")
		print ("")
		print ("You are awesome!")
		print ("")
		input ("Press ENTER to exit.")
		print ("");
	elif login == ("no"):
		print ("")
		print ("Thats fine. Bye!")
		break;
	elif login == ("yes"):
		print ("")
		if account == ("no"):
			print ("It appears that you do not have an account right now!")
			print ("")
			make = input("Would you like to make one?...Type Yes or No. ").lower()
			if make == ("yes"):
				print ("")
				user = input("What do you want your username to be? ")
				print ("")
				password = input("What do you want your password to be? ")
				print ("")
				f = open("C:\\Users\\Noah Stremmel\\Documents\\account.txt", "w")
				f.write("yup\n")
				f.write(user + "\n")
				f.write(password + "\n")
				f.close()
				sleep (.5)
				print ("Your account is ready!")
				print ("")
				continue;
			else:
				print ("")
				print ("Don't want to make one? Thats fine.")
				break;
		else:
			askuser = input("Type in your username: ") + ("\n")
			print ("")
			askpassword = input("Type in your passsword: ") + ("\n")
			bob = open("C:\\Users\\Noah Stremmel\\Documents\\account.txt", "r").readlines()[1]
			if askuser == bob:
				usercorrect = ("tr");
			else:
				usercorrect = ("false");
			bill = open("C:\\Users\\Noah Stremmel\\Documents\\account.txt", "r").readlines()[2]
			if askpassword == bill:
				passcorrect = ("ue");
			else:
				passcorrect = ("false");
			if usercorrect + passcorrect == ("true"):
				print ("")
				sleep (1.5)
				print ("Welcome to your account!")
				print ("")
				sleep (.5)
				print ("In here there are a variety of things to do.")
				print ("")
				while (True):
					#from here you go into multiple games and usefull things that I have created.
					games = input("Do you want to go to games, other, or log out?...Type Games Other or Log. ").lower()
					#Games section:
					if games == ("games"):
						print ("")
						print ("Welcome to the games section of your account. In here you can play rock paper scissors, simon, or a choose your own adventure game.")
						print ("")
						rps = input("Do you want to play rock paper scissors, simon, or the adventure game?...Type \"rps\", \"simon\", or \"adventure\". ").lower()
						if rps == ("rps"):
							#rps game


							print ("")
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
										print ("")
										print ("Thanks for playing rock paper scissors!")
										print ("")
										sleep(1.5)
										break;
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
									print ("")
									print ("Thanks for playing!")
									print ("")
									break;

							else:
								print ("")
								print ("I don't think that you typed one or two. Try again.")
								print ("")
								continue;
								#end of rps

						elif rps == ("adventure"):
							print ("")
							os.system("\"C:\\Users\\Noah Stremmel\\code2.py\"")
							print ("");


								#start of simon
						else:
							print ("");
							print ("You ready for this?")

							print ("3")
							sleep (1)
							print ("2")
							sleep (1)
							print ("1")
							sleep (1)
							print ("")
							os.system("color C0")
							print ("###############################################################################################################################################")
							sleep (.3)
							print ("#                                                                                                                                            #")
							sleep (.3)
							print ("#     l                        l                   lllllllllllllllllllll        ll                   ll                   lll                #") 
							sleep (.3)
							os.system("color E0")
							print ("#     l                        l                   l                            ll                   ll              l            l          #") 
							sleep (.3)
							print ("#     l                        l                   l                            ll                   ll             l               1        #")
							sleep (.3)
							print ("#     l                        l                   l                            ll                   ll            1                 1       #")
							sleep (.3)
							os.system("color A0")
							print ("#     l                        l                   l                            ll                   ll           1                   1      #")
							sleep (.3)
							print ("# llllllllllllllllllllllllllllllllll               lllllllllllllllllllll        ll                   ll          1                     1     #")
							sleep (.3)
							print ("#     l                        l                   l                            ll                   ll          1                     1     #")
							sleep (.3)
							os.system("color 30")
							print ("#     l                        l                   l                            ll                   ll           1                  1       #")
							sleep (.3)
							print ("#     l                        l                   l                            ll                   ll            1                1        #")
							sleep (.3)
							print ("#     l                        l                   l                            ll                   ll             1              1         #")
							sleep (.3)
							os.system("color 50")
							print ("#     l                        l                   l                            ll                   ll               1          1           #")
							sleep (.3)
							print ("#     l                        l                   l                            ll                   ll                 1       1            #")
							sleep (.3)
							print ("#     l                        l                   lllllllllllllllllllll        ll                   ll                    111               #")
							sleep (.3)
							print ("#                                                                                                                                            #")
							sleep (.3)
							print ("###############################################################################################################################################")
							sleep (.5)
							os.system("color 07")
							print ("")
							print ("That was pretty cool wasn't it?")
							print ("")
							print ("Welcome to Simon! In this game, random colors will flash on the screen. Each round, there will be a new random pattern with one more color than last time.")
							sleep (2)
							print ("")
							print ("After the round, you will have to type in the first letter of the colors, and if you get it right, you move on to the next round.")
							print ("")
							sleep (1)
							input("Press ENTER to start the game!")
							print ("")
							colors = ("")
							score = (0)
							count2 = (1)
							count = (0)
							while (True):
								count += (1)
								go = (randint(1,4))
								if go == (1):
									os.system("color C0")
									colors += ("r ")
									sleep (1);
								elif go == (2):
									os.system("color E0")
									colors += ("y ")
									sleep (1);
								elif go == (3):
									os.system("color A0")
									colors += ("g ")
									sleep (1);
								elif go == (4):
									os.system("color 10")
									colors += ("b ")
									sleep (1)
								if count == (count2):
									count2 += (1)
									os.system("color 0b")
									print ("Now type in the first letter of the color name followed by a space, and then the next letter. For instance if I had blue then red, I would type \"b r\".")
									print ("")
									right = input("").lower() + (" ")
									if right == (colors):
										score += (1)
										print ("")
										print ("You survived that round. Your score is %s" %(str(score)))
										print ("")
										colors = ("")
										count = (0)
										continue;
									else:
										print ("")
										print ("You lost. Your final score was %s" %(str(score)))
										print ("")
										again3 = input("Do you want to play again?...Type Yes or No. ").lower()
										if again3 == ("yes"):
											colors = ("")
											count = (0)
											score = (0)
											count2 = (1)
											print ("")
											continue;
										else:
											print ("")
											os.system("color 0b")
											break;
								else:
									os.system("color 0b")
									sleep (.2)
									continue;
											#end of simon
											#end of game section and start of other section
					elif games == ("other"):
						print ("")
						print ("In the \"Other\" section of your account, you can store information.")
						print ("")
						other = input("Type \"info\" to store information. ").lower()
						if other == ("info"):
							#start of information storage
							print ("")
							info = input("Do you want to look at your stored information?...Type Yes or No. ").lower()
							if info == ("yes"):
								hasinfo = open("C:\\Users\\Noah Stremmel\\Documents\\account.txt", "r").read()
								while (True):
									if ("9876543425562346342323542435356732") in hasinfo:
										print ("")
										print ("")
										line = (3)
										recover = ("stuff")
										while (True):
											line += (1)
											if recover == (" "):
												break;
											recover = open("C:\\Users\\Noah Stremmel\\Documents\\account.txt", "r").readlines()[line]
											print (recover)
											sleep (.5)
											continue;
										print ("")
										storemore = input("Do you want to store more information?...Type Yes or No. ").lower()
										if storemore == ("yes"):
											while (True):
												print ("")
												sleep(.5)
												information = input("Type in some information you want to store. ")
												file1 = open("C:\\Users\\Noah Stremmel\\Documents\\account.txt", "a")
												file1.write(information + "\n")
												file1.write(" ")
												file1.close()
												print ("")
												sleep (.5)
												print ("Your information has been stored.")
												print ("")
												addmore = input("Do you want to add more information to your account?...Type Yes or No. ").lower()
												if addmore == ("yes"):
													continue;
												else:
													print ("")
													break;
										
										break
										print ("")
									else:
										print ("")
										counter3 += (1)
										addmore = ("filler")
										if addmore == ("yes"):
											sleep(.1);
										elif addmore == ("filler"):
											print ("It looks like you haven't stored any information in your account.")
											print ("");
										else:
											sleep(.1);
										sleep(.5)
										information = input("Type in some information you want to store. ")
										file1 = open("C:\\Users\\Noah Stremmel\\Documents\\account.txt", "a")
										if counter3 == (2):
											file1.write("9876543425562346342323542435356732\n")
											file1.write(" ");
										file1.write(information + "\n")
										file1.write(" ")
										file1.close()
										print ("")
										sleep (.5)
										print ("Your information has been stored.")
									print ("")
									addmore = input("Do you want to add more information to your account?...Type Yes or No. ").lower()
									if addmore == ("yes"):
										continue;
									else:
										file7 = open("C:\\Users\\Noah Stremmel\\Documents\\account.txt", "a")
										file7.close()
										break;
										#end of information storage
							print ("")
						continue
					


					elif games == ("log"):
						print ("")
						print ("Thats fine. Goodbye!")
						break;

					else:
						print ("")
						print ("I don't think you typed either \"Games\" \"Other\" or \"Log\".")
						print ("")
						continue;
				break


			else:
				print ("")
				print ("Your username or password is incorrect.")
				print ("")
				continue;
	else:
		print ("")
		print ("I don't think you typed either yes or no. Try again.")
		print ("")
		continue;	
print ("")
input("Press ENTER to leave.")