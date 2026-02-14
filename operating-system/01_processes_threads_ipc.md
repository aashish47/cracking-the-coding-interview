# 01 Processes, Threads, & IPC

## 1. System Calls

The interface between a running program (User Mode) and the Operating System (Kernel Mode).

- **User Mode:** Restricted access; applications run here.
- **Kernel Mode:** Full access to hardware; OS runs here.
- **Context Switch:** The process of saving the state of the current process and loading the state of the next process. High overhead.
- **Types:** Process Control (`fork`, `exec`), File Management (`open`, `read`), Device Management, Information Maintenance, Communication.

## 2. Processes

A process is a program in execution. It is the unit of work in a system.

- **Process Control Block (PCB):** Data structure storing process info (PID, State, PC, Registers, Open Files).
- **Process States:**
    1.  **New:** Being created.
    2.  **Ready:** Waiting to be assigned to a processor.
    3.  **Running:** Instructions are being executed.
    4.  **Waiting (Blocked):** Waiting for an event (I/O).
    5.  **Terminated:** Finished execution.

## 3. Threads

A "lightweight process." A basic unit of CPU utilization.

- **Shared:** Code, Data, Files (within the same process).
- **Private:** Registers, Stack, Program Counter.

| Feature            | Process                | Thread                      |
| :----------------- | :--------------------- | :-------------------------- |
| **Isolation**      | High (Separate memory) | Low (Shared memory)         |
| **Creation**       | Heavyweight (Slow)     | Lightweight (Fast)          |
| **Communication**  | IPC (Slow)             | Direct memory access (Fast) |
| **Context Switch** | Slow                   | Fast                        |

## 4. Inter-Process Communication (IPC)

Mechanisms to allow processes to exchange data.

1.  **Shared Memory:** A region of memory accessible by multiple processes. Fastest method but requires synchronization.
2.  **Message Passing:** Processes communicate by sending/receiving messages (e.g., Pipes, Sockets, Message Queues). Slower due to kernel intervention (system calls).
