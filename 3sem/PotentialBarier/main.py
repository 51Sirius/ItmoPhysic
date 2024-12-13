import math
import json
import numpy as np
import matplotlib.pyplot as plt
from constants import *


hbar = 1.0545718e-34

def sum_integral(integrand, x_values):
    integrand = np.array(integrand)
    x_values = np.array(x_values)
    widths = np.diff(x_values)
    total_area = np.sum(integrand[:-1] * widths)

    return total_area


def load_potential(potential_file, analytic_expression=None, x_count=1000, h=1e-9):
    potential_data = []
    with open(potential_file, "r") as f:
        lines = f.readlines()
        for line in lines:
            x, u = map(float, line.split())
            potential_data.append((x, u))
    if not potential_data and analytic_expression:
        x_values = np.linspace(0, h, x_count)
        potential_data = [(x, analytic_expression(x)) for x in x_values]
    return np.array(potential_data)

def tunneling_probability(m, E, potential):
    x, U = potential[:, 0], potential[:, 1]

    forbidden_region = U > E
    if not np.any(forbidden_region):
        return 1.0
    
    x_forbidden = x[forbidden_region]
    U_forbidden = U[forbidden_region]
    integrand = np.sqrt(2 * m * (U_forbidden - E)) / hbar
    integral = sum_integral(integrand, x_forbidden)
    return np.exp(-2 * integral)


if __name__ == "__main__":
    analytic_expr = eval("lambda x: " + ANAL_POT)

    potential = load_potential("potential.txt", analytic_expression=analytic_expr, x_count=X_COUNT, h=BARIER_RANGE)

    probability = tunneling_probability(MASS, ENERGY, potential)

    plt.plot(potential[:, 0], potential[:, 1], label="Potential U(x)")
    plt.axhline(ENERGY, color="red", linestyle="--", label="Energy E")
    plt.xlabel("x")
    plt.ylabel("U(x)")
    plt.title("Potential Barrier and Energy Level")
    plt.legend()
    plt.grid()
    plt.show()
    print(f"Tunneling probability: {probability}")