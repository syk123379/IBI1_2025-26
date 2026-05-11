import numpy as np
import matplotlib.pyplot as plt

population = np.zeros((100, 100), dtype=int)

outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

beta = 0.3
gamma = 0.05
time_points = 100

snapshots = {0: population.copy()}

# PSEUDOCODE
# 1. Repeat for each time step:
# 2. Find all currently infected cells.
# 3. Make a copy of the grid so updates happen at the same time.
# 4. For each infected cell:
#    - Check all 8 neighbours.
#    - If a neighbour is inside the grid and susceptible, infect it with probability beta.
#    - Allow the infected cell to recover with probability gamma.
# 5. Replace the old grid with the updated grid.
# 6. Save selected time points for plotting.

for t in range(1, time_points + 1):
    new_population = population.copy()
    infected_points = np.argwhere(population == 1)

    for x, y in infected_points:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue

                nx = x + dx
                ny = y + dy

                if 0 <= nx < 100 and 0 <= ny < 100:
                    if population[nx, ny] == 0:
                        if np.random.random() < beta:
                            new_population[nx, ny] = 1

        if np.random.random() < gamma:
            new_population[x, y] = 2

    population = new_population

    if t % 10 == 0 or t == time_points:
        snapshots[t] = population.copy()

plot_times = sorted(snapshots.keys())

fig, axes = plt.subplots(3, 4, figsize=(12, 9), dpi=150)
axes = axes.flatten()

for i, t in enumerate(plot_times):
    axes[i].imshow(snapshots[t], cmap="viridis", interpolation="nearest", vmin=0, vmax=2)
    axes[i].set_title(f"time = {t}")
    axes[i].set_xticks([])
    axes[i].set_yticks([])

for j in range(len(plot_times), len(axes)):
    axes[j].axis("off")

plt.suptitle("Spatial SIR model")
plt.tight_layout()
plt.show()