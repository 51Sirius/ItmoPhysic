import math
import matplotlib.pyplot as plt
from py_linq import Enumerable
from scipy.optimize import fsolve
import numpy as np
from consts import *



def intersect(x1, x2, y1, y2, eps):
  points = []
  for i in range(len(x1)):

    dist = math.sqrt((x1[i] - x2[i]) ** 2 + (y1[i] - y2[i]) ** 2)
    if dist <= eps:
      points.append((x1[i], y1[i], dist))

  points = Enumerable(points)
  min_dist = points.select(lambda x: x[2]).min()
  min_point = points.where(lambda x: x[2] == min_dist).first()

  return (min_point[0], min_point[1])


xMin = -a - a
xMax = a + a
x = np.arange(xMin, xMax, 1e-12)

y = []

for i in range(len(x)):
    y.append(-U if abs(x[i]) <= a else 0)

plt.plot(x, y)
plt.xlabel("x, м")
plt.ylabel("U(x), Дж")
plt.title("Potential Pit")
plt.legend()
plt.grid()
plt.show()

k_2 = math.sqrt(2 * m * U) / constants.hbar

plt.figure(figsize=(10, 7))

print(f"max k_2: {k_2}")

lefty = np.arange(0, k_2, eps, dtype=float) * a
leftx = np.arange(0, k_2, eps)
n = math.ceil(k_2 * a / constants.pi)

plt.plot(leftx, lefty)

res = []

for i in range(1, n + 1):
    rightx = []
    righty = []
    for j in range(0, int(k_2), eps):
        rightx.append(j)
        righty.append(constants.pi * i - 2 * math.asin((constants.hbar * j) / math.sqrt(2 * constants.electron_mass * U)))

    plt.plot(rightx, righty, color='red')
    point = intersect(leftx, rightx, lefty, righty, eps)
    plt.plot(point[0], point[1],'go', color='orange')
    res.append((point[0], point[1]))


for i in range(len(res)):
    print(f'{res[i][0]:.3f} : {res[i][1]:.3f}')

plt.xlabel("$k_2$")
plt.ylabel(r"$f(k_2)$")
plt.title(r"$k_2a = \pi n - 2\arcsin(\frac{\hbar k_2}{\sqrt{2mU}})$")
plt.legend()
plt.grid()
plt.show()


plt.figure(figsize=(10, 7))
plt.plot(x, y)
energy = [0] * len(res)

def psi(x: float, n: int, scale: float = 1e23) -> float:
    if abs(x) > a:
        return 0
    return math.sqrt(2 / a) * math.sin(constants.pi * (n + 1) * x / (2*a) + (n + 1) * constants.pi / 2) / scale

for i in range(len(res)):
    energy[i] = constants.hbar ** 2 * res[i][0] ** 2 / (2 * m)
    plt.axhline(y=energy[i] - U, linestyle="--", linewidth = 0.5)

    y_psi = []
    x_psi = []
    for j in range(len(x)):
        tmp = psi(x[j], i)
        if tmp != 0:
          y_psi.append(tmp + (energy[i] - U))
          x_psi.append(x[j])

    plt.plot(x_psi, y_psi, color='red')

plt.xlabel("x, м")
plt.ylabel("U(x), Дж")
plt.title("Potential Pit with Energy connect statements")
plt.legend()
plt.grid()
plt.show()
for i in energy:
    print(f'{i:.3e}', end = " ")