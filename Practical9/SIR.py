import numpy as np
import matplotlib.pyplot as plt

N = 10000
S = N - 1
I = 1
R = 0

beta = 0.3
gamma = 0.05
time_points = 1000

S_history = [S]
I_history = [I]
R_history = [R]

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

    S_history.append(S)
    I_history.append(I)
    R_history.append(R)

plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S_history, label="susceptible")
plt.plot(I_history, label="infected")
plt.plot(R_history, label="recovered")
plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model")
plt.legend()
plt.tight_layout()
plt.show()