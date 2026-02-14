# 05 Transactions & Concurrency Control

## 1. ACID Properties (The Foundation)

- **Atomicity:** A transaction is "All or Nothing". If it fails, rollback everything.
- **Consistency:** Database transforms from one valid state to another (preserving constraints).
- **Isolation:** Concurrent transactions do not interfere with each other.
- **Durability:** Once committed, changes are permanent (survive power loss).

## 2. Transaction Anomalies (Read Phenomena)

These occur when simultaneous transactions do not result in data inconsistency due to lack of isolation.

| Anomaly               | Description                                                                                              |
| :-------------------- | :------------------------------------------------------------------------------------------------------- |
| **Lost Update**       | Two transactions update the same row; the last one overwrites the first without seeing its changes.      |
| **Dirty Read**        | A transaction reads data modified by another transaction that hasn't committed yet.                      |
| **Unrepeatable Read** | A transaction reads the same row twice and gets different values because another transaction updated it. |
| **Phantom Read**      | A transaction re-runs a query and finds new "phantom" rows added by a committed transaction.             |

## 3. Schedules

A **Schedule** is the "play-by-play" sequence of operations from various transactions.

| Schedule Type    | Description                               | Pros/Cons                                            |
| :--------------- | :---------------------------------------- | :--------------------------------------------------- |
| **Serial**       | Transactions execute one after another.   | **+** Consistent; **-** Poor performance.            |
| **Non-Serial**   | Operations are interleaved.               | **+** High performance; **-** Risk of inconsistency. |
| **Serializable** | Non-serial but behaves like a serial one. | **+** Best of both worlds.                           |

## 4. Serializability

A schedule is **serializable** if its outcome is the same as some serial execution of the same transactions.

### 4.1 Conflict Serializability

A schedule is conflict serializable if it can be transformed into a serial schedule by swapping non-conflicting operations. Two operations **conflict** if they meet all three criteria:

1. They belong to **different transactions**.
2. They access the **same data item**.
3. At least one is a **Write (W)** operation.

**Conflict Scenarios**

| Operation 1  | Operation 2  | Conflict? | Formal Name           | The "Real World" Consequence                                                                                                             |
| :----------- | :----------- | :-------- | :-------------------- | :--------------------------------------------------------------------------------------------------------------------------------------- |
| **Read(X)**  | **Read(X)**  | **No**    | **Safe**              | Multiple people can look at a bank balance without changing it.                                                                          |
| **Read(X)**  | **Write(X)** | **Yes**   | **Unrepeatable Read** | T1​ reads "100", T2​ changes it to "200". T1​ looks again and is confused why the "100" vanished.                                        |
| **Write(X)** | **Read(X)**  | **Yes**   | **Dirty Read**        | T1​ updates a balance but hasn't "Saved" (Committed) yet. T2​ sees the new value, but then T1​ crashes and reverts. T2​ just read a lie. |
| **Write(X)** | **Write(X)** | **Yes**   | **Lost Update**       | T1​ and T2​ both try to update the same row. T2​ finishes last and "overwrites" T1​, so T1​'s work is gone forever.                      |

### 4.2 Precedence Graph (Testing Serializability)

To determine if a schedule is conflict serializable:

1. Create a node for each transaction $T_i$.
2. Draw an edge $T_i \rightarrow T_j$ if $T_i$ performs an operation that conflicts with a _later_ operation in $T_j$.
3. **Result:** If the graph has **no cycles**, the schedule is conflict serializable.

**Example:**
Schedule $S: R_1(X), W_2(X), R_1(Y), W_3(X)$

| $T_1$  | $T_2$  | $T_3$  |
| :----- | :----- | :----- |
| $R(X)$ |        |        |
|        | $W(X)$ |        |
| $R(Y)$ |        |        |
|        |        | $W(X)$ |

