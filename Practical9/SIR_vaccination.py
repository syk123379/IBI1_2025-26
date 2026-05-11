import numpy as np
import matplotlib.pyplot as plt

N = 10000
beta = 0.3
gamma = 0.05
time_points = 1000

vaccination_rates = range(0, 101, 10)

plt.figure(figsize=(6, 4), dpi=150)

for rate in vaccination_rates:
    vaccinated = int((N - 1) * rate / 100)
    S = N - 1 - vaccinated
    I = 1
    R = 0

    infected_history = [I]

    for _ in range(time_points):
        infection_prob = beta * I / N
        infection_prob = min(infection_prob, 1)

        if S > 0:
            new_infections = np.random.choice([0, 1], size=S, p=[1 - infection_prob, infection_prob]).sum()
        else:
            new_infections = 0

        if I > 0:
            new_recoveries = np.random.choice([0, 1], size=I, p=[1 - gamma, gamma]).sum()
        else:
            new_recoveries = 0

        S = S - new_infections
        I = I + new_infections - new_recoveries
        R = R + new_recoveries

        infected_history.append(I)

    plt.plot(infected_history, label=f"{rate}%")

plt.xlabel("time")
plt.ylabel("number of infected people")
plt.title("SIR model with different vaccination rates")
plt.legend()
plt.tight_layout()
plt.show()