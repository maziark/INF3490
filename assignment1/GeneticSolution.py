from Header import *
from numpy import random

def fitness (path):
    d = float(evalTravel (path))
    
    return 1.0/max(d, 1.0)


def genes (numberOfCities) :
    return data[0][:numberOfCities]

def createPath (cities):
    return random.choice (cities, len(cities), replace = False)


def createPopulation (populationSize, cities) :
    population = [] # (individual, fitness)
    for i in range (populationSize):
        individual = createPath (cities)
        fit = fitness (individual)

        population.append((individual, fit))

    return population

def rankIndividuals (population):
    # Sort based on the fitness value
    #print (population)
    population.sort(key=lambda x : x[1], reverse = True)
    return population


def sumFitness (population):
    l = [x[1] for x in population]
    return sum(l)

def randomSelection (population, eliteSize):
    eliteMembers = population[:eliteSize]
    sizeOfRest = len(population) - eliteSize

    sumFit = sumFitness (population) 

    climate = random.random()

    print (climate, sumFit)

    selection = [x for x in population if x[1]/sumFit > climate]
    
    selection = eliteMembers + selection
   
    return selection

def breed (individual_1, individual_2):

    cut_1 = rand (0, len(individual_1))
    cut_2 = rand(0, len(individual_2))

    startCut = min (cut_1, cut_2)
    endCut = max(cut_1, cut_2)

    child = list(individual_1[startCut:endCut+1])

    # Need more Genes!

    for g in individual_2:
        if (g not in child) : child.append(g)

    return child


def repopulate (population, eliteSize = 0):
    # They will survive!
    elites = population[:eliteSize]
    print ('pop : ', population)
    rest = population [eliteSize:]
    
    print (rest, elites)
    dates = random.choice (list (range(len(rest))), len(rest), replace = False)

    notElites = []
    for i in range (len(rest) - 1):
        child = breed(rest[i][0], rest[i+1][0])
        notElites.append((child, 1000)) # Just some value!

    return elites + notElites

def UV (population):
    paths = [x[0] for x in population]
    cancered = [swapStuff (p) for p in paths]
    print (cancered[0])
    population_new = [(x, fitness(x)) for x in cancered]

    return population_new

def evolution (population, eliteSize=0):
    rankIndividuals (population)
    selection = randomSelection (population, eliteSize)
    pre_UV = repopulate (selection, eliteSize)
    post_UV = UV (pre_UV)
    return post_UV

def playGod (geneVariety, populationSize, eliteSize, iterations):
    DNA = genes(geneVariety)
    population = createPopulation (populationSize, DNA)
    
    #print (population)

    rankIndividuals (population)
    
    for i in range (iterations):
        population = evolution (population, eliteSize)

    #population = rankIndividuals (population)

    print (population[0][0], 1.0/population[0][1])


playGod (5, 20, 3, 100)
