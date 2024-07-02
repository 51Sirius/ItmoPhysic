from Simulation import *


def bounce(m, n):
    V1 = 0
    V2 = 1.0
    count = 0
    while V2 > V1:
        V3 = (m - n) / (m + n) * V1 + (2 * n) / (m + n) * V2
        V2 = (2 * m) / (m + n) * V1 + (n - m) / (m + n) * V2
        if 0 >= V3 > V2:
            count += 1
            break
        V1 = -V3
        count += 2

    return count


if __name__ == "__main__":
    for i in [pow(100, x) for x in range(5)]:
        simulation(i, 1)
