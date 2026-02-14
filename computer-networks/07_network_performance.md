# 07 Network Performance

## 1. Bandwidth vs. Throughput

- **Bandwidth:** The maximum theoretical capacity of a link to carry data. Usually measured in bits per second (bps).
    - _Analogy:_ The width of a pipe.
- **Throughput:** The actual amount of data successfully moved from one place to another in a given time period.
    - _Analogy:_ The amount of water actually flowing through the pipe (affected by clogs, pressure, etc.).
    - **Goodput:** The amount of useful application-level data delivered (excludes protocol overhead like headers).

## 2. Latency (Delay)

The time it takes for a message to travel from sender to receiver. Total Latency = $T_{prop} + T_{trans} + T_{queue} + T_{proc}$.

1.  **Propagation Delay ($T_{prop}$):** Time for a bit to travel through the medium.
    - Formula: $T_{prop} = \frac{\text{Distance (d)}}{\text{Speed of Signal (s)}}$
2.  **Transmission Delay ($T_{trans}$):** Time to push all bits of the packet onto the link.
    - Formula: $T_{trans} = \frac{\text{Packet Size (L)}}{\text{Bandwidth (B)}}$
3.  **Queuing Delay ($T_{queue}$):** Time spent waiting in a router's buffer before processing. Highly variable depending on congestion.
4.  **Processing Delay ($T_{proc}$):** Time for the router to check headers, determine output port, and check for errors.

## 3. Bandwidth-Delay Product (BDP)

- **Definition:** Defines the maximum amount of data that can be on the link at any given time.
- **Formula:** $BDP = \text{Bandwidth} \times T_{prop}$
- **Significance:** Important for TCP tuning. It represents the "volume" of the pipe. To fully utilize the link, the sender must send this much data before waiting for the first acknowledgment.

## 4. Jitter

- **Definition:** The variation in the delay of received packets.
- **Impact:** Critical for real-time applications (VoIP, Video Streaming).
- **Mitigation:** Buffering at the receiver (Jitter Buffer) to smooth out arrival times.

## 5. Packet Loss

- **Definition:** The percentage of packets sent that fail to reach their destination.
- **Causes:**
    - **Congestion:** Router buffers fill up and drop new packets (Tail Drop).
    - **Errors:** Bit errors on the physical link (detected and discarded).
- **Effect:** Triggers retransmissions in TCP (lowering throughput); causes artifacts/skips in UDP streams.
