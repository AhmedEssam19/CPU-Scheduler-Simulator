def process_data(no_of_processes):
    processes = []
    for i in range(no_of_processes):
        process_id= int(input("Enter process ID: "))
        arrival = int(input(f"Input the arrival time of process {process_id}: "))
        burst = int(input(f"input the burst time of process {process_id}:  "))
        processes.append([process_id, arrival, burst])
    # sorting according to arrival time
    processes.sort(key=lambda x: x[1])
    return processes


def display(processes_id, starting_time, finish_time):
    dictionary = {}
    for i in range(len(processes_id)):
        dictionary[f"Process {processes_id[i]} "] = [f"start time: {starting_time[i]}",
                                                     f"finish time: {finish_time[i]}"]

    return dictionary


def schedule(processes):
    dictionary = {}
    temp = processes.copy()
    time = 0
    burst = 0
    starting_time = []
    finish_time = []
    for i in range(len(temp)):
        if time == 0:
            burst = processes[i][2]

            time += burst



        
#
# def schedule(processes):
#     dictionary = {}
#     time = 0
#     burst = 0
#     rem_time = 0
#     start_time = []
#     waiting_time = []
#     finish_time = []
#     for i in range(len(processes)):
#         # push first process to cpu
#         if processes[i][1] == 0:
#             start_time[processes[i][0]] = time
#             dictionary[f"process {processes[i][0]} "] = [f"Start time ", processes[i][1], processes[i][2]]
#             burst = processes[i][2]
#         #elif processes[i][2] < burst:
#
#
#

arr = process_data(2)
print(len(arr))
# dictionary = {}
# for i in range(len(arr)):
#     dictionary[f"item: {i}"] = [arr[i][0], arr[i][1], arr[i][2]]
#
# print(dictionary)
