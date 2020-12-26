#Bandar Al Aish
#To do list:
#Calculate fitness
#Reproduction and mutation

import random
import string
phrase = "To be or not to be that is the question"
chars = list(string.printable)

#removes unnecessary characters
chars.remove("\r")
chars.remove("\n")
chars.remove("\t")
chars.remove("\x0b")
chars.remove("\x0c")

print(chars)
generation = []

print("===============================\n Running code \n===============================")


#n = number of species
def createGeneration(n):
    for i in range(n):
        currentPhrase = []
        for i in range(len(phrase)):
            currentPhrase.append(random.choice(chars))

        currentPhrase = "".join(currentPhrase)
        generation.append(currentPhrase)

    #Prints out every member in generation. Optional and it saves time

    #memberCount = 0
    #for member in generation:
    #    print(str(memberCount) + ". " + member)
    #    memberCount += 1

createGeneration(100)

def calcFitness():

    #Every member has a corresponding fitness rank at the same index
    fitnessRank = []

    #calculates individual fitness
    for member in generation:
        fitness = 0
        for i in range(len(member)):
            if (str(member[i]) == (phrase[i])):
                fitness = fitness + 1
        fitnessRank.append(fitness)
    
    for i in range(len(generation)):
        print(generation[i] + " " + str(fitnessRank[i]))
        

calcFitness()