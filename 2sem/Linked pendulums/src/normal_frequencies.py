import numpy as np


def search_normal_frequencies(g, m, k, L):
    a = g / L - k / m
    b = k / m

    A = np.array([[a, b], [b, a]])

    eigenvalues, eigenvectors = np.linalg.eig(A)

    omega1 = np.sqrt(eigenvalues[0])
    omega2 = np.sqrt(eigenvalues[1])

    print(f'Нормальные частоты: ω1 = {omega1:.4f} гц, ω2 = {omega2:.4f} гц')