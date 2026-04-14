import numpy as np
import matplotlib.pyplot as plt

# define the basic variables of the model
N = 10000  
beta = 0.3
gamma = 0.05
time_points = 1000
S = 9999
I = 1
R = 0
S_list = [S]
I_list = [I]
R_list = [R]

#Time loop---For each time step:
#  Calculate infection probability = beta × (I / N)
#  Randomly select new infected people from susceptible group
#  Reduce the number of susceptible people
#  Randomly select new recovered people from infected group
#  Reduce the number of infected people
#  Increase the number of recovered people
#  Update S, I, R values
#  Append new values to tracking lists
for i in range(time_points):
    infect_prob = beta * (I / N)
    new_infect = 0
    for person in range(S):
        if np.random.random() < infect_prob:
            new_infect += 1
    new_recover = 0
    for person in range(I):
        if np.random.random() < gamma:
            new_recover += 1

    S = S - new_infect
    I = I + new_infect - new_recover
    R = R + new_recover

    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

# plot
plt.figure(figsize = (6,4), dpi = 150)
plt.plot(S_list, label="susceptible")
plt.plot(I_list, label="infected")
plt.plot(R_list, label="recovered")
plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR Model")
plt.legend()
plt.savefig("SIR.png")
plt.show()