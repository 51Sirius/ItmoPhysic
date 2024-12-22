import numpy as np
import matplotlib.pyplot as plt
import json

def load_parameters(json_file):
    with open(json_file, 'r') as file:
        return json.load(file)

def get_function_zones(a_alpha, P):
    return np.cos(a_alpha) + P * np.sin(a_alpha) / a_alpha

def plot_kronig_penney(P, a_alpha_range=[-25, 25]):
    a_alpha = np.linspace(*a_alpha_range, 10000)
    y = get_function_zones(a_alpha, P)

    plt.figure(figsize=(10, 6))
    plt.plot(a_alpha, y, label=r'$P = {}$'.format(P), color='r')

    plt.axhline(1, color='k', linestyle='--')
    plt.axhline(-1, color='k', linestyle='--')

    plt.fill_between(a_alpha, 1, -1, where=(np.abs(y) < 1), color='yellow', alpha=0.3, label='Allowed Zones')

    plt.xlabel(r'$a \cdot \alpha$')
    plt.ylabel(r'$\cos(a \cdot \alpha) + P \cdot \frac{\sin(a \cdot \alpha)}{a \cdot \alpha}$')
    plt.title('Graphical Analysis of the Kronig-Penney Equation')
    plt.legend()
    plt.grid(True)
    plt.show()


P_values = [0, 1, 10, 100, 1000]

for P in P_values:
    plot_kronig_penney(P)