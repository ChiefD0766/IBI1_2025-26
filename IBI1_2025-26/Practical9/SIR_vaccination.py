import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# define the basic variables of the model
N = 10000  
beta = 0.3
gamma = 0.05
time_points = 1000

# set different vaccine rates
vaccine_rates = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
curves = []
for r in vaccine_rates:
    V = int(N * r)
    S = N - V - 1
    I = 1
    R = 0
    I_list = [I]

    for t in range(time_points):
        S = max(S, 0)
        I = max(I, 0)
        if S == 0:
            new_infect = 0
        else:
            new_infect = np.random.binomial(n=S, p=beta * (I / N))
        
        if I == 0:
            new_recover = 0
        else:
            new_recover = np.random.binomial(n=I, p=gamma)
        S = max(S - new_infect, 0)
        I = max(I + new_infect - new_recover, 0)
        R = min(R + new_recover, N)
        I_list.append(I)
    curves.append(I_list)

# plot
plt.figure(figsize = (6,4), dpi = 150)
for i in range(len(vaccine_rates)):
    plt.plot(curves[i], label=f"{int(vaccine_rates[i]*100)}%", color = cm.viridis(60))
plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR Model with different vaccination rates")
plt.legend(loc="upper right")
plt.savefig("C:\\cygwin64\\home\\26838\\IBI\\IBI_25-26\\IBI1_2025-26\\Practical9")
plt.savefig("SIR_vaccination.png")
plt.show()