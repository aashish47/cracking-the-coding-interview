# 02 Data Link Layer

## 1. Responsibilities (Hop-to-Hop)

- **Framing:** Encapsulating network layer packets into frames.
- **Flow Control:** Managing the pace of data between sender and receiver.
- **Error Control:** Detecting and/or correcting bit errors.
- **Access Control:** Managing access to shared media (MAC).

## 2. Framing (Node-to-Node)

Determines where a frame starts and ends.

| Method              | Mechanism                                                                            | Pros                                                                                | Cons                                                                                         |
| :------------------ | :----------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------- |
| **Character Count** | Header contains the total byte count of the frame.                                   | Simple implementation.                                                              | **Fragile:** One bit error in count causes loss of synchronization for all following frames. |
| **Byte Stuffing**   | Uses `FLAG` (e.g., `0x7E`) to delimit frames and `ESC` to escape data-payload flags. | Resyncs at every `FLAG`; good for variable-length text.                             | High overhead; specific to byte-oriented protocols.                                          |
| **Bit Stuffing**    | Uses flag `01111110`. Inserts a `0` after five consecutive `1`s in data.             | **Robust:** Works at bit-level; prevents data from mimicking flags; lower overhead. | Requires bit-level hardware processing.                                                      |

**Bit Stuffing (Receiver Logic):**

- If five `1`s are followed by a `0`: The `0` is a "stuffed" bit and is **discarded**.
- If five `1`s are followed by a `1`: It indicates a **Flag** (if the next bit is `0`) or an **Error**.

## 3. Ethernet (IEEE 802.3)

### 3.1 Frame Structure

| Preamble | SFD    | Dest Addr | Src Addr | Length/Type | Data(Payload)   | FCS/CRC |
| :------- | :----- | :-------- | :------- | :---------- | :-------------- | :------ |
| 7 Bytes  | 1 Byte | 6 Bytes   | 6 Bytes  | 2 Bytes     | 46 - 1500 Bytes | 4 Bytes |

- **Preamble/SFD:** Synchronization.
- **MAC Address:** 48-bit (6 bytes) physical address.
- **Min Frame Size:** 64 Bytes (Required for CSMA/CD collision detection).

### 3.2 MAC Addressing

- **Unicast:** First byte ends in `0` (e.g., `A2:...`).
- **Multicast:** First byte ends in `1` (e.g., `A3:...`).
- **Broadcast:** All `F`s (`FF:FF:FF:FF:FF:FF`).

## 4. Error Detection & Correction

### 4.1 Parity Check

Appends a single bit to make the total number of 1s even (Even Parity) or odd (Odd Parity). Simple but cannot detect even numbers of bit flips.

**Example:** For data `1101`, Even Parity bit is `1` (total four 1s: `11011`), Odd Parity bit is `0` (total three 1s: `11010`).

### 4.2 Checksum

Used to verify data integrity. The sender divides data into $k$ segments of $n$ bits each.

- **Sender:** Adds all segments using 1's complement arithmetic (any carry-out from the MSB is added back to the LSB). The final result is complemented (flipped) to get the checksum.
- **Receiver:** Adds all segments plus the checksum. If the result is all 1s, the data is accepted.
- **Example (4-bit segments):**
- **Sender:** 1. Data: `1011` and `1101`. 2. Sum: `1011 + 1101 = 11000`. 3. Handle Carry: `1000 + 1 (carry) = 1001`. 4. Checksum (Complement): `~1001 = 0110`.
- **Receiver Check:** Sum: `1011 + 1101 + 0110 = 11110` $\rightarrow$ `1110 + 1 = 1111`. Result is all 1s: **Accepted**.

### 4.3 Cyclic Redundancy Check (CRC)

A powerful method using "binary long division" to catch errors. It treats data as a long number and divides it by a fixed "generator" number.

**The Process:**

1. **Sender:** Picks a generator $G$ (length $n+1$). Appends $n$ zeros to the data.
2. **Divide:** Performs Modulo-2 division (XOR operation) of the data by $G$.
3. **Remainder:** The result of this division is the CRC. The sender replaces the $n$ zeros with this CRC and sends it.
4. **Receiver:** Divides the incoming message by the same generator $G$. If the remainder is **zero**, the data is perfect.

