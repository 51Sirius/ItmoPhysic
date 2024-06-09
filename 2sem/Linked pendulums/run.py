import tkinter as tk
from src.consts import *
from src.normal_frequencies import *
from src.draw import *


def simulation():
    def on_submit():
        omega1, omega2 = search_normal_frequencies(float(entry_vars[0].get()),
                                                   float(entry_vars[1].get()),
                                                   float(entry_vars[2].get()))
        output_text.set(
            f"{round(omega1, 2)} ГЦ")
        output_text1.set(f"{round(omega2, 2)} ГЦ")
        draw_plots(float(entry_vars[0].get()), float(entry_vars[1].get()), float(entry_vars[2].get()),
                   float(entry_vars[3].get()), float(entry_vars[4].get()), float(entry_vars[5].get()),
                   float(entry_vars[6].get()),
                   float(entry_vars[7].get()), float(entry_vars[8].get()))

    root = tk.Tk()
    root.title("LINKPEND")
    list_box_names = ["Масса, Кг", "Жесткость пружины, Н/М", "Длина маятников, М", "Начальное отклонение №1, Гр",
                      "Начальное отклонение №2, Гр", "Положение пружины, М", "Время моделирования от, С",
                      "Время моделирования до, С", "Коэф затухания"]
    default_values = [
        "1.0", "0.3", "8.0", "0.01", "-0.3",
        "4.0", "1000.0", "1500.0", "0.01"
    ]
    entry_vars = [tk.StringVar(value=default_values[i]) for i in range(len(list_box_names))]
    output_text = tk.StringVar()
    output_text1 = tk.StringVar()
    for i in range(len(list_box_names)):
        label = tk.Label(root, text=list_box_names[i])
        label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
        entry = tk.Entry(root, textvariable=entry_vars[i])
        entry.grid(row=i, column=1, padx=5, pady=5)
    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.grid(row=12, column=0, columnspan=3, pady=10)
    output_label = tk.Label(root, text="Частота первого маятника:")
    output_label.grid(row=13, column=0, padx=5, pady=5, sticky=tk.W)
    output_label = tk.Label(root, text="Частота второго маятника:")
    output_label.grid(row=14, column=0, padx=5, pady=5, sticky=tk.W)
    output_entry = tk.Entry(root, textvariable=output_text, state="readonly", width=60)
    output_entry.grid(row=13, column=1, columnspan=2, padx=5, pady=5)
    output_entry = tk.Entry(root, textvariable=output_text1, state="readonly", width=60)
    output_entry.grid(row=14, column=1, columnspan=3, padx=5, pady=5)
    root.mainloop()


simulation()
