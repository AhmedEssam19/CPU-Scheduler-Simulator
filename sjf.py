# importing for the tuple
from collections import namedtuple


# taking the input
def input_processes(no_of_processes):
    processes = []
    for i in range(no_of_processes):
        process_id = int(input("Enter process ID: "))
        arrival = int(input(f"Input the arrival time of process {process_id}: "))
        burst = int(input(f"input the burst time of process {process_id}:  "))
        processes.append([process_id, arrival, burst])
    # sorting according to arrival time
    processes.sort(key=lambda x: x[1])
    return processes


def schedule_non_preemptive(processes):
    # tuple for the final processes in the desired format
    Process = namedtuple('Process', 'process_id starting_time finish_time arrival_time')
    # temporary list of lists to schedule the process according to their burst time except the first one
    temp = processes.copy()
    # current time
    time = 0
    final_data = [Process(processes[0][0], processes[0][1], processes[0][1] + processes[0][2], processes[0][1])]
    burst = processes[0][2]
    time += burst
    temp.remove(processes[0])

    # sorting according to burst time
    temp.sort(key=lambda x: x[2])
    item = 0
    while item < len(temp):
        burst = temp[item][2]
        # check if arrival time <= the current time
        if temp[item][1] <= time:
            # schedule the other processes except the first one according to their burst time
            final_data.append(Process(temp[item][0], time, time + burst, temp[item][1]))
            time += burst
            temp.remove(temp[item])
            item -= 1

        # if arrival time < current time
        else:
            p = min(temp, key=lambda t: t[1])
            burst = p[2]
            # gap between the next arrival time and current time
            if time < p[1]:
                time = p[1]

            final_data.append(Process(p[0], time, time + burst, p[1]))
            time += burst
            temp.remove(p)
            item -= 1
        item += 1

    return final_data


def avg_waiting_time(final_data):
    waiting_time = 0

    for i in range(len(final_data)):
        waiting_time += getattr(final_data[i], "starting_time") - getattr(final_data[i], "arrival_time")

    avg_time = waiting_time / len(final_data)
    return avg_time


def display(data):
    dictionary = {}
    for i in range(len(data)):
        dictionary[f"Process number "] = getattr(data[i], "process_id")
        dictionary[f"Start time "] = getattr(data[i], "starting_time")
        dictionary[f"Finish time "] = getattr(data[i], "finish_time")
        print(dictionary)


# main
n = int(input("Enter the number of processes: "))
arr = input_processes(no_of_processes=n)
arr1 = schedule_non_preemptive(arr)
display(arr1)
avg_waiting_time(arr1)

