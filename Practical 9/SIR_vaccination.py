import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import cm
plt.figure(figsize=(6,4),dpi=150)
vaccination = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
N = 10000
beta = 0.3
gamma = 0.05
for j in vaccination:
    vaccinated = int(N*j)
    Susceptible = N - vaccinated - 1
    Infected = 1
    Recovered = 0
    S_array = [Susceptible]
    I_array = [Infected]
    R_array = [Recovered]
    for i in range(1000):
        recovery = np.random.choice(range(2),Infected,p=[1-gamma,gamma]).sum()
        S_I = np.random.choice(range(2),Susceptible,p=[1-beta*Infected/N,beta*Infected/N]).sum()
        Susceptible = Susceptible - S_I
        Infected = Infected + S_I - recovery
        Recovered = Recovered + recovery
        S_array.append(Susceptible)
        I_array.append(Infected)
        R_array.append(Recovered)
    plt.plot(I_array,label=f'{j}')
plt.plot([0]*1000,label="1")
plt.title("SIR model with different vaccination rates")
plt.xlabel("time")
plt.ylabel("number of people")
plt.legend()
plt.show()