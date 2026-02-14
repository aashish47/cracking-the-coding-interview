# 04 Transport Layer

## 1. Responsibilities

- **Process-to-Process Delivery:** Delivers data to the specific application using Port Numbers (16-bit).
- **Segmentation:** Breaks application data into segments (MSS - Maximum Segment Size).
- **Reliability:** Ensures error-free and in-order delivery (TCP).
- **Flow Control:** Matches the sender's rate with the receiver's capacity.
- **Congestion Control:** Prevents the network from becoming overwhelmed by too much traffic.
- **Multiplexing/Demultiplexing:** Allowing multiple applications to use the network simultaneously.

## 2. Sockets

- **Definition:** An endpoint for communication, uniquely identified by the combination of an **IP Address** and a **Port Number**.
- **Socket Address:** `IP Address : Port Number` (e.g., `192.168.1.1:80`).
- **Connection:** A TCP connection is uniquely identified by a 5-tuple: `{Source IP, Source Port, Destination IP, Destination Port, Protocol}`.
- **Ephemeral Ports:** Temporary ports (usually 49152–65535) assigned by the OS to client applications.

## 3. Multiplexing & Demultiplexing

**The Problem:** A single computer has only one physical network connection (one IP address), but it runs many applications simultaneously (Browser, Spotify, Zoom). Without a way to distinguish which incoming data belongs to which app, the OS wouldn't know where to deliver the packets.

**The Solution:** Multiplexing and Demultiplexing allow the Transport Layer to act as a "mail sorter," using port numbers to ensure data from different processes can share the same network pipe without getting mixed up.

- **Multiplexing (at Sender):** Gathering data from multiple sockets, enveloping data with header (including ports) to create segments, and passing them to the Network Layer.
- **Demultiplexing (at Receiver):** Delivering received segments to the correct socket by examining the port numbers and IP addresses.
    - **UDP Demultiplexing:** Uses only the **Destination Port** and **Destination IP** to direct the segment to a socket.
    - **TCP Demultiplexing:** Uses the full **5-tuple**: `{Source IP, Source Port, Destination IP, Destination Port, Protocol}`.
      This allows a web server to support many simultaneous TCP sockets all mapped to the same port (e.g., 80), each associated with a different connecting client.

## 4. Connection Management (TCP)

### 4.1 The 3-Way Handshake (Establishment)

1.  **SYN:** Client sends a segment with `SYN=1` and a random `Initial Sequence Number (ISN_c)`.
2.  **SYN-ACK:** Server responds with `SYN=1`, `ACK=1`, `Ack Number = ISN_c + 1`, and its own `ISN_s`.
3.  **ACK:** Client sends `ACK=1`, `Ack Number = ISN_s + 1`. Connection is now **Established**.

### 4.2 Connection Teardown (4-Way Termination)

1.  **FIN:** Side A sends `FIN` to close its data stream.
2.  **ACK:** Side B acknowledges.
3.  **FIN:** Side B sends its own `FIN` when finished sending data.
4.  **ACK:** Side A acknowledges and enters `TIME_WAIT` state to ensure the ACK was received.

### 4.3 TCP Flags

- **SYN:** Synchronize sequence numbers (Connection setup).
- **ACK:** Acknowledgment field is valid.
- **FIN:** No more data from sender (Termination).
- **RST:** Reset the connection (Error/Abrupt close).
- **PSH:** Push data to application immediately.
- **URG:** Urgent pointer field is valid.

## 4. Segment Structure

### TCP Header Fields (20-60 Bytes)

| Field               | Size (Bits) | Description                                                       |
| :------------------ | :---------- | :---------------------------------------------------------------- |
| **Source Port**     | 16          | Port of the sending application.                                  |
| **Dest Port**       | 16          | Port of the receiving application.                                |
| **Sequence Number** | 32          | Byte-stream number of the first data byte in the segment.         |
| **Ack Number**      | 32          | Next expected byte number from the other side.                    |
| **Data Offset**     | 4           | Header length (number of 32-bit words).                           |
| **Flags**           | 6-9         | Control bits (URG, ACK, PSH, RST, SYN, FIN).                      |
| **Window Size**     | 16          | Number of bytes the receiver is willing to accept (Flow Control). |
| **Checksum**        | 16          | Error checking for header and data.                               |
| **Urgent Pointer**  | 16          | Points to the end of urgent data.                                 |
| **Options**         | Variable    | Max Segment Size (MSS), Window Scaling, etc.                      |

### UDP Header Fields (8 Bytes)

| Field           | Size (Bits) | Description                                         |
| :-------------- | :---------- | :-------------------------------------------------- |
| **Source Port** | 16          | Port of the sending application.                    |
| **Dest Port**   | 16          | Port of the receiving application.                  |
| **Length**      | 16          | Total length of the UDP segment (Header + Data).    |
| **Checksum**    | 16          | Error checking for header and data (Optional IPv4). |

---

## 5. Protocols

### Comparison: TCP vs. UDP

| Feature          | TCP (Transmission Control Protocol)   | UDP (User Datagram Protocol) |
| :--------------- | :------------------------------------ | :--------------------------- |
| **Connection**   | Connection-oriented (3-way handshake) | Connectionless               |
| **Reliability**  | Reliable (ACKs, Retransmission)       | Unreliable (Best effort)     |
| **Header Size**  | 20-60 Bytes                           | Fixed 8 Bytes                |
| **Data Flow**    | Byte Stream                           | Datagram (Message-based)     |
| **Speed**        | Slower (due to overhead/checks)       | Faster (low overhead)        |
| **Flow Control** | Yes (Sliding Window)                  | No                           |
| **Congestion**   | Yes (Slow Start, Avoidance)           | No                           |
| **Ordering**     | Guaranteed in-order delivery          | No guarantee                 |
| **Use Cases**    | HTTP, FTP, SMTP, SSH                  | DNS, VoIP, Gaming, Streaming |

