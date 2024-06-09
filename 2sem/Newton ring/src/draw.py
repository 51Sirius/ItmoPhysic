import numpy as np
import matplotlib.pyplot as plt
from src import wave_convertor as wvc
from src.calculations import *


def draw_plots(Lambda, Lambda_q, Spectr, Radius):
    radius_decay = np.sqrt(Lambda_q * 1e-9 * Radius * (Lambda_q / Spectr - 0.5))
    arr_radius = np.linspace(0, radius_decay, 1000)
    mono_I = []
    quasi_I = []
    for radius in arr_radius:
        mono_I.append(I_mono(Lambda, r=radius, Radial=Radius))
        quasi_I.append(I_quasi(Lambda_q, Spectr, r=radius, Radial=Radius))
    mono_I = np.array(mono_I)
    quasi_I = np.array(quasi_I)
    quasi_I = (quasi_I - min(quasi_I)) / (max(quasi_I) - min(quasi_I))

    figure1, plots = plt.subplots(1, 2, figsize=(10, 5))
    rgb = wvc.color_convertation(Lambda)
    plot1 = plots[0]
    plot2 = plots[1]
    plot1.set_facecolor('black')
    for radius, intensity in zip(arr_radius, mono_I):
        circle = plt.Circle((0, 0), radius, edgecolor=rgb, alpha=intensity, fill=False, lw=0.2)
        plot1.add_patch(circle)
    plot1.set_xlim(-max(arr_radius), max(arr_radius))
    plot1.set_ylim(-max(arr_radius), max(arr_radius))
    plot1.set_title('Монохроматический свет')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(False)
    plot2.set_xlim(-max(arr_radius), max(arr_radius))
    plot2.set_ylim(-max(arr_radius), max(arr_radius))
    plot2.set_facecolor('black')
    rgb = wvc.color_convertation(Lambda_q)
    for radius, intensity in zip(arr_radius, quasi_I):
        circle = plt.Circle((0, 0), radius, edgecolor=rgb, alpha=intensity, fill=False, lw=0.2)
        plot2.add_patch(circle)

    plot2.set_title('Квазимонохроматический свет')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(False)
    plt.tight_layout()
    plt.show()

    figure2, plots = plt.subplots(2, 1, figsize=(10, 5))
    plot1 = plots[0]
    plot2 = plots[1]
    plot1.plot(arr_radius, mono_I)
    plot1.set_title('Интенсивность в монохроматическом свете')
    plot1.set_xlabel('r, m')
    plot1.set_ylabel('I')
    plot1.grid(True)
    plot2.plot(arr_radius, quasi_I)
    plot2.set_title('Интенсивность в квазимонохроматическом свете')
    plot2.set_xlabel('r, m')
    plot2.set_ylabel('I')
    plot2.grid(True)
    plt.tight_layout()
    plt.show()
