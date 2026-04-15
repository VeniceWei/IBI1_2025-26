import numpy as np
import matplotlib.pyplot as plt

def SIR_model(N, S0, I0, R0, beta, gamma, t):
    S = np.zeros(t)
    I = np.zeros(t)
    R = np.zeros(t)

    S[0] = S0
    I[0] = I0   
    R[0] = R0

    for i in range (1,t):
        current_S = int(S[i-1])
        current_I = int(I[i-1])
        current_R = int(R[i-1])
        infection_prob = beta * (current_I / N)
    
        new_infections = np.sum(np.random.choice([0, 1], current_S, p=[1 - infection_prob, infection_prob]))
        new_recoveries = np.sum(np.random.choice([0, 1], current_I, p=[1 - gamma, gamma]))
    
        S[i] = current_S - new_infections
        I[i] = current_I + new_infections - new_recoveries
        R[i] = current_R + new_recoveries
    
    plt.figure(figsize=(6, 4), dpi=150)
    plt.plot(S, label='Susceptible', color='orange')
    plt.plot(I, label='Infected', color='red')
    plt.plot(R, label='Recovered', color='blue')
    plt.title('SIR Model')
    plt.xlabel('Time (days)')
    plt.ylabel('Number of individuals')
    plt.legend()
    plt.show() 
    
    return S, I, R
 
SIR_model(N=10000, S0=9999, I0=1, R0=0, beta=0.3, gamma=0.05, t=100)