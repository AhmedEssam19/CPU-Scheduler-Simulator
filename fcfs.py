from typing import List
from collections import namedtuple

import pandas as pd


def first_come_first_served(processes: List[list]):
    Process = namedtuple('Process', ['task_name', 'arrival_time', 'burst_time'])
    processes = [Process(process[0], process[1], process[2]) for process in processes]

    processes.sort(key=lambda task: task.arrival_time)

    start_times = []
    finish_times = [0]
    task_names = []

    avg_waiting_time = 0
    for process in processes:
        start_times.append(max(process.arrival_time, finish_times[-1]))
        finish_times.append(start_times[-1] + process.burst_time)
        task_names.append(process.task_name)
        avg_waiting_time += start_times[-1] - process.arrival_time

    df = pd.DataFrame({'Task': task_names, 'Start': start_times, 'Finish': finish_times[1:]})
    avg_waiting_time /= len(processes)

    return df, avg_waiting_time


# tasks = [
#     ['Task1', 2, 3],
#     ['Task2', 1, 8],
#     ['Task3', 5, 9],
# ]
# print(first_come_first_served(tasks)[1])
