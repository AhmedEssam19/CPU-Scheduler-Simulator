import tkinter as tk
from tkinter import ttk

BACKGROUND_COLOR = '#2c313c'
ENTRY_FONT = ("TkDefaultFont", 10)
ALGORITHMS = ['FCFS', 'SJF', 'Priority', 'Round Robin']

root = tk.Tk()
root.geometry('+%d+%d' % (350, 10))
root.configure(bg='#2c313c')

canvas = tk.Canvas(root, width=800, height=600, bg=BACKGROUND_COLOR)
canvas.pack()

row1 = tk.Frame(root, bd=10, bg=BACKGROUND_COLOR)
row1.place(relheight=0.1, relwidth=1)

# choose the algorithm
algorithm_label = tk.Label(row1, text='Choose Algorithm:', bg=BACKGROUND_COLOR, fg='white')
algorithm_label.place(relx=0, rely=0, relheight=1, relwidth=0.2)
algorithm_input = ttk.Combobox(row1, values=ALGORITHMS, justify="center", font=ENTRY_FONT, state="readonly")
algorithm_input.bind("<<ComboboxSelected>>", None)
algorithm_input.place(relx=0.2, rely=0.2, relwidth=0.15, relheight=0.6)

# check if it's preemptive
isPreemptive = tk.BooleanVar()
preemptive_choice = tk.Checkbutton(row1, text='Preemptive', variable=isPreemptive, onvalue=True, offvalue=False)
preemptive_choice.place(relx=0.4, rely=0, relheight=1, relwidth=0.15)

# quantum time
quantum_label = tk.Label(row1, text='Quantum Time:', bg=BACKGROUND_COLOR, fg='white')
quantum_label.place(relx=0.6, rely=0, relheight=1, relwidth=0.2)
quantum_input = tk.Entry(row1, borderwidth=4, justify="center", font=10, state="normal")
quantum_input.place(relx=0.8, rely=0.0, relheight=1, relwidth=0.1)

scrollbar = tk.Scrollbar(root)
scrollbar.pack()

root.mainloop()
