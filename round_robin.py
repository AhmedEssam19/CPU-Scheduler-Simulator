from typing import List
from collections import namedtuple
import pandas as pd

def round_robin (processes: List[list], quantam_time):
    Process = namedtuple('Process', ['task_name', 'arrival_time', 'burst_time'])
    processes = [Process(process[0], process[1], process[2]) for process in processes]
    current_time = 0

    start_time = []
    finish_time = []
    task = []
    while True:
        is_processes_finished = True;
        for process in processes:
            if process.burst_time > 0:
                is_processes_finished = False;
                start_time.append(current_time)
                finish_time.append(current_time + quantam_time)
                task.append(process.task_name)

                current_time += quantam_time
                process.burst_time -= quantam_time
                #avg_waiting_time += start_times[-1] - process.arrival_time
        if is_processes_finished :
            break;

    df = pd.DataFrame({'Task': task, 'Start': start_time, 'Finish': finish_time})