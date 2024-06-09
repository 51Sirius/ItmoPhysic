import numpy as np
import matplotlib.pyplot as plt
from src import wave_convertor as wvc
from src.consts import *
from src.calculations import *

radius_decay = np.sqrt(LAMBDA_Q * 1e-9 * RADIUS * (LAMBDA_Q / SPECTR - 0.5))
r_array = np.linspace(0, radius_decay, 1000)

I_mono_array_r = np.array([intens_mono(wavelenght=LAMBDA, r=radius) for radius in r_array])
I_quasi_array_r = np.array([intens_quasimono(LAMBDA_Q, SPECTR, r=radius) for radius in r_array])
I_quasi_norm_r = (I_quasi_array_r - min(I_quasi_array_r)) / (max(I_quasi_array_r) - min(I_quasi_array_r))

figure1, axs = plt.subplots(1, 2, figsize=(14, 7))
rgb = wvc.color_convertation(LAMBDA)
axs[0].set_facecolor('black')
for radius, intensity in zip(r_array, I_mono_array_r):
    circle = plt.Circle((0, 0), radius, edgecolor=rgb, alpha=intensity, fill=False, lw=0.5)
    axs[0].add_patch(circle)
axs[0].set_xlim(-radius_decay, radius_decay)
axs[0].set_ylim(-radius_decay, radius_decay)
axs[0].set_title('Кольца Ньютона в монохроматическом свете')
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(False)
axs[1].set_xlim(-radius_decay, radius_decay)
axs[1].set_ylim(-radius_decay, radius_decay)
axs[1].set_facecolor('black')
rgb = wvc.color_convertation(LAMBDA_Q)
for radius, intensity in zip(r_array, I_quasi_norm_r):
    circle = plt.Circle((0, 0), radius, edgecolor=rgb, alpha=intensity, fill=False, lw=0.5)
    axs[1].add_patch(circle)

axs[1].set_title('Кольца Ньютона в квазимонохроматическом свете')
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(False)
plt.tight_layout()
plt.show()

figure2, axs = plt.subplots(2, 1, figsize=(14, 7))
axs[0].plot(r_array, I_mono_array_r)
axs[0].set_title('Интенсивность в монохроматическом свете')
axs[0].set_xlabel('r, m')
axs[0].set_ylabel('I')
axs[0].grid(True)
axs[1].plot(r_array, I_quasi_norm_r)
axs[1].set_title('Интенсивность в квазимонохроматическом свете')
axs[1].set_xlabel('r, m')
axs[1].set_ylabel('I')
axs[1].grid(True)
plt.tight_layout()
plt.show()
