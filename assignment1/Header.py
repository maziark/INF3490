from csv_example import data
from itertools import permutations
from timeit import default_timer as time
from random import randint as rand
import matplotlib.pyplot as plt


def distance (city_1, city_2):
    return float(data[data[0].index(city_1) + 1][data[0].index(city_2)])

def evalTravel (path):
    travelingTime = 0
    for i in range (1, len(path)):
        travelingTime += distance (path[i-1], path[i])

    return travelingTime


def swapStuff (path):
    element_1 = 0
    element_2 = 0

    # generates two different elemenets to swap
    while (element_1 == element_2):
        element_1 = rand(0, len(path) - 1)
        element_2 = rand(0, len(path) - 1)

    temp1 = path[element_2]
    path[element_2] = path[element_1]
    path[element_1] = temp1

    return path
