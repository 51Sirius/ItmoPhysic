from Modeling import *
import tkinter as tk
from Capacitor import Capacitor
from VariableCapacitor import VariableCapacitor
import graph as g


def simulation():
    def on_submit():
        capacitor = Capacitor(int(entry_vars[1].get()), int(entry_vars[0].get()), int(entry_vars[2].get()),
                              int(entry_vars[3].get()), int(entry_vars[6].get()))

        selected_options = [var.get() for var in checkbox_vars]

        capacitor.is_circle = selected_options[0]
        if selected_options[1]:
            draw_capacitors(int(entry_vars[2].get()))
        if selected_options[2]:

            var_capacitor = VariableCapacitor(int(entry_vars[7].get()), int(entry_vars[2].get()),
                                              int(entry_vars[0].get()), int(entry_vars[1].get()), int(entry_vars[3].get()))
            g.create_graph_pool_from_time(var_capacitor, int(entry_vars[5].get()), int(entry_vars[4].get()))
        output_text.set(f"C = {capacitor.pool_capacitor()}")

    root = tk.Tk()
    root.title("Capacitor")

    entry_vars = [tk.StringVar() for _ in range(10)]
    checkbox_vars = [tk.IntVar() for _ in range(3)]
    output_text = tk.StringVar()

    list_box_names = ["Ширина, см", "Длина, см", "Дистанция, мм", "Диэл. проницаемость", "Интервал", "Время",
                      "Радиус, см", "Угловая скорость"]
    list_check_box_names = ["Круг", "Визуализация", "2 часть"]
    for i in range(len(list_box_names)):
        label = tk.Label(root, text=list_box_names[i])
        label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
        entry = tk.Entry(root, textvariable=entry_vars[i])
        entry.grid(row=i, column=1, padx=5, pady=5)

    for i in range(3):
        checkbox = tk.Checkbutton(root, text=list_check_box_names[i], variable=checkbox_vars[i])
        checkbox.grid(row=11, column=i, padx=5, pady=5)

    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.grid(row=12, column=0, columnspan=3, pady=10)

    output_label = tk.Label(root, text="Output:")
    output_label.grid(row=13, column=0, padx=5, pady=5, sticky=tk.W)
    output_entry = tk.Entry(root, textvariable=output_text, state="readonly", width=40)
    output_entry.grid(row=13, column=1, columnspan=2, padx=5, pady=5)

    root.mainloop()
