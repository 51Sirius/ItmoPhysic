from numpy import *
from src.consts import *


def intens_mono(wavelenght, r):
    return cos((pi * r ** 2) / (RADIUS * wavelenght * 1e-9) + pi / 2) ** 2


def intens_quasimono(wavelenght, spectrum_width, r, T_cf=0.999, R_cf=0.001):
    wl_loc = wavelenght * 1e-9
    delta_wl_loc = spectrum_width * 1e-9
    return R_cf * (T_cf ** 2 + 1 + 2 * T_cf * sinc((pi * delta_wl_loc * r ** 2) / (wl_loc ** 2 * RADIUS)) *
                   cos(2 * pi * r ** 2 / (wl_loc * RADIUS)))