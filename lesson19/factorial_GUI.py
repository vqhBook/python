import math
import tkinter as tk
from tkinter import ttk

def on_calculate():
    try:
        fact = math.factorial(num.get())
    except:
        num.set(0)
        fact = 1
    finally:
        fact_label.configure(text=str(fact))
        num_entry.focus()
    
win = tk.Tk()
win.title("Calculating Factorial")
win.resizable(False, False)

num = tk.IntVar()

ttk.Label(win, text="n = ").grid(row=0, column=0, sticky="E")
(num_entry := ttk.Entry(win, textvariable=num)).grid(row=0, column=1, sticky="W")
ttk.Label(win, text="n! = ").grid(row=1, column=0, sticky="E")
(fact_label := ttk.Label(win, width=40, text="1", foreground="red")).grid(row=1, column=1, sticky="W")
ttk.Button(win, text="Calculate", command=on_calculate).grid(row=2, column=0, sticky="E")
ttk.Button(win, text="Exit", command=win.destroy).grid(row=2, column=1, sticky="W")

win.bind('<Return>', lambda _: on_calculate())
win.bind('<Escape>', lambda _: win.destroy())

for child in win.winfo_children():
    child.grid(padx=4, pady=4)

num_entry.focus()

win.mainloop()
