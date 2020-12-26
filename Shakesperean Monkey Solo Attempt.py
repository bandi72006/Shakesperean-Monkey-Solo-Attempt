#Bandar Al Aish
#To do list:
#Calculate fitness
#Reproduction and mutation

import random
import string
phrase = "To be or not to be that is the question"
chars = list(string.printable)
generation = []

#n = number of species
def runGeneration(n):
    for i in range(n):
        currentPhrase = []
        for i in range(len(phrase)):
            currentPhrase.append(random.choice(chars))

        currentPhrase = "".join(currentPhrase)
        generation.append(currentPhrase)

    #print(currentPhrase)

runGeneration(100)

def calcFitness():
    for member in generation:
        for i in range(len(member)):
            fitness = 0
            if (str(member[i]) == (phrase[i])):
                print(member[i] + "  " + phrase[i])
                fitness = fitness + 1
        

calcFitness()
        
    


