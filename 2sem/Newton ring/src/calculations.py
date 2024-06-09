from numpy import *


def intens_mono(wavelenght, r, Radial):
    return (cos(2 * (pi * r ** 2) / (Radial * wavelenght * 1e-9) + pi) + 1) / 2


def intens_quasimono(wavelenght, spectrum_width, r, Radial, T_cf=0.999, R_cf=0.001):
    wl_loc = wavelenght * 1e-9
    delta_wl_loc = spectrum_width * 1e-9
    return R_cf * (T_cf ** 2 + 1 + 2 * T_cf * sinc((pi * delta_wl_loc * r ** 2) / (wl_loc ** 2 * Radial)) *
                   cos(2 * pi * r ** 2 / (wl_loc * Radial)))
