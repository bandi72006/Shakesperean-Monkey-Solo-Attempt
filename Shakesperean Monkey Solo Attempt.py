#Bandar Al Aish || bandi72006

#To do list:
#Fix bugs (no reproduction/changes occuring)!
#Mutation
#COMMENT CODE SO ITS EASIER TO READ


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

#Define crucial variables that stores the generations data
generation = []
fitnessScores = []
selections = []

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


def calcFitness():

    #calculates individual fitness
    for member in generation:
        fitness = 0
        for i in range(len(member)):
            if (str(member[i]) == (phrase[i])):
                fitness = fitness + 1
        fitnessScores.append(fitness)
    

def selection():

    for i in range(0, len(generation), 2):
        if (fitnessScores[i] >= fitnessScores[i+1]):
            selections.append(generation[i])
        else:
            selections.append(generation[i+1])


def reproduce():

    matingPool = []
    memberCount = 0
    generation = []

    for i in range(0,len(selections),2):
        #Adds 2 members at a time to the mating pool        
        matingPool.append(selections[i])
        matingPool.append(selections[i+1])
        
        #crossover

        crossoverPoint = random.randint(0,len(matingPool[0]))
        parent1 = list(matingPool[0])
        parent2 = list(matingPool[1])

        #Creates children by join first part of parent and second part of other parent
        child1 = "".join(parent1[:crossoverPoint] + parent2[crossoverPoint:])
        child2 = "".join(parent2[:crossoverPoint] + parent1[crossoverPoint:])
        
        generation.append(child1)
        generation.append(child2)

        #clears mating pool for next "pair" of members
        matingPool = []
    
    
    children = []
    for i in range(10):
        print(str(i) + ":     " + generation[i] + "      fitness:    " + str(fitnessScores[i]))

    print("\n\n\n\n")
    


def isPhraseTyped():
    for member in generation:
        if member == phrase:
            return True
            break


createGeneration(100)


while True:
    calcFitness()
    selection()
    reproduce()
    if isPhraseTyped == True:
        break

        