import tkinter as tk


def reset_scroll_region(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))


def add_process(frame, state):
    label = tk.Label(frame, text='Task Name', bg=state['BACKGROUND_COLOR'], fg='white')
    label.grid(row=state['row'], column=0, padx=10)
    entry = tk.Entry(frame, borderwidth=4, justify="center", font=10, state="normal")
    entry.grid(row=state['row'], column=1, padx=10, )
    label2 = tk.Label(frame, text='Arrival Time', bg=state['BACKGROUND_COLOR'], fg='white')
    label2.grid(row=state['row'], column=2, padx=10)
    entry2 = tk.Entry(frame, borderwidth=4, justify="center", font=10, state="normal")
    entry2.grid(row=state['row'], column=3, padx=10)
    label3 = tk.Label(frame, text='Burst Time', bg=state['BACKGROUND_COLOR'], fg='white')
    label3.grid(row=state['row'], column=4, padx=10)
    entry3 = tk.Entry(frame, borderwidth=4, justify="center", font=10, state="normal")
    entry3.grid(row=state['row'], column=5, padx=10)
    state['row'] += 1
