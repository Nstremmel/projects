#!/usr/bin/env python
import random
from random import randint

wordList = []
poem = ""

f = open("C:\\Users\\Noah Stremmel\\Documents\\sublimeFiles\\noah-joel\\wordsAA.txt.txt")
for line in f.readlines():
	wordList.append(line.strip())

wordsAdded = 0

while (wordsAdded < 200):
    index = randint(0, len(wordList)-1)
    currentRandomWord = wordList[index]      
    poem = poem + currentRandomWord + " " 
    wordsAdded = wordsAdded + 1


file = open('C:\\Users\\Noah Stremmel\\Documents\\sublimeFiles\\noah-joel\\billy.html.css', 'w')
save_path = ("C:\\Users\\Noah Stremmel\\Documents\\sublimeFiles\\noah-joel\\billy.html.css")
file.write(str(poem))
file.close()

