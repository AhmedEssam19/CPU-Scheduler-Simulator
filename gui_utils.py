import tkinter as tk
import tkinter.messagebox

from collections import namedtuple
from fcfs import first_come_first_served
from SJF import Decide_Short_job
from priority import Priority_Scheduling
from round_robin import round_robin
from GanttChart import plot_schedule

Process = namedtuple('Process', 'task_name arrival_time burst_time priority')


def reset_scroll_region(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))


def add_process(frame, state, algorithms_combobox):
    task_name_label = tk.Label(frame, text='Task Name', bg=state['BACKGROUND_COLOR'], fg='white')
    task_name_label.grid(row=state['row'], column=0, padx=10)
    task_name_entry = tk.Entry(frame, borderwidth=4, justify="center", font=10)
    task_name_entry.grid(row=state['row'], column=1, padx=10, )

    arrival_time_label = tk.Label(frame, text='Arrival Time', bg=state['BACKGROUND_COLOR'], fg='white')
    arrival_time_label.grid(row=state['row'], column=2, padx=10)
    arrival_time_entry = tk.Entry(frame, borderwidth=4, justify="center", font=10)
    arrival_time_entry.grid(row=state['row'], column=3, padx=10)

    burst_time_label = tk.Label(frame, text='Burst Time', bg=state['BACKGROUND_COLOR'], fg='white')
    burst_time_label.grid(row=state['row'], column=4, padx=10)
    burst_time_entry = tk.Entry(frame, borderwidth=4, justify="center", font=10)
    burst_time_entry.grid(row=state['row'], column=5, padx=10)

    algorithm = algorithms_combobox.get()
    priority_entry = None
    priority_label = None
    if algorithm == 'Priority':
        priority_label = tk.Label(frame, text='Priority', bg=state['BACKGROUND_COLOR'], fg='white')
        priority_label.grid(row=state['row'], column=6, padx=10)
        priority_entry = tk.Entry(frame, borderwidth=4, justify="center", font=10)
        priority_entry.grid(row=state['row'], column=7, padx=10)

    new_process = Process(task_name_entry, arrival_time_entry, burst_time_entry, priority_entry)
    state['processes'].append(new_process)
    state['processes_labels'].append([task_name_label, arrival_time_label, burst_time_label, priority_label])
    state['row'] += 1
    state['simulate_button']['state'] = 'normal'


def select_algorithm(state, algorithms_combobox, preemptive_checkbox, quantum_input, add_process_button):
    clear_processes(state)
    algorithm = algorithms_combobox.get()

    add_process_button['state'] = 'normal'
    preemptive_checkbox['state'] = 'disable'
    quantum_input['state'] = 'disable'

    if algorithm == 'SJF' or algorithm == 'Priority':
        preemptive_checkbox['state'] = 'normal'

    elif algorithm == 'Round Robin':
        quantum_input['state'] = 'normal'


def clear_processes(state):
    for process in state['processes']:
        process.task_name.destroy()
        process.arrival_time.destroy()
        process.burst_time.destroy()

        if process.priority is not None:
            process.priority.destroy()

    for process_labels in state['processes_labels']:
        for label in process_labels:
            if label is not None:
                label.destroy()

    state['row'] = 0
    state['processes'] = []
    state['simulate_button']['state'] = 'disable'


def simulate(state, algorithms_combobox, quantum_input):
    task_names = []
    processes = []
    for i, process in enumerate(state['processes']):

        # check valid task name
        task_name = process.task_name.get()
        if task_name == "":
            tk.messagebox.showerror('Error', f'Invalid Task Name in process {i + 1}')
            return

        # check valid arrival time
        try:
            arrival_time = float(process.arrival_time.get())
        except ValueError:
            tk.messagebox.showerror('Error', f'Invalid Arrival Time in process {i+1}')
            return

        # check valid burst time
        try:
            burst_time = float(process.burst_time.get())
        except ValueError:
            tk.messagebox.showerror('Error', f'Invalid Burst Time in process {i+1}')
            return

        process_element = [task_name, arrival_time, burst_time]
        if process.priority is not None:
            # check valid priority
            try:
                priority = float(process.priority.get())
            except ValueError:
                tk.messagebox.showerror('Error', f'Invalid priority in process {i + 1}')
                return

            process_element.append(priority)

        task_names.append(task_name)
        processes.append(process_element)

    # check unique task names
    if len(task_names) != len(set(task_names)):
        tk.messagebox.showerror('Error', f'Duplicate Task Names')
        return

    algorithm = algorithms_combobox.get()
    if algorithm == 'FCFS':
        time_intervals, avg_wait_time = first_come_first_served(processes)

    elif algorithm == 'SJF':
        time_intervals, avg_wait_time = Decide_Short_job(processes, state['isPreemptive'])

    elif algorithm == 'Priority':
        time_intervals, avg_wait_time = Priority_Scheduling(processes, state['isPreemptive'])

    else:
        try:
            quantum_time = float(quantum_input.get())
        except ValueError:
            tk.messagebox.showerror('Error', 'Invalid Quantum Time')
            return

        time_intervals, avg_wait_time = round_robin(processes, quantum_time)

    plot_schedule(time_intervals)
