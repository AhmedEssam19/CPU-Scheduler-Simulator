import pandas as pd


def round_robin(processes, quantam_time):
    # Process = namedtuple('Process', ['task_name', 'arrival_time', 'burst_time'])
    # processes = [Process(process[0], process[1], process[2]) for process in processes]
    current_time = 0

    start_time = []
    finish_time = []
    task = []
    avg_waiting_time = 0
    # process[0] -> name /// process[1] -> arrival time /// process[2] -> burst time
    while True:
        is_processes_finished = True
        for process in processes:
            if process[2] > 0:
                is_processes_finished = False
                start_time.append(current_time)

                # process time burst not always greater than quantam
                finish = quantam_time
                if process[2] < quantam_time:
                    finish = process[2]
                finish_time.append(current_time + finish)
                task.append(process[0])
                avg_waiting_time += current_time - process[1]
                current_time += finish
                # new current_time value -> current + quantam which is equal to new finish time
                process[1] = current_time
                process[2] -= finish
        if is_processes_finished:
            break

    df = pd.DataFrame({'Task': task, 'Start': start_time, 'Finish': finish_time})
    avg_waiting_time /= len(processes)

    return df, avg_waiting_time


# tasks = [
#     ['Task1', 0, 24],
#     ['Task2', 1, 3],
#     ['Task3', 2, 3],
# ]
# print(round_robin(tasks, 4))
