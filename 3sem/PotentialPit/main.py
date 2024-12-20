import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import eigh
from consts import *


y = []

for i in range(len(x)):
    y.append(-U0 if - a/2 <= x[i] <= a/2 else 0)
k_2max = math.sqrt(2 * m * U0) / hbar
n_max = math.ceil(k_2max * a / constants.pi)
V = np.where(np.abs(x) < a / 2, -U0, 0)

diag = hbar**2 / (2 * m * dx**2)

H = np.diag(2 * diag + V) + np.diag(-diag * np.ones(N - 1), k=-1) + np.diag(-diag * np.ones(N - 1), k=1)

self_state, self_vecs = eigh(H)
engs = self_state / eV
eng_vecs = self_vecs / np.sqrt(dx)

linked_states_if = engs < 0
linked_eng = engs[linked_states_if]
linked_engvecs = eng_vecs[:, linked_states_if]


plt.figure(figsize=(12, 8))
for i in range (n_max):
    plt.plot(x,linked_engvecs[:, i] / np.max(np.abs(linked_engvecs[:, i])) * 0.3 + linked_eng[i])

plt.plot(x, V / eV, color='black')
plt.xlabel("x, nm")
plt.ylabel("E, eV")
plt.ylim(-U0 / eV - 1, 1)
plt.title("Potential Pit")
plt.legend()
plt.grid()
plt.show()