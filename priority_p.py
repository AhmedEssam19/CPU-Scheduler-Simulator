from collections import namedtuple
def Priority_P(processes):
    Process = namedtuple('Process', 'process_id starting_time finish_time')
    All_Process = []
    All_Times = []
    schedule = []
    n = len(processes)
    wt = [0] * n
    burst = [0] * n
    priority = [0] * n
    for i in range(n):
        burst[i] = processes[i][2]
        priority[i] = processes[i][3]

    complete = 0
    t = 0
    minimum = 999999999
    fast = 999999999
    short = 0
    check = False
    while complete != n:
        for j in range(n):
            if processes[j][1] <= t and burst[j] > 0 and priority[j] < fast:
                fast = priority[j]
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
            fast = 9999999999
            complete += 1
            check = False
            fint = t + 1
            wt[short] = (fint - proc[short][2] - proc[short][1])
            if wt[short] < 0:
                wt[short] = 0
        t += 1
    m = len(All_Times)
    start = All_Times[0]
    end = 0
    for i in range(len(All_Times) - 1):
        if All_Process[i] != All_Process[i + 1]:
            end = All_Times[i]+1
            schedule.append(Process(All_Process[i], start, end))
            start = All_Times[i+1]
    schedule.append(Process(All_Process[i], start, All_Times[len(All_Times)-1]+1))
    total_wt = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
    avg_wait = (total_wt / n)
    return schedule, avg_wait


if __name__ == "__main__":
    # proc = [["P1", 4, 2, 2], ["P2", 0, 1, 1]]
    proc = [["P1", 0, 1, 2], ["P2", 1, 7, 6], ["P3", 2, 3, 3], ["P4", 3, 6, 5], ["P5", 4, 5, 4], ["P6", 5, 15, 10], ["P7", 15, 8, 9]]
    # proc = [["P1", 2, 6], ["P2", 5, 2], ["P3", 1, 8], ["P4", 0, 3], ["P5", 4, 4]]
    # proc = [["P1", 6, 2], ["P2", 2, 5], ["P3", 8, 1], ["P4", 3, 0], ["P5", 4, 4]]
    final = Priority_P(proc)
    print(final)
