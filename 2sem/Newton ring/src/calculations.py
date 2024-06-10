from numpy import *


def I_mono(Lambda, radius, Radius):
    return (cos(2 * (pi * radius ** 2) / (Radius * Lambda * 1e-9) + pi) + 1) / 2


def I_quasi(Lambda, spec, radius, Radius):
    return 0.001 * (0.999 ** 2 + 1 + 2 * 0.999 * sinc(
        (pi * (spec * 1e-9) * radius ** 2) / ((Lambda * 1e-9) ** 2 * Radius) + pi / 2) *
                    cos(2 * pi * radius ** 2 / (Lambda * 1e-9 * Radius) + pi / 2))