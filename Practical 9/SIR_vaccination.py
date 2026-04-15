import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def SIR_vaccination_model(N, I0, R0, vaccination_rate, beta, gamma, t):
    V0 = int(N * vaccination_rate)
    S0 = N - I0 - R0 - V0
    
    S = np.zeros(t)
    I = np.zeros(t)
    R = np.zeros(t)
    V = np.zeros(t) 

    S[0] = S0
    I[0] = I0   
    R[0] = R0
    V[0] = V0

    for i in range (1,t):
        current_S = int(S[i-1])
        current_I = int(I[i-1])
        current_R = int(R[i-1])
        infection_prob = beta * (current_I / N)
    
        new_infections = np.random.binomial(current_S, infection_prob)
        new_recoveries = np.random.binomial(current_I, gamma)
    
        S[i] = current_S - new_infections
        I[i] = current_I + new_infections - new_recoveries
        R[i] = current_R + new_recoveries
    
    return I

vaccine_ratios = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5,0.6, 0.7, 0.8, 0.9]
colors = [cm.viridis(i*80) for i in range(len(vaccine_ratios))]

plt.figure(figsize=(8,5), dpi=150)

for v_rate in vaccine_ratios:
    infected = SIR_vaccination_model(10000, 1, 0, v_rate, 0.3, 0.05, 1000)
    plt.plot(infected, label=str(int(v_rate*100)) + "% vaccine")

plt.title('SIR Model with Vaccination')
plt.xlabel('Time')
plt.ylabel('Infected people')
plt.legend()
plt.grid(alpha=0.3)
plt.show()