# mIdea.py

# ------------------------------------ IMPORTS --------------------------------------------

import time

# ------------------------------------ FUNCTIONS --------------------------------------------

def bankIdea(idea):

    # Open ideaBank, bank current idea, close file opened in write/append mode
    ideaBankWrite = open("C:/Users/Noah Stremmel/Documents/sublimeFiles/ideaBank.txt", 'a')
    idea = idea.lower()
    ideaBankWrite.write('\n' + idea)
    ideaBankWrite.close()    

def relateIdea(idea, matchThreshold):

    # Format output
    print ("---------------------------------------------")

    # Open ideaBank to check for relations
    ideaBank = open("C:/Users/Noah Stremmel/Documents/sublimeFiles/ideaBank.txt", 'r')
    inputIdea = idea.split(' ')

    if (matchThreshold > len(inputIdea)):
        print ("Terminating: Word match threshold was greater than the number of words in the idea.")
        print ("---------------------------------------------")
        print ("")
        return

    # Loop through all ideas in idea bank
    for line in ideaBank:

        # Format idea
        currentBankedIdea = line.rstrip()
        if (currentBankedIdea == ""):
            continue
        currentBankedIdeaAsList = currentBankedIdea.split(' ')

        # Set current matches
        currentMatches = 0

        # Loop through words in input
        for word in inputIdea:

            # Get length properties
            wordLength = len(word)
            wordLengthMinusOne = wordLength - 1
            wordLengthMinusTwo = wordLength - 2
            wordLengthMinusThree = wordLength - 3

            # Format word
            word = word.lower()
            if ('.' in word):
                word = word[:wordLengthMinusOne]
            if (',' in word):
                word = word[:wordLengthMinusOne]
            if (':' in word):
                word = word[:wordLengthMinusOne]
            if (';' in word):
                word = word[:wordLengthMinusOne]        

            # If a word in the input matches the current idea from the idea bank
            # Then add to current matches
            if (word in currentBankedIdeaAsList):
                currentMatches = currentMatches + 1
            elif ((word + 's') in currentBankedIdeaAsList):
                currentMatches = currentMatches + 1
            elif ((word + 'ed') in currentBankedIdeaAsList):
                currentMatches = currentMatches + 1
            elif ((word + 'ing') in currentBankedIdeaAsList):
                currentMatches = currentMatches + 1   
            else:
                continue
        
            # If threshhold is achieved 
            # Then print the related idea and move to checking the next banked idea    
            if (currentMatches == matchThreshold):
                print (currentBankedIdea)
                break
    
    # Close ideaBank file that was opened in read mode        
    ideaBank.close()            

    # Format output
    print ("---------------------------------------------")
    print ("")

# ------------------------------------ EXECUTION --------------------------------------------

# Get idea and matchThreshold as input
idea = input("Enter idea as a sentence: ")
matchThreshold = input("Enter word match threshold as an integer: ")
matchThreshold = int(matchThreshold)

# Notify bank
print ("")
print ("Banking idea: " + "> " + idea + " <")

# Call bank function
bankIdea(idea)

# Nofity relate
time.sleep(3)
print ("Retrieving banked ideas related to idea: " + "> " + idea + " <")
print ("")
time.sleep(5)

# Call relate function
relateIdea(idea, matchThreshold)

# Notify end
print ("Thank you for submitting your idea to the idea bank and viewing related ideas.")
time.sleep(3)
print ("")