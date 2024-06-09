import numpy as np
import matplotlib.pyplot as plt
from src import wave_convertor as wvc
from src.calculations import *


def draw_plots(Lambda, Lamda_q, Spectr, Radius):
    radius_decay = np.sqrt(Lamda_q * 1e-9 * Radius * (Lamda_q / Spectr - 0.5))
    r_array = np.linspace(0, radius_decay, 1000)

    mono_radius = np.array([intens_mono(wavelenght=Lambda, r=radius, Radial=Radius) for radius in r_array])
    quasi_radius = np.array([intens_quasimono(Lamda_q, Spectr, r=radius, Radial=Radius) for radius in r_array])
    quasi_r = (quasi_radius - min(quasi_radius)) / (max(quasi_radius) - min(quasi_radius))

    figure1, plots = plt.subplots(1, 2, figsize=(14, 7))
    rgb = wvc.color_convertation(Lambda)
    plot1 = plots[0]
    plot2 = plots[1]
    plot1.set_facecolor('black')
    for radius, intensity in zip(r_array, mono_radius):
        circle = plt.Circle((0, 0), radius, edgecolor=rgb, alpha=intensity, fill=False, lw=0.5)
        plot1.add_patch(circle)
    plot1.set_xlim(-radius_decay, radius_decay)
    plot1.set_ylim(-radius_decay, radius_decay)
    plot1.set_title('Монохроматический свет')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(False)
    plot2.set_xlim(-radius_decay, radius_decay)
    plot2.set_ylim(-radius_decay, radius_decay)
    plot2.set_facecolor('black')
    rgb = wvc.color_convertation(Lamda_q)
    for radius, intensity in zip(r_array, quasi_r):
        circle = plt.Circle((0, 0), radius, edgecolor=rgb, alpha=intensity, fill=False, lw=0.5)
        plot2.add_patch(circle)
    plot2.set_title('Квазимонохроматический свет')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(False)
    plt.tight_layout()
    plt.show()

    figure2, plots = plt.subplots(2, 1, figsize=(14, 7))
    plot1 = plots[0]
    plot2 = plots[1]
    plot1.plot(r_array, mono_radius)
    plot1.set_title('Интенсивность в монохроматическом свете')
    plot1.set_xlabel('r, m')
    plot1.set_ylabel('I')
    plot1.grid(True)
    plot2.plot(r_array, quasi_r)
    plot2.set_title('Интенсивность в квазимонохроматическом свете')
    plot2.set_xlabel('r, m')
    plot2.set_ylabel('I')
    plot2.grid(True)
    plt.tight_layout()
    plt.show()
