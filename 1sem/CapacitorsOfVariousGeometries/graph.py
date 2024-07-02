import numpy as np
import matplotlib.pyplot as plt
import VariableCapacitor as v


def create_graph_pool_from_time(capacitor, t, interval):
    x = np.arange(1, t, interval)
    y = capacitor.get_plot(x)
    plt.plot(x, y)
    plt.xlabel("Время")
    plt.ylabel("Емкость")
    plt.show()
