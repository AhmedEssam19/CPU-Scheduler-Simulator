from tkinter import ttk
from tkinter import *
from gui_utils import *

ENTRY_FONT = ("TkDefaultFont", 10)
ALGORITHMS = ['FCFS', 'SJF', 'Priority', 'Round Robin']

state = {
    'row': 0,
    'BACKGROUND_COLOR': '#2c313c',
    'processes': [],
    'processes_labels': []
}


def main():
    root = tk.Tk()
    root.geometry("1450x600")
    root.configure(bg='#2c313c')

    # Make the main frame
    main_frame = Frame(root, bg=state['BACKGROUND_COLOR'])
    main_frame.pack(fill=BOTH, expand=1)

    row1 = tk.Frame(main_frame, bd=10, bg=state['BACKGROUND_COLOR'])
    row1.place(relheight=0.1, relwidth=1)

    # choose the algorithm
    algorithm_label = tk.Label(row1, text='Choose Algorithm:', bg=state['BACKGROUND_COLOR'], fg='white')
    algorithm_label.place(relx=0, rely=0, relheight=1, relwidth=0.2)
    algorithm_input = ttk.Combobox(row1, values=ALGORITHMS, justify="center", font=ENTRY_FONT, state="readonly")
    algorithm_input.bind("<<ComboboxSelected>>", lambda _: select_algorithm(state, algorithm_input, preemptive_choice,
                                                                            quantum_input, add_process_button))
    algorithm_input.place(relx=0.2, rely=0.2, relwidth=0.15, relheight=0.6)

    # check if it's preemptive
    isPreemptive = tk.BooleanVar()
    state['isPreemptive'] = isPreemptive
    preemptive_choice = tk.Checkbutton(row1, text='Preemptive', variable=isPreemptive,
                                       onvalue=True, offvalue=False, state='disable')
    preemptive_choice.place(relx=0.4, rely=0, relheight=1, relwidth=0.15)

    # quantum time
    quantum_label = tk.Label(row1, text='Quantum Time:', bg=state['BACKGROUND_COLOR'], fg='white')
    quantum_label.place(relx=0.6, rely=0, relheight=1, relwidth=0.2)
    quantum_input = tk.Entry(row1, borderwidth=4, justify="center", font=10, state="disable")
    quantum_input.place(relx=0.8, rely=0.0, relheight=1, relwidth=0.1)

    # Make frame for input processes
    processes_input_frame = Frame(main_frame, bd=10, bg='white')
    processes_input_frame.place(relx=0, rely=0.1, relwidth=1, relheight=0.6)

    my_canvas = Canvas(processes_input_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(processes_input_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    inner_frame = Frame(my_canvas)
    inner_frame.bind("<Configure>", lambda e: reset_scroll_region(my_canvas))

    my_canvas.create_window((0, 0), window=inner_frame, anchor='nw')

    # Make button to add processes
    add_process_button = tk.Button(main_frame, text="Add Process",
                                   command=lambda: add_process(inner_frame, state, algorithm_input), state='disable')
    add_process_button.place(rely=0.71, relx=0.84, relwidth=0.15, relheight=0.1)

    root.mainloop()


if __name__ == "__main__":
    main()