**Example:**

- **Data:** `10110`, **Generator:** `1101` (degree 3).
- **Sender:** Appends three 0s $\rightarrow$ `10110000`. Divides by `1101`.

```text
Modulo-2 Division (XOR):

- If the leftmost bit of the current dividend is 1: Use the Generator (XOR with 1101).
- If the leftmost bit is 0 (The Skip Rule): Use all 0s (XOR with 0000). This effectively "skips" to the next bit.

        11011   (Quotient)
1101|10110000
        1101
        ----
        1101
        1101
        ----
        0001
        0000 (Skip Rule: MSB was 0)
        ----
        0010
        0000 (Skip Rule: MSB was 0)
        ----
            0100
            0000 (Skip Rule: MSB was 0)
            ----
            1000
            1101
            ----
            101 (Remainder/CRC)
```

- **Transmission:** Sender sends `10110` + `101` $\rightarrow$ `10110101`.
- **Receiver:** Divides `10110101` by `1101`. If remainder is `0`, **Accepted**.

- **Strength:** Detects all single-bit errors, burst errors (multiple bits in a row), and most random errors.

| Method         | Strength               | Weakness                                                                    |
| :------------- | :--------------------- | :-------------------------------------------------------------------------- |
| **Parity Bit** | Super simple.          | If two bits flip, it misses the error entirely.                             |
| **Checksum**   | Fast to calculate.     | Can be "fooled" by data being rearranged (1+2 is the same as 2+1).          |
| **CRC**        | Mathematically robust. | Catches "burst errors" (like a spark of static electricity hitting a wire). |

### 4.4 Hamming Distance ($d$)

The number of bit positions in which two **codewords** differ.

_Example:_ $d(10101, 11110) = 3$ (bits 2, 4, and 5 differ).

- **Error Detection ($d_{min} \ge t + 1$):** To detect $t$ errors, the distance between any two valid codewords must be large enough so that $t$ bit flips cannot turn one valid codeword into another valid codeword.

    _Example:_ If $d_{min}=3$, flipping 1 or 2 bits results in an invalid codeword (detected). Flipping 3 bits could result in another valid codeword (undetected).

- **Error Correction ($d_{min} \ge 2t + 1$):** To correct $t$ errors, a corrupted codeword must remain "closer" to the original valid codeword than any other valid codeword.

    _Example:_ If $d_{min}=5$ and $t=2$ errors occur, the received string is distance 2 from the original and at least distance 3 from any other valid codeword. The receiver can uniquely "map" it back to the closest valid one.

### 4.5 Hamming Code

A self-correcting code. Redundant bits ($p$) are placed at positions $2^n$ (1, 2, 4, 8...).

- **The Binary Secret:**

    Every position can be written as a sum of powers of 2 ($1, 2, 4, 8 \dots$).

    | Position | Binary | Sum of Powers of 2 |
    | :------- | :----- | :----------------- |
    | 1        | 001    | 1                  |
    | 2        | 010    | 2                  |
    | 3        | 011    | 1 + 2              |
    | 4        | 100    | 4                  |
    | 5        | 101    | 1 + 4              |
    | 6        | 110    | 2 + 4              |
    | 7        | 111    | 1 + 2 + 4          |

    **Look at the "1s" Column:**
    - Parity 1 checks every position that has a 1 in its binary sum (1, 3, 5, 7).
    - Parity 2 checks every position that has a 2 in its binary sum (2, 3, 6, 7).
    - Parity 4 checks every position that has a 4 in its binary sum (4, 5, 6, 7). (Note: For 7 bits, this is the MSB).

    - **Condition:** $2^p \ge m + p + 1$ (where $m$ = data bits, $p$ = parity bits).

