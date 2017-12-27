import os
from time import sleep
import random


twice = False
letter = ("abcdefghijklmnopqrstuvwxyz")
print ("Welcome to hangman!")
print ("")
words = ["america", "bathtub", "cartoon", "devastating", "evolution", "finance", "garage", "hippopotamus", "internet", "jealous", "knowledge", "lamp", "marker", "newsletter", "orange", "picture", "quartet", "rabbit", "sunshine", "television", "urgent", "vacant", "watertower", "xenophobia", "yawn", "zookeeper", "frog", "magnet", "water", "pillow", "curtain", "glass", "hair", "feet", "green", "blue", "orange", "purple", "black", "grey", "yellow", "red", "cake", "garden", "chair", "desktop", "snake", "numbers", "picture", "fruit", "carpet", "stove", "bench", "blanket", "clocktower", "clay", "shouting", "carseat"]
wordselect = (random.choice(words))
sleep(1)
print ("Your word has been chosen")
print ("")
underscore = ("")
counter = (0)
while (counter < 13):
	if len(wordselect) == counter:
	   letters = (underscore)
	counter += (1)
	underscore += ("-")
print (letters)
print ("")
wrongGuess = ("")
seperate = []
seperate += (wordselect)
Final = (letters)
while (True):
    final = []
    final += (Final)
    guess = input("Guess one letter or guess the word. ").lower()
    if guess == (""):
        print ("")
        print ("Thats not a letter or word! Try again.")
        print ("")
        continue;
    elif guess == (wordselect):
        break;
    elif guess == ("stop"):
        break;
    if guess in seperate:
        print ("")
        print ("There is a(n) %s in the word!" %guess)
        counter2 = (0)
        while (True):
            try:
                if guess == (seperate[counter2]):
                    final[counter2] = (guess)
                elif twice == True:                
                    if final[counter2] in letter:
                        counter2 += (1)
                        continue;
                else:
                    final[counter2] = ("-")
                    counter2 += (1)
                    continue;
                counter2 += (1)
            except IndexError:
                break;
        print ("")
        sleep (.5)
        if wrongGuess == (""):
            print ("You haven't guessed any letters incorrectly! :)");
        else:
            print ("Letters you guessed incorrectly: " + wrongGuess);
        sleep (.5)
        print ("")
        Final = "".join(final)
        print (Final)
        sleep (.5)
        print ("")
        twice = True
    else:
        print ("")
        print ("There is no %s in the word." %guess)
        print ("")
        wrongGuess += (guess + ", ")
        sleep (.5)
        print ("Letters you guessed incorrectly: " + wrongGuess)
        sleep (.5)
        print ("")
        print (Final)
        print ("")
        twice = True
print ("")
print ("Congradulations! You won!")
print ("")
input("Press ENTER to exit.")
