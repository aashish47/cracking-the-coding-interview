# 04 CPU & I/O Scheduling

## 1. CPU Scheduling

Deciding which process in the Ready Queue gets the CPU.

- **Preemptive:** OS can interrupt a running process (e.g., time quantum expires, higher priority arrives).
- **Non-Preemptive:** Process keeps CPU until it terminates or switches to waiting state.

### 1.1 Scheduling Metrics

- **Arrival Time (AT):** Time process enters ready queue.
- **Burst Time (BT):** Time required for execution.
- **Turnaround Time (TAT):** Completion Time - Arrival Time.
- **Waiting Time (WT):** TAT - Burst Time.

### 1.2 Algorithms

| Algorithm                                | Type           | Description                                                               | Pros/Cons                                                                                                     |
| :--------------------------------------- | :------------- | :------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------ |
| **FCFS** (First Come First Serve)        | Non-Preemptive | FIFO Queue.                                                               | Simple. Suffers from **Convoy Effect** (short process waits for long process).                                |
| **SJF** (Shortest Job First)             | Non-Preemptive | Selects process with smallest BT.                                         | Optimal average WT. Requires knowing BT in advance.                                                           |
| **SRTF** (Shortest Remaining Time First) | Preemptive     | Preemptive version of SJF.                                                | Minimal average WT. High overhead.                                                                            |
| **Round Robin (RR)**                     | Preemptive     | Each process gets a time quantum ($q$).                                   | Fair, good response time. Performance depends on $q$ (Too large = FCFS; Too small = Context Switch overhead). |
| **Priority**                             | Both           | Highest priority runs first.                                              | Risk of **Starvation** (Low priority never runs). Solution: **Aging** (increase priority over time).          |
| **Multilevel Queue**                     | Both           | Separate queues for different process types (System, Interactive, Batch). | Fixed priority between queues.                                                                                |

## 2. I/O (Disk) Scheduling

Goal: Minimize **Seek Time** (time for disk arm to move to the cylinder).

### 2.1 Algorithms

Assume Head starts at 50. Request Queue: 98, 183, 37, 122, 14, 124, 65, 67.

1.  **FCFS (First Come First Serve):**
    - Process requests in order.
    - _Fair but slow._ Random head movement.

2.  **SSTF (Shortest Seek Time First):**
    - Select request closest to current head position.
    - _High performance, risk of starvation_ for far-away tracks.

3.  **SCAN (Elevator Algorithm):**
    - Head moves in one direction (e.g., up), servicing requests until it hits the end, then reverses.
    - _Good distribution._

4.  **C-SCAN (Circular SCAN):**
    - Like SCAN, but when it reaches the end, it returns to the beginning _without_ servicing requests on the return trip.
    - _More uniform wait time._

5.  **LOOK / C-LOOK:**
    - Like SCAN/C-SCAN, but the arm only goes as far as the last request in that direction, not to the physical end of the disk.

| Algorithm       | Best Use Case                             |
| :-------------- | :---------------------------------------- |
| **SSTF**        | General purpose, low load.                |
| **SCAN/C-SCAN** | Heavy load systems (prevents starvation). |
| **LOOK/C-LOOK** | Optimization of SCAN (saves idle travel). |