- **Bit Mapping (7,4 Example):**

    | Position   | 1 ($2^0$) | 2 ($2^1$) |   3   | 4 ($2^2$) |   5   |   6   |   7   |
    | :--------- | :-------: | :-------: | :---: | :-------: | :---: | :---: | :---: |
    | **Type**   |   $P_1$   |   $P_2$   | $D_1$ |   $P_4$   | $D_2$ | $D_3$ | $D_4$ |
    | **Binary** |    001    |    010    |  011  |    100    |  101  |  110  |  111  |
    - **Parity Coverage:**
        - $P_1$ checks positions with LSB `1`: (1, 3, 5, 7)
        - $P_2$ checks positions with middle bit `1`: (2, 3, 6, 7)
        - $P_4$ checks positions with MSB `1`: (4, 5, 6, 7)

    - **Hamming (7,4) Walkthrough**

        **1. Encoding (Sender)**
        - **Data:** `1011` ($D_1=1, D_2=0, D_3=1, D_4=1$)
        - **Placement:**
            - Pos 3, 5, 6, 7 $\rightarrow$ `1, 0, 1, 1`
            - Pos 1, 2, 4 $\rightarrow$ `P1, P2, P4` (To be calculated)
        - **Calculations (Even Parity):**
            - $P_1$ (1, 3, 5, 7): $P_1 \oplus 1 \oplus 0 \oplus 1 = 0 \rightarrow \mathbf{P_1 = 0}$
            - $P_2$ (2, 3, 6, 7): $P_2 \oplus 1 \oplus 1 \oplus 1 = 0 \rightarrow \mathbf{P_2 = 1}$
            - $P_4$ (4, 5, 6, 7): $P_4 \oplus 0 \oplus 1 \oplus 1 = 0 \rightarrow \mathbf{P_4 = 0}$
        - **Sent Codeword:** `0110011`

        **2. The Error (Transmission)**
        - Bit at **Position 5** flips: `0110011` $\rightarrow$ `0110111`

        **3. Detection & Correction (Receiver)**
        - **Check $P_1$ (1, 3, 5, 7):** `0, 1, 1, 1` $\rightarrow$ Sum is 3 (Odd). **Result: 1 (Fail)**
        - **Check $P_2$ (2, 3, 6, 7):** `1, 1, 1, 1` $\rightarrow$ Sum is 4 (Even). **Result: 0 (Pass)**
        - **Check $P_4$ (4, 5, 6, 7):** `0, 1, 1, 1` $\rightarrow$ Sum is 3 (Odd). **Result: 1 (Fail)**
        - **The Syndrome:** Read results from highest parity to lowest ($P_4, P_2, P_1$) $\rightarrow$ **`101`**
        - **The Fix:** Binary `101` = Decimal **5**. Flip bit at position 5 back to `0`.
        - **Extraction:** Remove $P_1, P_2, P_4$ to get original data `1011`.

    | Feature      | CRC (Detection)                    | Hamming Code (Correction)          |
    | :----------- | :--------------------------------- | :--------------------------------- |
    | **Overhead** | Very low (few bits for huge data). | Higher (requires many extra bits). |
    | **Action**   | Discard and ask for resend.        | Fix it on the spot.                |
    | **Best Use** | High-speed internet, hard drives.  | ECC RAM, satellite comms, CDs.     |

## 5. Medium Access Control (MAC)

### 5.1 Functions of MAC

- **Channel Partitioning:** Dividing the bandwidth into smaller "pieces" (Time slots, Frequencies).
- **Taking Turns:** Coordinating access to avoid collisions (Token Passing).
- **Random Access:** Allowing nodes to compete for the channel (Collision-based).

### 5.2 Random Access Protocols

| Protocol          | Mechanism                                                | Efficiency ($\eta$) | Key Characteristic                    |
| :---------------- | :------------------------------------------------------- | :------------------ | :------------------------------------ |
| **Pure ALOHA**    | Transmit immediately when data is ready.                 | $18.4\%$            | High collision probability.           |
| **Slotted ALOHA** | Time is divided into slots; transmit only at slot start. | $36.8\%$            | Reduces collision window by half.     |
| **CSMA**          | "Listen Before Talk." Check if carrier is idle.          | Variable            | Doesn't stop if collision starts.     |
| **CSMA/CD**       | CSMA + Collision Detection (Wired/Ethernet).             | High                | Aborts transmission upon collision.   |
| **CSMA/CA**       | CSMA + Collision Avoidance (Wireless/802.11).            | Medium              | Uses Handshaking to avoid collisions. |

