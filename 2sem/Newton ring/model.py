import numpy as np
import matplotlib.pyplot as plt
from src import wave_convertor as wvc
from src.consts import *
from src.calculations import *

radius_decay = np.sqrt(LAMBDA_Q * 1e-9 * RADIUS * (LAMBDA_Q / SPECTR - 0.5))
r_array = np.linspace(0, radius_decay, 1000)


def plot_mono_newton_rings(ax, title):
    rgb = wvc.color_convertation(LAMBDA)
    ax.set_facecolor('black')
    for radius, intensity in zip(r_array, I_mono_array_r):
        circle = plt.Circle((0, 0), radius, edgecolor=rgb, alpha=intensity, fill=False, lw=0.5)
        ax.add_patch(circle)
    ax.set_xlim(-radius_decay, radius_decay)
    ax.set_ylim(-radius_decay, radius_decay)
    ax.set_title(title)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(False)


def plot_I_r_mono(ax, title):
    rgb = wvc.color_convertation(LAMBDA)
    ax.plot(r_array, I_mono_array_r, color=rgb)
    ax.set_title(title)
    ax.set_xlabel('r, m')
    ax.set_ylabel('I')
    ax.grid(True)


def plot_quasi_newton_rings(ax, title):
    ax.set_xlim(-radius_decay, radius_decay)
    ax.set_ylim(-radius_decay, radius_decay)
    ax.set_facecolor('black')
    rgb = wvc.color_convertation(LAMBDA_Q)
    for radius, intensity in zip(r_array, I_quasi_norm_r):
        circle = plt.Circle((0, 0), radius, edgecolor=rgb, alpha=intensity, fill=False, lw=0.5)
        ax.add_patch(circle)

    ax.set_title(title)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(False)


def plot_I_r_quasi(ax, title):
    rgb = wvc.color_convertation(LAMBDA_Q)
    ax.plot(r_array, I_quasi_norm_r, color=rgb)
    ax.set_title(title)
    ax.set_xlabel('r, m')
    ax.set_ylabel('I')
    ax.grid(True)


I_mono_array_r = np.array([intens_mono(wavelenght=LAMBDA, r=radius) for radius in r_array])
I_quasi_array_r = np.array(
    [intens_quasimono(LAMBDA_Q, SPECTR, r=radius) for radius in r_array])
I_quasi_norm_r = (I_quasi_array_r - min(I_quasi_array_r)) / (max(I_quasi_array_r) - min(I_quasi_array_r))

figure1, axs = plt.subplots(1, 2, figsize=(14, 7))
plot_mono_newton_rings(axs[0], 'Кольца Ньютона в монохроматическом свете')
plot_quasi_newton_rings(axs[1], 'Кольца Ньютона в квазимонохроматическом свете')
plt.tight_layout()
plt.show()

figure2, axs = plt.subplots(2, 1, figsize=(14, 7))
plot_I_r_mono(axs[0], 'Интенсивность в монохроматическом свете')
plot_I_r_quasi(axs[1], 'Интенсивность в квазимонохроматическом свете')
plt.tight_layout()
plt.show()