1. $R_1(X)$ conflicts with $W_2(X)$ (later) $\rightarrow$ Edge $T_1 \rightarrow T_2$
2. $W_2(X)$ conflicts with $W_3(X)$ (later) $\rightarrow$ Edge $T_2 \rightarrow T_3$
3. Graph: $T_1 \rightarrow T_2 \rightarrow T_3$
4. **Conclusion:** No cycles. The schedule is conflict serializable.

**Example (Non-Serializable):**
Schedule $S: R_1(X), W_2(X), W_1(X)$

| $T_1$  | $T_2$  |
| :----- | :----- |
| $R(X)$ |        |
|        | $W(X)$ |
| $W(X)$ |        |

1. $R_1(X)$ conflicts with $W_2(X)$ (later) $\rightarrow$ Edge $T_1 \rightarrow T_2$
2. $W_2(X)$ conflicts with $W_1(X)$ (later) $\rightarrow$ Edge $T_2 \rightarrow T_1$
3. **Conclusion:** Cycle detected ($T_1 \leftrightarrow T_2$). Not conflict serializable.

### 4.3 View Serializability

A schedule $S$ is **View Serializable** if it is **View Equivalent** to some serial schedule $S'$.

#### The Three Conditions for View Equivalence

Two schedules $S$ and $S'$ are view equivalent if for every data item $Q$:

1.  **Initial Read:** If $T_i$ reads the initial value of $Q$ in $S$, it must also read the initial value of $Q$ in $S'$.
2.  **Updated Read (Read-from):** If $T_i$ reads a value of $Q$ written by $T_j$ in $S$, it must also read the value of $Q$ written by $T_j$ in $S'$.
3.  **Final Write:** The transaction that performs the last write on $Q$ in $S$ must also perform the last write on $Q$ in $S'$.

#### Blind Writes

- **Definition:** A $Write(Q)$ operation performed by a transaction without a preceding $Read(Q)$.
- **Significance:** A schedule can only be View Serializable but NOT Conflict Serializable if it contains **Blind Writes**.
- **Logic:** In Conflict Serializability, $W-W$ conflicts create rigid arrows. In View Serializability, if transactions just "overwrite" data without looking at it, the intermediate order doesn't matter—only the final writer does.

#### Testing View Serializability

To prove it, you must find at least one serial permutation ($n!$ possibilities) that satisfies the three rules above.

**Example:** For transactions $\{T_1, T_2, T_3\}$:

**Schedule $S$:**

| $T_1$  | $T_2$  | $T_3$  |
| :----- | :----- | :----- |
| $R(X)$ |        |        |
| $W(X)$ |        |        |
|        | $W(X)$ |        |
|        |        | $W(X)$ |

