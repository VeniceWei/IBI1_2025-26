import numpy as np
import matplotlib.pyplot as plt

population = np.zeros((100, 100), dtype=int)

x, y = np.random.choice(range(100), 2)  # Randomly select a position for the initial infected individual
population[x,y] = 1  # Infected individual at position (x, y)

plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')

beta = 0.3   
gamma = 0.1  
time_steps = 200  

def neighbours(x,y):
    return [(i,j) for i in range(x-1, x+2) 
                  for j in range(y-1, y+2) 
                  if (0 <= i < 100 and 0 <= j < 100 and (i != x or j != y))]

for t in range(time_steps):
    new_infections = []
    infected_points = np.where(population == 1)
    for i, j in zip(infected_points[0], infected_points[1]):
                for ni, nj in neighbours(i, j):
                    if population[ni, nj] == 0 and np.random.rand() < beta:  # Infection occurs
                        new_infections.append((ni, nj))
                if np.random.rand() < gamma:  # Recovery occurs
                    population[i,j] = 2  # Mark as recovered

    for ni, nj in new_infections:
        population[ni, nj] = 1  # Mark new infections

    if t % 10 == 0:
            plt.clf()
            plt.imshow(population, cmap="viridis")
            plt.title(f"Step {t}")
            plt.pause(0.2)

plt.show()