## 6. Flow Control

Flow Control is a speed-matching mechanism. It ensures a fast sender doesn't "drown" a slow receiver by sending data faster than the receiver can process it.

It happens primarily at the Transport Layer (end-to-end), but can occasionally be seen at the Data Link Layer (hop-by-hop).

### 6.1 Sliding Window

TCP uses a Sliding Window to manage this. The process follows these four steps:

1.  **Buffering:** The receiver sets aside a chunk of memory (the Receive Buffer).
2.  **Advertising:** In every message (ACK) sent back to the sender, the receiver includes a value called the **Receive Window ($rwnd$)**. This number tells the sender exactly how much empty space is left in that buffer.
3.  **Sending:** The sender is strictly forbidden from having more "in-flight" data than the $rwnd$ allows.
4.  **Consuming:** As the application (like your browser) pulls data out of the buffer, space clears up, the $rwnd$ increases, and the receiver tells the sender, "Okay, you can speed up now."

### 6.2 Error Recovery Strategies

When data loss occurs, the protocol employs specific ARQ (Automatic Repeat Request) mechanisms to ensure reliability:

| Strategy             | Mechanism                                                                                                                                                                    | Performance                                            |
| :------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------- |
| **Stop-and-Wait**    | Sender transmits a single segment and waits for an acknowledgment before sending the next.                                                                                   | Low efficiency; high idle time.                        |
| **Go-Back-N**        | Sender transmits multiple segments (window). On failure, the receiver discards all subsequent segments; sender retransmits the entire window starting from the lost segment. | Moderate efficiency; simple receiver logic.            |
| **Selective Repeat** | Sender transmits multiple segments. Receiver buffers out-of-order segments and requests retransmission only for the specific lost segment.                                   | High efficiency; requires complex buffering and logic. |

## 7. Congestion Control

**Congestion Control** prevents the network (routers/links) from becoming overwhelmed, which leads to packet loss and long delays.

### 7.1 The Congestion Window ($cwnd$)

The sender maintains $cwnd$ to limit the amount of data in flight. Unlike $rwnd$ (which is explicit), $cwnd$ is a **dynamic guess** based on perceived network health.

#### 7.1.1 Key Terms

- **MSS (Maximum Segment Size):** The largest amount of data (in bytes) that a communications device can handle in a single, unfragmented piece.
- **cwnd (Congestion Window):** A TCP state variable that limits the amount of data the sender can transmit into the network before receiving an ACK.
- **ssthresh (Slow Start Threshold):** The threshold that determines whether TCP uses the Slow Start or Congestion Avoidance algorithm to control data flow.
- **RTT (Round Trip Time):** The time it takes for a signal to be sent plus the time it takes for an acknowledgment of that signal to be received.

### 7.2 The Four Phases of TCP Congestion Control

| Phase                       | Trigger                            | Action                                                               | Growth      |
| :-------------------------- | :--------------------------------- | :------------------------------------------------------------------- | :---------- |
| **1. Slow Start**           | Connection start or after Timeout. | Start with 1 MSS. Double $cwnd$ every RTT until $cwnd \ge ssthresh$. | Exponential |
| **2. Congestion Avoidance** | $cwnd \ge ssthresh$.               | Increase $cwnd$ by 1 MSS every RTT (Additive Increase).              | Linear      |
| **3. Fast Retransmit**      | 3 Duplicate ACKs received.         | Retransmit missing segment immediately.                              | -           |
| **4. Fast Recovery**        | After Fast Retransmit.             | Set $ssthresh = cwnd/2$, set $cwnd = ssthresh$.                      | Linear      |

### 7.3 Handling Packet Loss

TCP interprets packet loss as a signal of congestion. The reaction depends on how the loss was detected:

1.  **Timeout (Severe Congestion):**
    - $ssthresh$ is set to $cwnd / 2$.
    - $cwnd$ is reset to **1**.
    - Enters **Slow Start**.
2.  **3 Duplicate ACKs (Mild Congestion):**
    - $ssthresh$ is set to $cwnd / 2$.
    - $cwnd$ is set to $ssthresh$ (skipping the reset to 1).
    - Enters **Fast Recovery**.

### 7.4 AIMD (Additive Increase Multiplicative Decrease)

TCP's behavior of linear growth (Congestion Avoidance) and sudden halving (on 3 Duplicate ACKs) creates a **Sawtooth Pattern** in the congestion window over time. This ensures the sender constantly probes for more bandwidth but backs off quickly to prevent collapse.

## 8. Flow Control vs. Congestion Control

| Feature                     | **Flow Control**             | **Congestion Control**                    |
| --------------------------- | ---------------------------- | ----------------------------------------- |
| **Who is being protected?** | The Receiver (the "Bucket"). | The Network (the "Pipes").                |
| **Who decides the limit?**  | The Receiver ($rwnd$).       | The Sender ($cwnd$).                      |
| **Main Signal**             | Explicit "Stop/Go" messages. | Packet loss (Timeouts or Duplicate ACKs). |
| **Mechanism**               | Sliding Window ($rwnd$)      | Slow Start, Avoidance ($cwnd$)            |
