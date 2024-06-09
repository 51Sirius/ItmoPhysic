import tkinter as tk
from src.draw import *


def simulation():
    def on_submit():
        draw_plots(float(entry_vars[0].get()), float(entry_vars[1].get()), float(entry_vars[2].get()),
                   float(entry_vars[3].get()))

    root = tk.Tk()
    root.title("Newton Ring")
    list_box_names = ["Длина волны, НМ", "Середина спектра, НМ", "Ширина спектра, НМ", "Радиус, М"]
    default_values = [
        "400", "400", "10", "1"
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
    root.mainloop()


simulation()