**CSMA/CD Deep Dive:**

- **What is a Collision?** A collision occurs when two or more devices on a shared physical medium attempt to transmit data simultaneously. The electrical signals overlap and interfere with each other, resulting in corrupted, unintelligible data that must be discarded and retransmitted.

- **The Collision Detection Rule:** Collision is detected by the **sender** monitoring the signal voltage on the medium; if the observed voltage exceeds the expected voltage of its own signal, a collision has occurred. For a sender to detect this, it must still be transmitting when the collision signal (the "echo" of the crash) travels back from the furthest point.
    - **Condition:** $T_t \ge 2 \times T_p$ (where $T_t$ is Transmission Delay and $T_p$ is Propagation Delay)
    - **Why $2 \times T_p$?** In the worst case, a collision occurs just as the bit reaches the receiver ($1 \times T_p$). The collision signal then needs another $1 \times T_p$ to travel back to the sender.

- **Min Frame Size:** $L_{min} = Bandwidth \times 2 \times T_p$.
- **Backoff:** Uses **Binary Exponential Backoff**. After $n$ collisions, choose $K$ at random from $\{0, 1, 2, \dots, 2^n - 1\}$. Wait time $= K \times 512$ bit times.

**CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance):**

- Uses **RTS (Request to Send)** and **CTS (Clear to Send)** frames: A handshake mechanism where the sender asks for permission (RTS) and the receiver grants it (CTS), notifying all other nodes to remain silent.
- Solves the **Hidden Terminal Problem**: Occurs when two nodes (A and C) are out of range of each other but both can communicate with a central Access Point (B). Without RTS/CTS, A and C might transmit simultaneously to B, causing a collision they cannot detect.

## 6. Devices & Switching

### 6.1 Switching Logic (Learning Bridge)

Switches use a **MAC Table** (also called a Content Addressable Memory or CAM table), which is a database stored in the switch's memory that maps individual MAC addresses to the physical ports they are connected to. It forwards traffic efficiently via four actions:

1. **Learning:** Records source MAC and port from incoming frames.
2. **Filtering:** Drops frame if destination is on the same port as source.
3. **Forwarding:** Sends frame to the specific port matching the destination MAC.
4. **Flooding:** Sends to all ports (except source) if destination MAC is unknown.

### 6.2 Hardware Comparisons

**Bridge vs. Switch**

| Feature            | Bridge (Legacy)    | Switch (Modern)         |
| :----------------- | :----------------- | :---------------------- |
| **Implementation** | Software-based     | Hardware (**ASIC**)     |
| **Role**           | Connects 2 LANs    | Multi-port connectivity |
| **MAC Address**    | None (Transparent) | Manages others' MACs    |
| **Performance**    | Slower             | Wire-speed (ASIC)       |

**NIC vs. ASIC**

| Feature               | NIC (Network Interface Card)     | ASIC (Application-Specific IC)        |
| :-------------------- | :------------------------------- | :------------------------------------ |
| **Where is it?**      | Inside your Computer/Phone/Node. | Inside Switches/Routers.              |
| **What is its role?** | It is an End Point.              | It is the "Engine" of the Middle Man. |
| **Function**          | Connects a device to the wire.   | Processes frames at wire-speed.       |
| **MAC Address**       | Has its own unique MAC address.  | Doesn't have one; processes others'.  |

### 6.3 Network Segmentation

**Key Concepts:**

- **VLAN (802.1Q):** Logically splits one physical switch into multiple broadcast domains.
- **STP (Spanning Tree):** Prevents Layer 2 loops by blocking redundant paths.
- **Trunking:** Carries multiple VLANs over a single physical link between switches.

**Domains Comparison:**

| Device     | Collision Domain | Broadcast Domain |
| :--------- | :--------------- | :--------------- |
| **Hub**    | One (All ports)  | One (All ports)  |
| **Switch** | **Per Port**     | One (Per VLAN)   |
| **Router** | Per Port         | **Per Port**     |
