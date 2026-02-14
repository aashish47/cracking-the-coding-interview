# 02 Concurrency & Synchronization

## 1. The Critical Section Problem

A code segment where shared resources are accessed. To prevent race conditions, three conditions must be met:

1.  **Mutual Exclusion:** Only one process in the Critical Section (CS) at a time.
2.  **Progress:** If no one is in the CS, someone wanting to enter should not be blocked indefinitely.
3.  **Bounded Waiting:** A limit exists on how many times other processes can enter the CS before a specific process is granted access (prevents starvation).

## 2. Synchronization Tools

- **Mutex (Lock):** A locking mechanism. `acquire()` to lock, `release()` to unlock. Boolean variable.
- **Semaphore:** An integer variable used for signaling.
    - **Wait (P):** Decrements value. If < 0, block.
    - **Signal (V):** Increments value. Wakes up a blocked process.
    - **Binary Semaphore:** Values 0 or 1 (Same as Mutex).
    - **Counting Semaphore:** Values 0 to N (Manages N instances of a resource).
- **Monitors:** High-level abstraction (class/object) where only one thread can be active at a time. Handles locking automatically.

## 3. Classic Problems

- **Producer-Consumer:** Buffer management.
- **Readers-Writers:** Multiple readers allowed; writers require exclusive access.
- **Dining Philosophers:** Resource allocation without deadlock.
