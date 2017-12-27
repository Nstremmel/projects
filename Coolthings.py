import os
import time
from time import sleep
from random import randint
import random




"""
while (True):
    print ("")
    ask = input("Type in a number 1-200. ")
    print ("")
    if (int(ask)) > 200:
        print ("That isn't 1-200! Try again!")
        continue;
    if (int(ask)) < 1:
        print ("That isn't 1-200! Try again!")
        continue;
    else:
        break;
counter = (1)
while (True):
    counter += (1)
    print ("This will be typed %s times." %(int(ask)))
        sleep (.1)
    if counter > (int(ask)):
        break;
    else:
        continue;
print ("")
print ("#Finished")
input ("")
"""



"""
counter = (2)
while (True):
    counter -= .2
    sleep(counter)
    print ("Buuuuuuuuuuuuuu")
    sleep(counter)
    print ("Dun!")
    print ("")
    if counter < (.2):
        break;
    else:
        continue;
        """


"""
print("Welcome to your personal Clock!")
print ("")
sleep (.4)
while (True):
    checktime = input("Would you like to look at the time?...Type Yes or No. ").lower()
    if checktime == ("yes"):
        time1 = time.strftime("%b %d %Y %H:%M:%S")
        print ("")
        sleep(.5)
        print (time1)
        break;
    elif checktime == ("no"):
        print ("")
        print ("Thats fine.")
        break;
    else:
        print ("I don't think you typed in yes or no. Try again.")
        print ("")
        continue;
print ("")
stopwatch = input("Do you want to start a timer?...Type Yes or No. ").lower()
if stopwatch == ("yes"):
    print ("")
    length = input("How long do you want the timer to be in seconds?...Type a number. ")
    length = int(length)
    while (0 < length):
        print (str(length))
        length -= (1)
        sleep(1)
        os.system("cls")
    print ("")
    print ("TIMER IS DONE!")
elif stopwatch == ("no"):
    print ("")
    print ("Thats fine.")
print ("")
input("press ENTER to exit")
"""
       
       
       



"""
print("Welome to the survey!")
print("")
dogs = open("C:\\Users\\Noah Stremmel\\Documents\\survey.txt", "r").readlines()[0]
dogs = int(dogs)
cats = open("C:\\Users\\Noah Stremmel\\Documents\\survey.txt", "r").readlines()[1]
cats = int(cats)
while (True):
    question = input("Do you prefer dogs, or cats?...Type \"dogs\" or \"cats\". ").lower()
    if question == ("dogs"):
        dogs1 = (dogs + 1)
        dogs1 = str(dogs1)
        cats1 = str(cats)
        f = open("C:\\Users\\Noah Stremmel\\Documents\\survey.txt", "w")
        f.write(dogs1 + "\n")
        f.write(cats1)
        f.close()
        break;
    elif question == ("cats"):
        cats1 = (cats + 1)
        cats1 = str(cats1)
        dogs1 = str(dogs)
        file = open("C:\\Users\\Noah Stremmel\\Documents\\survey.txt", "w")
        file.write(dogs1 + "\n")
        file.write(cats1)
        file.close()
        break;
    else:
        print ("")
        print ("I don't think you typed in either dogs or cats. Try again.")
        print ("")
        continue;
sleep (1.5)
print ("")
print ("Your oppinion has been added to the data.")
print ("")
sleep (.5)
print ("Currently, %s people have voted for dogs " %dogs1 + "and %s people have voted for cats." %cats1)
input("")
"""


"""
phrases = []
words = []
while (True):
    while (True):
        printwords = input("Type in a phrase you want to be shown when you type in a word. ")
        add = input("Type in the word you will type in to display that phrase. ")
        phrases.append(printwords)
        words.append(add)
        print ("")
        more = input ("Would you like to add more words and phrases?...Type Yes or No. ").lower()
        print ("")
        if more == ("no"):
            break;
    os.system("cls")
    counter = (0)
    while (True):
        userinput = input("Type in a word. ")
        if userinput == ("stop"):
            break;
        while (True):
            try:
                if str(userinput) in str(words[counter]):
                    print (phrases[counter])
                    break;
                else:
                    counter += (1)
            except:
                os.system("cls")
                break;
    """     


