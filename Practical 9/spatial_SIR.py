# import necessary libraries
import numpy as np 
import matplotlib.pyplot as plt
# 1. Create 100x100 grid of susceptible (0)
# 2. Pick one random cell, set to infected (1)
# 3. FOR each of 100 time steps:
#    a. Find all infected cells
#    b. FOR each infected cell:
#       - For each of its 8 neighbours:
#            if neighbour is susceptible (0):
#                infect it with probability beta
#       - The infected cell recovers (2) with probability gamma
#    c. Every 10 steps (and at final step), plot a heatmap
# make array of all susceptible population
population = np.zeros((100,100))
# choose one random point in array for where the outbreak happens
outbreak = np.random.choice(range(100),2)
#change status for 0 to 1
population[outbreak[0],outbreak[1]] = 1
# set up model parameters
beta = 0.3
gamma = 0.05
plt.figure(figsize=(6,4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title("Time 0")
plt.show()
# loop through 100 time points
for j in range(100):
    # find infected points
    infectedIndex = np.where(population==1)
    # loop through all infected points
    for i in range(len(infectedIndex[0])):
        # get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        # infect each neighbour with probability beta
        # infect all 8 neighbours (this is a bit finicky, is there a better way?):
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                # don't infect yourself! (Is this strictly necessary?)
                if (xNeighbour,yNeighbour) != (x,y):
                    # make sure I don't fall off an edge
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                        # only infect neighbours that are not already infected!
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
        # an infected individual can recover at rate gamma
        population[x, y] = np.random.choice([2, 1], p=[gamma, 1 - gamma])
    # a heat map for each time point
    if j % 10 == 0 or j == 99:
        # plot
        plt.figure(figsize=(6,4),dpi=150)
        plt.imshow(population,cmap="viridis",interpolation="nearest")
        plt.show()