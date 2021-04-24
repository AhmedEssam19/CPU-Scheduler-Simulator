import tkinter as tk
from tkinter import ttk
from tkinter import *

BACKGROUND_COLOR = '#2c313c'
ENTRY_FONT = ("TkDefaultFont", 10)
ALGORITHMS = ['FCFS', 'SJF', 'Priority', 'Round Robin']

root = tk.Tk()
root.geometry('+%d+%d' % (350, 10))
root.configure(bg='#2c313c')

wrapper1 = LabelFrame(root)
wrapper2 = LabelFrame(root)
wrapper3 = LabelFrame(root)

################################## Section1 ########################################
canvas1 = tk.Canvas(wrapper1, width=800, height=60, bg=BACKGROUND_COLOR)
canvas1.pack()

section1_row = tk.Frame(wrapper1, bd=10, bg=BACKGROUND_COLOR)
section1_row.place(relheight=1, relwidth=1)

# choose the algorithm
algorithm_label = tk.Label(section1_row, text='Choose Algorithm:', bg=BACKGROUND_COLOR, fg='white')
algorithm_label.place(relx=0, rely=0, relheight=1, relwidth=0.2)
algorithm_input = ttk.Combobox(section1_row, values=ALGORITHMS, justify="center", font=ENTRY_FONT, state="readonly")
algorithm_input.bind("<<ComboboxSelected>>", None)
algorithm_input.place(relx=0.2, rely=0.2, relwidth=0.15, relheight=0.6)

# check if it's preemptive
isPreemptive = tk.BooleanVar()
preemptive_choice = tk.Checkbutton(section1_row, text='Preemptive', variable=isPreemptive, onvalue=True, offvalue=False)
preemptive_choice.place(relx=0.4, rely=0, relheight=1, relwidth=0.15)

# quantum time
quantum_label = tk.Label(section1_row, text='Quantum Time:', bg=BACKGROUND_COLOR, fg='white')
quantum_label.place(relx=0.6, rely=0, relheight=1, relwidth=0.2)
quantum_input = tk.Entry(section1_row, borderwidth=4, justify="center", font=10, state="normal")
quantum_input.place(relx=0.8, rely=0.0, relheight=1, relwidth=0.1)

################################## Section2 ########################################
canvas2 = tk.Canvas(wrapper2, width=800, height=300, bg=BACKGROUND_COLOR)
canvas2.pack(fill="y")

section2_column = tk.Frame(wrapper2, bd=10, bg=BACKGROUND_COLOR)
section2_column.place(relheight=1, relwidth=1)

#Add Process Botton
add_process_button = tk.Button(section2_column, text="Add Process")
add_process_button.place(rely=0.87, relx=0.4, relwidth=0.2, relheight=0.16)

##Scrollbar
y_scrollbar = ttk.Scrollbar(section2_column, orient="vertical", command=canvas2.yview)
y_scrollbar.place(relx=1, relwidth=0.8, relheight=0.75)

################################## Section3 ########################################
canvas3 = tk.Canvas(wrapper3, width=800, height=240, bg=BACKGROUND_COLOR)
canvas3.pack(fill="x")


#simulate & Cancle Row
section3_row = tk.Frame(wrapper3, bd=10, bg=BACKGROUND_COLOR)
section3_row.place(rely=0.8, relheight=0.25, relwidth=1)

#Cancle Botton
cancel_button = tk.Button(section3_row, text="Cancel")
cancel_button.place(relx=0.81, relwidth=0.2, relheight=1)

#simulate Botton
simulate_button = tk.Button(section3_row, text="Simulate")
simulate_button.place(relx=0.605, relwidth=0.2, relheight=1)



wrapper1.pack(fill="x", expand="yes", padx=10, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=10, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=10, pady=10)

root.mainloop()
