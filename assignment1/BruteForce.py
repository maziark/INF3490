from csv_example import data
from itertools import permutations
from timeit import default_timer as time
from random import randint as rand
import matplotlib.pyplot as plt

def distance (city_1, city_2):
    return float(data[data[0].index(city_1) + 1][data[0].index(city_2)])

def evalTravel (route):
    travelingTime = 0
    for i in range (1, len(route)):
        travelingTime += distance (route[i-1], route[i])

    return travelingTime


def bruteForceTheProblem (numberOfCities):
    cities = data[0][:numberOfCities]
    routes = list(permutations(cities))

    #print (routes)

    route_best = (routes[0], evalTravel(routes[0]))

    routes.pop(0)

    for route in routes:
        t = evalTravel (route)
        if (t < route_best[1]) : route_best = (route, t)

    return route_best


def swapStuff (route):
    element_1 = 0
    element_2 = 0

    # generates two different elemenets to swap
    while (element_1 == element_2):
        element_1 = rand(0, len(route) - 1)
        element_2 = rand(0, len(route) - 1)

    temp1 = route[element_2]
    route[element_2] = route[element_1]
    route[element_1] = route[element_2]

    return route



def time_bruteForce ():
    x = list (range (2, 11))
    y = []
    for i in x:
        start = time()
        bruteForceTheProblem (i)
        stop = time()

        y.append(stop-start)

    print (x, y)
    plt.plot (x, y)
    plt.show()


#print (bruteForceTheProblem (5))
time_bruteForce()
