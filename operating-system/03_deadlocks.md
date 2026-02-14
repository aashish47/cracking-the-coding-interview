# 03 Deadlocks

## 1. Definition

A situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.

## 2. Necessary Conditions (Coffman Conditions)

Deadlock can arise if **all four** conditions hold simultaneously:

1.  **Mutual Exclusion:** At least one resource is non-sharable.
2.  **Hold and Wait:** A process holding at least one resource is waiting to acquire additional resources held by others.
3.  **No Preemption:** Resources cannot be forcibly taken; they must be released voluntarily.
4.  **Circular Wait:** $P_0$ waits for $P_1$, $P_1$ waits for $P_2$ ... $P_n$ waits for $P_0$.

## 3. Handling Deadlocks

### 3.1 Deadlock Prevention

Ensure at least one of the 4 conditions cannot hold.

- _Attack Hold and Wait:_ Request all resources at start.
- _Attack No Preemption:_ If a process requests a resource that isn't available, it must release all held resources.
- _Attack Circular Wait:_ Impose a total ordering of resource types.

### 3.2 Deadlock Avoidance

The OS requires a priori information about how many resources a process will request.

- **Safe State:** A system is in a safe state if there exists a sequence of all processes such that each can satisfy its maximum demand using available resources + resources held by finished processes.
- **Banker's Algorithm:** Used to determine if a request can be granted safely.
    - If Request $\le$ Available, pretend to allocate.
    - Check if the new state is Safe.
    - If Safe $\rightarrow$ Grant. If Unsafe $\rightarrow$ Wait.

### 3.3 Deadlock Detection

Allow deadlock to occur, then detect and recover.

- **Resource Allocation Graph (RAG):**
    - If graph has no cycles $\rightarrow$ No deadlock.
    - If graph has cycles:
        - Single instance resources $\rightarrow$ Deadlock.
        - Multi-instance resources $\rightarrow$ Possibility of deadlock.

### 3.4 Deadlock Recovery

1.  **Process Termination:**
    - Abort all deadlocked processes.
    - Abort one at a time until the cycle is eliminated.
2.  **Resource Preemption:**
    - Select a victim (minimize cost).
    - Rollback the victim process to a safe state.
    - Prevent starvation (ensure the same process isn't always the victim).
