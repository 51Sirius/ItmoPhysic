import numpy as np


def search_normal_frequencies(g, m, k, L):
    # Матрица коэффициентов
    a = g / L - k / (4*m)
    b = k / (m * 4)

    A = np.array([[a, b], [b, a]])

    # Поиск собственных значений (квадраты нормальных частот)
    eigenvalues, eigenvectors = np.linalg.eig(A)

    # Нормальные частоты
    omega1 = np.sqrt(eigenvalues[0])
    omega2 = np.sqrt(eigenvalues[1])

    print(f'Нормальные частоты: ω1 = {omega1:.4f}, ω2 = {omega2:.4f}')
