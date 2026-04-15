import numpy as np
import matplotlib.pyplot as plt
# set up model parameters
beta = 0.3
gamma = 0.05
time_points = 100

population = np.zeros((100,100))
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

# plot the initial condition
plt.figure(figsize=(6,4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title("Time 0")
plt.show()

# Create a copy of the current population grid to store new state
# Find all infected points in the grid
# For each infected point:
#    Check all 8 neighbours
#    If neighbour is inside grid and can get infected:
#       Infect the neighbor with probability beta
#    Recover the infected cell with probability gamma
# Update the grid to the new state
# Plot the grid every 10 time points to demonstrate the infection spread
for t in range(time_points+1):
    new_population = population.copy()
    infect_x, infect_y = np.where(population == 1) # to find the infected points

    # address the neighbours
    for i in range(len(infect_x)):
        x = infect_x[i]
        y = infect_y[i]

        neighbours = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)] # infect 8 neighbours
        for dx, dy in neighbours:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < 100 and 0 <= ny < 100:
                if population[nx, ny] == 0:
                    if np.random.random() < beta:
                        new_population[nx, ny] = 1

        if np.random.random() < gamma:
            new_population[x, y] = 2

    # update the population
    population = new_population

    # update the plot every 10 time points
    if t % 10 == 0:
        plt.imshow(population, cmap="viridis", interpolation="nearest")
        plt.title(f"Time {t}")
        plt.show()