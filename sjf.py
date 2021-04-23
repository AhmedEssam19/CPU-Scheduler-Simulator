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
    Process = namedtuple('Process', 'process_id starting_time finish_time')
    # temporary list of lists to schedule the process according to their burst time except the first one
    temp = processes.copy()
    # current time
    time = 0
    final_data = []
    for item in range(len(temp)):
        burst = processes[item][2]
        # first process
        if time == 0:
            final_data.append(Process(processes[item][0], time, time + burst))
            time += burst
            temp.remove(processes[item])
            # sorting according to burst time
            temp.sort(key=lambda x: x[2])

        else:
            # schedule the other processes except the first one according to their burst time
            final_data.append(Process(temp[item-1][0], time, time+burst))
            time += burst

    return final_data


def display(data):
    for i in range(len(data)):
        print(data[i])


# main
n = int(input("Enter the number of processes: "))
display(schedule_non_preemptive(input_processes(no_of_processes=n)))





