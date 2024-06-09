import numpy as np


def search_normal_frequencies(m, k, L, g=9.82):
    a = g / L - k / m
    b = k / m

    A = np.array([[a, b], [b, a]])

    eigenvalues, eigenvectors = np.linalg.eig(A)

    omega1 = np.sqrt(eigenvalues[0])
    omega2 = np.sqrt(eigenvalues[1])

    return omega1, omega2
