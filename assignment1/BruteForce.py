from Header import *

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



time_bruteForce()
