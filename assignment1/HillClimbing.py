from Header import *

def hillClimber (path, numberOfIterations, temperature = 0.10):
    path_old = path.copy()
    distance_old = evalTravel (path_old)
    for i in range (numberOfIterations):
        path_new = path_old.copy()
        path_new = swapStuff (path_new)
        distance_new = evalTravel (path_new)
        #print (distance_old)
        
        if ((distance_old - distance_new)/distance_old > temperature):
            path_old = path_new
            distance_old = distance_new

        """if (distance_new < distance_old) : 
            path_old = path_new
            distance_old = distance_new"""
    print (path_old, distance_old, '\n\n\n')
    return (path_old, distance_old)



def time_hillClimber():
    x = list( range(2, 24))
    y = []
    for i in x:
        start = time()
        initial_path = data[0][:i].copy()
        print (initial_path)
        hillClimber (initial_path, 1000)
        stop = time()

        y.append(stop - start)

    print (x, y)
    plt.plot(x, y)
    plt.show()


time_hillClimber()

