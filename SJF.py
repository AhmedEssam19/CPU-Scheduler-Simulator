from collections import namedtuple
import pandas as pd

def Decide_Short_job(processes,flag):
    if flag:
        return SJF_P(processes)
    else:
        return schedule_non_preemptive(processes)


def SJF_P(processes):
    Process = namedtuple('Process', 'process_id starting_time finish_time')
    All_Process = []
    All_Times = []
    task_names = []
    start_times = []
    finish_times = []
    schedule = []
    n = len(processes)
    wt = [0] * n
    burst = [0] * n
    for i in range(n):
        burst[i] = processes[i][2]

    complete = 0
    t = 0
    minimum = 999999999
    short = 0
    check = False
    while complete != n:
        for j in range(n):
            if processes[j][1] <= t and minimum > burst[j] > 0:
                minimum = burst[j]
                short = j
                check = True
        if not check:
            t += 1
            continue

        burst[short] -= 1
        All_Process.append(processes[short][0])
        All_Times.append(t)
        minimum = burst[short]
        if minimum == 0:
            minimum = 999999999

        if burst[short] == 0:
            complete += 1
            check = False
            fint = t + 1
            wt[short] = (fint - processes[short][2] - processes[short][1])
            if wt[short] < 0:
                wt[short] = 0
        t += 1
    m = len(All_Times)
    start = All_Times[0]
    end = 0
    for i in range(len(All_Times) - 1):
        if All_Process[i] != All_Process[i + 1]:
            end = All_Times[i]+1
            #schedule.append(Process(All_Process[i], start, end))
            task_names.append(All_Process[i])
            start_times.append(start)
            finish_times.append(end)
            start = All_Times[i+1]
    #schedule.append(Process(All_Process[i], start, All_Times[len(All_Times)-1]+1))
    task_names.append(All_Process[i])
    start_times.append(start)
    finish_times.append(All_Times[len(All_Times)-1]+1)
    total_wt = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
    avg_wait = (total_wt / n)
    df = pd.DataFrame({'Task': task_names, 'Start': start_times, 'Finish': finish_times})

    return df, avg_wait


def schedule_non_preemptive(processes):
    task_names = []
    start_times = []
    finish_times = []
    # tuple for the final processes in the desired format
    Process = namedtuple('Process', 'process_id starting_time finish_time arrival_time')
    # temporary list of lists to schedule the process according to their burst time except the first one
    temp = processes.copy()
    # current time
    time = 0
    final_data = []

    # sorting according to burst time
    temp.sort(key=lambda x: x[2])
    item = 0
    while item < len(temp):
        burst = temp[item][2]
        # check if arrival time <= the current time
        if temp[item][1] <= time:
            # schedule the other processes except the first one according to their burst time
            final_data.append(Process(temp[item][0], time, time + burst, temp[item][1]))
            task_names.append(temp[item][0])
            start_times.append(time)
            finish_times.append(time + burst)
            time += burst
            temp.remove(temp[item])
            item -= 1

        # if arrival time < current time
        else:
            # array of items which their arrival time between 0 to time

            j2 = filter(lambda x: x[1] <= time, temp)
            p = min(j2, key=lambda t: t[2])
            burst = p[2]
            # gap between the next arrival time and current time
            if time < p[1]:
                time = p[1]

            final_data.append(Process(p[0], time, time + burst, p[1]))
            task_names.append(p[0])
            start_times.append(time)
            finish_times.append(time + burst)
            time += burst
            temp.remove(p)
            item -= 1
        item += 1
    avg = avg_waiting_time(final_data)
    df = pd.DataFrame({'Task': task_names, 'Start': start_times, 'Finish': finish_times})
    return df,avg


def avg_waiting_time(final_data):
    waiting_time = 0

    for i in range(len(final_data)):
        waiting_time += getattr(final_data[i], "starting_time") - getattr(final_data[i], "arrival_time")

    avg_time = waiting_time / len(final_data)
    return avg_time

# if __name__ == "__main__":

    # proc = [["P1", 4, 2]]
    # proc = [["P1", 2, 6], ["P2", 5, 2], ["P3", 1, 8], ["P4", 0, 3], ["P5", 4, 4]]
    # proc = [["P1", 0, 5], ["P2", 3, 6], ["P3", 9, 2]]
    # final = Decide_Short_job(proc, 0)
    # print(final)