"""
while (True):
    digits = input("How many digits of pi do you want to see? ")
    if digits == ("exit"):
        break;
    digits = int(digits)
    pi = ("3.1415926535897932384626433832795028841971693993")
    length = len(pi)
    if digits > (length-1):
        print ("")
        print ("That number is too high!")
        print ("")
        continue;
    counter = (0)
    final = ("")
    while (counter < (digits+1)):
        final += (pi[counter])
        counter += (1);
    print (final)
    print ("")
print ("")
input ("Press ENTER to exit.")
"""



"""
while (True):
    roll=input("How many sides do you want on your die? ")
    if roll == ("clear"):
        os.system("cls")
        continue;
    output = str(randint(1,int(roll)))
    print ("You roll a " + output + ("."))
    if output == roll:
        print ("Congadulations!");
    elif output == ("1"):
        print ("A 1? Thats too bad. :(")
    print ("")
    """


"""
while (True):
    love = input("On a scale of 1-10, how much do you love your mother? ")
    answers = open("C:\\Users\\Noah Stremmel\\Documents\\sublimeFiles\\love.txt", "r").readlines()[0]
    amount = open("C:\\Users\\Noah Stremmel\\Documents\\sublimeFiles\\love.txt", "r").readlines()[1]
    os.system("break>love.txt")
    f= open("C:\\Users\\Noah Stremmel\\Documents\\sublimeFiles\\love.txt", "w")
    f.write(str(int(love) + int(answers))+"\n")
    f.write(str(int(amount)+1))
    f.close()
    answers1 = open("C:\\Users\\Noah Stremmel\\Documents\\sublimeFiles\\love.txt", "r").readlines()[0]
    amount1 = open("C:\\Users\\Noah Stremmel\\Documents\\sublimeFiles\\love.txt", "r").readlines()[1]
    print ("On average, on a scale of 1-10, people love their mother " + str(int(answers1)/int(amount1)) + " out of 10.")
    print ("")
    """


'''
matrix = ("")
os.system("color 0a")
combos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
#options = ["0", "1"]
#options = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#options = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "=", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "{", "~", "[", "]", "}", "\\", "|", "<", ".", ">", ",", "?", "/", ";", ":", "\"", "'"]
#options = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "=", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "{", "~", "[", "]", "}", "\\", "|", "<", ".", ">", ",", "?", "/", ";", ":", "\"", "'", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
#options = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "=", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "{", "~", "[", "]", "}", "\\", "|", "<", ".", ">", ",", "?", "/", ";", ":", "\"", "'", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
while (True):
    while len(matrix) < 140:
        matrix += random.choice(options)
    print (matrix)
    #os.system("color " + random.choice(combos) + random.choice(combos))
    matrix = ("")
    sleep (.05)
'''



drink = ("beer")
bottles = (5)
while bottles > 1:
    print (str(bottles)+" bottles of %s on the wall." %drink)
    sleep (1.4)
    print (str(bottles)+" bottles of %s." %drink)
    sleep (1.6)
    print ("Take one down.")
    sleep (.9)
    print ("Pass it around,")
    sleep (1.1)
    print (str(bottles-1)+" bottles of %s on the wall!" %drink)
    print ("")
    sleep (1.6)
    bottles -= (1)
print ("1 bottle of %s on the wall." %drink)
sleep (1.4)
print ("1 bottle of %s." %drink)
sleep (1.6)
print ("Take it down, pass it around...")
sleep (3)
print ("OH NO WE RAN OUT OF %s!" %drink.upper())
input ("")



"""
print ("           LOADING...")
progress=[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","]"]
Counter=(0)
while Counter<17:
    sleep(random.randint(2,10)/5)
    os.system("cls")
    print ("           LOADING...")
    print("[" + ' '.join(map(str, progress)))
    progress[Counter]="%"
    Counter+=(1)
"""