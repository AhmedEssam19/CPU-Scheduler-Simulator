import tkinter as tk

from collections import namedtuple
from fcfs import first_come_first_served
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


def simulate(state, algorithms_combobox, quantum_input, root):
    try:
        quantum_time = float(quantum_input.get())
    except ValueError:
        pass

    processes = []
    for process in state['processes']:
        task_name = process.task_name.get()
        arrival_time = float(process.arrival_time.get())
        burst_time = float(process.burst_time.get())

        process_element = [task_name, arrival_time, burst_time]
        if process.priority is not None:
            priority = float(process.priority.get())
            process_element.append(priority)

        processes.append(process_element)

    algorithm = algorithms_combobox.get()
    if algorithm == 'FCFS':
        time_intervals, avg_wait_time = first_come_first_served(processes)

    elif algorithm == 'SJF':
        time_intervals, avg_wait_time = first_come_first_served(processes)

    elif algorithm == 'Priority':
        time_intervals, avg_wait_time = first_come_first_served(processes)

    else:
        time_intervals, avg_wait_time = first_come_first_served(processes, quantum_time)
    plot_schedule(time_intervals)
