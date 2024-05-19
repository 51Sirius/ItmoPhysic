import numpy as np


def search_normal_frequencies(g, m, k, L, L1):
    # Матрица коэффициентов
    a = g / L + k / L1
    b = -k / L1

    A = np.array([[a, b], [b, a]])

    # Поиск собственных значений (квадраты нормальных частот)
    eigenvalues, eigenvectors = np.linalg.eig(A)

    # Нормальные частоты
    omega1 = np.sqrt(eigenvalues[0])
    omega2 = np.sqrt(eigenvalues[1])

    print(f'Нормальные частоты: ω1 = {omega1:.4f}, ω2 = {omega2:.4f}')
