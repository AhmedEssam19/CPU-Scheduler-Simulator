import pandas as pd


def round_robin(processes, quantam_time):
    current_time = 0
    no_of_processes = len(processes)
    finished = [[]] * no_of_processes
    start_time = []
    finish_time = []
    task = []
    avg_waiting_time = 0

    # process[0] -> name /// process[1] -> arrival time /// process[2] -> burst time
    while True:
        is_processes_finished = True
        dummy = 0
        for process in processes:
            if process in finished:
                continue
            if process[2] > 0:
                is_processes_finished = False
                dummy += 1
                if current_time >= process[1]:
                    dummy -= 1
                    start_time.append(current_time)

                    # process time burst not always greater than quantam
                    finish = quantam_time
                    if process[2] < quantam_time:
                        finish = process[2]
                    finish_time.append(current_time + finish)
                    task.append(process[0])
                    avg_waiting_time += current_time - process[1]

                    # new current_time value -> current + quantam which is equal to new finish time
                    current_time += finish

                    # arrival time
                    process[1] = current_time

                    # burst time
                    process[2] -= finish
                    if process[2] == 0:
                        finished.append(process)

        # dummy here counts how many processes still in queue but (current pointer) doesn't reach to it yet
        # if we in a case where arrival time of a process is greater than our pointer, dummy = no of un finished
        # processes
        if dummy > 0 and dummy == no_of_processes - count_elements_in_finished(finished):
            current_time = processes[count_elements_in_finished(finished)][1]
        if is_processes_finished:
            break

    df = pd.DataFrame({'Task': task, 'Start': start_time, 'Finish': finish_time})
    avg_waiting_time /= no_of_processes

    return df, avg_waiting_time


def count_elements_in_finished (finished):
    c = 0
    for process in finished:
        if len(process) > 0:
            c += 1
    return c


# tasks = [
#     ['Task1', 0, 24],
#     ['Task2', 1, 3],
#     ['Task3', 2, 3],
# ]
# print(round_robin(tasks, 4))
