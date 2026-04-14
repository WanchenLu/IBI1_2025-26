import numpy as np 
import matplotlib.pyplot as plt 
Susceptible = 9999
Infected = 1
Recovered = 0
N = 10000
beta = 0.3
gamma = 0.05
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
plt.figure(figsize=(6,4),dpi=150)
plt.title("SIR model")
plt.xlabel("time")
plt.ylabel("number of people")
plt.plot(S_array,label="susceptible")
plt.plot(I_array,label="infected")
plt.plot(R_array,label="recovered")
plt.legend()
plt.savefig("SIR.png")