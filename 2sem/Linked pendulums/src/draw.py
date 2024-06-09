import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def equations(t, y, m, g, L, k, beta):
    phi1, dphi1_dt, phi2, dphi2_dt = y
    d2phi1_dt2 = (-g / L) * np.sin(phi1) - (beta / (m * L)) * dphi1_dt + (k / (m * L)) * (phi1 - phi2)
    d2phi2_dt2 = (-g / L) * np.sin(phi2) - (beta / (m * L)) * dphi2_dt + (k / (m * L)) * (phi2 - phi1)
    return [dphi1_dt, d2phi1_dt2, dphi2_dt, d2phi2_dt2]


def draw_plots(m, k, L, phi_zero1, phi_zero2, L1, time_start, time_end, beta, g=9.8):
    dt = round((time_end - time_start) / 100, 2)
    t_values = np.arange(time_start, time_end, dt)

    y0 = [phi_zero1, 0, phi_zero2, 0]
    sol = solve_ivp(equations, [time_start, time_end], y0, t_eval=t_values, args=(m, g, L, k, beta))

    phi1_values = sol.y[0]
    dphi1_dt_values = sol.y[1]
    phi2_values = sol.y[2]
    dphi2_dt_values = sol.y[3]

    plt.figure(figsize=(12, 12))

    plt.subplot(2, 2, 1)
    plt.plot(t_values, phi1_values, 'r', label='Первый маятник')
    plt.title('Угол отклонения первого маятника')
    plt.xlabel('Время (с)')
    plt.ylabel('Угол отклонения (рад)')
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 2, 2)
    plt.plot(t_values, dphi1_dt_values, 'r', label='Первый маятник')
    plt.title('Угловая скорость первого маятника')
    plt.xlabel('Время (с)')
    plt.ylabel('Угловая скорость (рад/с)')
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 2, 3)
    plt.plot(t_values, phi2_values, 'b', label='Второй маятник')
    plt.title('Угол отклонения второго маятника')
    plt.xlabel('Время (с)')
    plt.ylabel('Угол отклонения (рад)')
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 2, 4)
    plt.plot(t_values, dphi2_dt_values, 'b', label='Второй маятник')
    plt.title('Угловая скорость второго маятника')
    plt.xlabel('Время (с)')
    plt.ylabel('Угловая скорость (рад/с)')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()