| Schedule Type   | Order                 | View Equivalent to S?           |
| :-------------- | :-------------------- | :------------------------------ |
| Serial Choice 1 | $T_1 \to T_2 \to T_3$ | **Yes!** (Matches all 3 rules)  |
| Serial Choice 2 | $T_3 \to T_2 \to T_1$ | No (Initial read doesn't match) |
| Serial Choice 3 | $T_1 \to T_3 \to T_2$ | No (Final write doesn't match)  |
| Serial Choice 4 | $T_2 \to T_1 \to T_3$ | No (Initial read doesn't match) |
| Serial Choice 5 | $T_2 \to T_3 \to T_1$ | No (Initial read doesn't match) |
| Serial Choice 6 | $T_3 \to T_1 \to T_2$ | No (Initial read doesn't match) |

#### Comparison

- All conflict-serializable schedules are view-serializable.
- View serializability is more inclusive but harder to compute.

| Feature          | Conflict Serializability        | View Serializability    |
| :--------------- | :------------------------------ | :---------------------- |
| **Strictness**   | Higher (More restrictive)       | Lower (More inclusive)  |
| **Constraint**   | Order of all conflicting ops    | Results & data flow     |
| **Complexity**   | $O(n^2)$ using Precedence Graph | NP-Complete (Very slow) |
| **Practicality** | Used in most DBMS               | Mostly theoretical      |

## 5. Recoverability

Ensures the database can recover correctly from a failure.

| Type            | Rule                                                                        |
| :-------------- | :-------------------------------------------------------------------------- |
| **Recoverable** | If $T_j$ reads from $T_i$, $T_i$ must commit before $T_j$ commits.          |
| **Cascadeless** | $T_j$ can only read data from $T_i$ _after_ $T_i$ has committed.            |
| **Strict**      | $T_j$ can neither read nor write data from $T_i$ until $T_i$ has committed. |

## 6. Concurrency Control Protocols

### 6.1 Lock-Based Protocols (2PL)

- **Shared Lock (S):** Read-only access; multiple transactions can hold S-locks.
- **Exclusive Lock (X):** Read and Write access; only one transaction can hold an X-lock.
- **2-Phase Locking (2PL):**
    - **Growing Phase:** Transaction acquires all locks, releases none.
    - **Shrinking Phase:** Transaction releases locks, acquires none.
    - _Guarantee:_ Ensures **Serializability**.
    - _Drawback:_ Subject to **Deadlocks**.
    - **Example:** If $T_1$ needs to update $X$ and $Y$, it must acquire locks for both before it can release either. It cannot release the lock on $X$ and then later ask for a lock on $Y$.

### 6.2 Timestamp Ordering

- Assigns a unique timestamp (TS) to every transaction.
- Operations are allowed only if they follow the timestamp order (older transactions get priority).
- _Guarantee:_ **Deadlock-free**.
- **Example:** If $T_1$ (TS=10) tries to read a value written by $T_2$ (TS=20), $T_1$ is rolled back because it is "too old" to see a "future" value.

### 6.3 MVCC (Multiversion Concurrency Control)

- Maintains multiple versions of a data item.
- Readers don't block writers, and writers don't block readers (PostgreSQL/MySQL).
- **Example:** While $T_1$ is updating a row, $T_2$ can still read the "old version" of that row. $T_2$ doesn't have to wait for $T_1$ to finish.

## 7. Deadlock Handling

A **Deadlock** is a stalemate where $T_1$ waits for a lock held by $T_2$, and $T_2$ waits for a lock held by $T_1$.

### 7.1 Deadlock Prevention

Uses timestamps to decide which transaction waits or aborts.

- **Wait-Die (Pessimistic):**
    - If **Older** wants lock held by **Younger**: Older **waits**.
    - If **Younger** wants lock held by **Older**: Younger **dies** (restarts).
- **Wound-Wait (Optimistic):**
    - If **Older** wants lock held by **Younger**: Older **wounds** Younger (forces restart).
    - If **Younger** wants lock held by **Older**: Younger **waits**.

> **Mnemonic:** In **Wait-Die**, the old are patient. In **Wound-Wait**, the old are bullies.

### 7.2 Deadlock Detection

The DBMS allows deadlocks to occur and periodically checks for them using a **Wait-For Graph (WFG)**.

- **Nodes:** Transactions.
- **Edges:** $T_i \rightarrow T_j$ if $T_i$ is waiting for a resource held by $T_j$.
- **Detection:** A **cycle** in the graph indicates a deadlock.

### 7.3 Deadlock Recovery

Once a deadlock is detected, the system must break it:

1. **Selection of a Victim:** Choose the "cheapest" transaction to abort (e.g., least work done).
2. **Rollback:** Undo the victim's changes (Total or Partial).
3. **Starvation Prevention:** Ensure the same transaction isn't always the victim (usually by increasing its priority/age).

| Strategy       | Approach                          | Cost                                           |
| :------------- | :-------------------------------- | :--------------------------------------------- |
| **Prevention** | Stop deadlocks before they start. | High (aborts transactions unnecessarily).      |
| **Detection**  | Let them happen, then find them.  | Moderate (requires scanning Wait-For Graph).   |
| **Avoidance**  | Allocate resources only if safe.  | Very High (requires knowing all future needs). |
