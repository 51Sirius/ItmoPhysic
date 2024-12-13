from main import tunneling_probability
import numpy as np


hbar = 1.0545718e-34

def test_tunneling():
    m = 9.11e-31
    E = 1.5e-19
    U0 = 2.0e-19
    a = 1.0e-11
    x_count = 1000

    def analytic_probability():
        k = np.sqrt(2 * m * (U0 - E)) / hbar
        return 1 / (1 + (U0**2) / (4 * E * (U0 - E)) * np.sinh(k * a)**2)

    def rectangular_barrier(x):
        return U0 if 0 <= x <= a else 0

    x_values = np.linspace(-a, 2 * a, x_count)
    potential_data = [(x, rectangular_barrier(x)) for x in x_values]
    potential = np.array(potential_data)

    numerical_prob = tunneling_probability(m, E, potential)

    analytic_prob = analytic_probability()
    print(f"Numerical tunneling probability: {numerical_prob:.5e}")
    print(f"Analytic tunneling probability:  {analytic_prob:.5e}")

test_tunneling()