import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from src import *


def E(q, r0, x, y):
    den = ((x - r0[0]) ** 2 + (y - r0[1]) ** 2) ** 1.5
    return q * (x - r0[0]) / den, q * (y - r0[1]) / den


def V(q, r0, x, y):
    return q / np.sqrt((x - r0[0]) ** 2 + (y - r0[1]) ** 2)


def draw_capacitors(d):
    nx, ny = 128, 128
    x = np.linspace(-5, 5, nx)
    y = np.linspace(-5, 5, ny)
    X, Y = np.meshgrid(x, y)
    nq, d = 20, d
    charges = []
    for i in range(nq):
        charges.append((1, (i / (nq - 1) * 2 - 1, -d / 2)))
        charges.append((-1, (i / (nq - 1) * 2 - 1, d / 2)))

    Ex, Ey = np.zeros((ny, nx)), np.zeros((ny, nx))
    for charge in charges:
        ex, ey = E(*charge, x=X, y=Y)
        Ex += ex
        Ey += ey

    V_total = np.zeros_like(X)
    for charge in charges:
        V_total += V(*charge, x=X, y=Y)

    fig = plt.figure(figsize=(WIDTH / DPI, HEIGHT / DPI), facecolor='k')
    ax = fig.add_subplot(facecolor='k')
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)

    color = np.log(np.sqrt(Ex ** 2 + Ey ** 2))
    ax.streamplot(x, y, Ex, Ey, color=color, linewidth=1, cmap=plt.cm.plasma,
                  density=2, arrowstyle='->')

    charge_colors = {True: '#aa0000', False: '#0000aa'}
    for q, pos in charges:
        ax.add_artist(Circle(pos, 0.05, color=charge_colors[q > 0], zorder=10))

    contour = plt.contour(X, Y, V_total, colors='green', levels=15, linewidths=1)

    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_aspect('equal')

    plt.savefig('capacitor_with_equipotential.png', dpi=DPI)
    plt.show()
