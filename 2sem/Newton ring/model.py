import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Параметры
R = 10  # Радиус линзы в мм
wavelength_mono = 550  # Длина волны монохроматического света в нм
wavelength_center = 550  # Центральная длина волны для квазимонохроматического света в нм
wavelength_width = 20  # Ширина спектра для квазимонохроматического света в нм

# Функция для расчета интенсивности для монохроматического света
def intensity_mono(r, R, wavelength):
    t = (r**2) / (2 * R)
    delta = 2 * t
    return np.cos(np.pi * delta / wavelength)**2

# Функция для расчета интенсивности для квазимонохроматического света
def intensity_quasi(r, R, wavelength_center, wavelength_width):
    def integrand(wavelength):
        t = (r**2) / (2 * R)
        delta = 2 * t
        return np.cos(np.pi * delta / wavelength)**2
    result, _ = quad(integrand, wavelength_center - wavelength_width / 2, wavelength_center + wavelength_width / 2)
    return result / wavelength_width

# Радиальные координаты
radii = np.linspace(0, 5, 500)  # Радиусы в мм

# Рассчет интенсивности
intensity_mono_values = [intensity_mono(r, R, wavelength_mono) for r in radii]
intensity_quasi_values = [intensity_quasi(r, R, wavelength_center, wavelength_width) for r in radii]

# График зависимости интенсивности от радиальной координаты
plt.figure(figsize=(12, 6))
plt.plot(radii, intensity_mono_values, label='Монохроматический свет', color='blue')
plt.plot(radii, intensity_quasi_values, label='Квазимонохроматический свет', color='green')
plt.xlabel('Радиальная координата (мм)')
plt.ylabel('Интенсивность')
plt.title('Зависимость интенсивности от радиальной координаты')
plt.legend()
plt.grid(True)
plt.show()

# Визуализация цветного распределения
X, Y = np.meshgrid(radii, radii)
Z_mono = np.array([intensity_mono(np.sqrt(x**2 + y**2), R, wavelength_mono) for x, y in zip(X.flatten(), Y.flatten())]).reshape(X.shape)
Z_quasi = np.array([intensity_quasi(np.sqrt(x**2 + y**2), R, wavelength_center, wavelength_width) for x, y in zip(X.flatten(), Y.flatten())]).reshape(X.shape)

fig, ax = plt.subplots(1, 2, figsize=(14, 6))

cax1 = ax[0].imshow(Z_mono, extent=(0, 5, 0, 5), origin='lower', cmap='inferno')
ax[0].set_title('Монохроматический свет')
fig.colorbar(cax1, ax=ax[0])

cax2 = ax[1].imshow(Z_quasi, extent=(0, 5, 0, 5), origin='lower', cmap='inferno')
ax[1].set_title('Квазимонохроматический свет')
fig.colorbar(cax2, ax=ax[1])

plt.show()
