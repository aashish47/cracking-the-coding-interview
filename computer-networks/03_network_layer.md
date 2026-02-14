# 03 Network Layer

## 1. Responsibilities (Host-to-Host)

- **Routing:** Determining the best path for packets across multiple networks.
- **Logical Addressing:** Assigning IP addresses to identify hosts and networks.
- **Fragmentation:** Breaking large packets into smaller pieces to fit the MTU of a link.
- **Inter-networking:** Connecting different types of physical networks.

## 2. Routing

### 2.1 Routing Strategies & Algorithms

Routing is the process of selecting paths in a network to send data.

- **Flooding:** Every incoming packet is sent out on every outgoing line except the one it arrived on.
    - _Pros:_ Highly robust, ensures delivery. _Cons:_ Extremely high traffic/overhead.
- **Distance Vector (Bellman-Ford):** Routers share their entire routing table with neighbors periodically.
    - **Example:** Router A knows it can reach B in 1 hop. It tells neighbor C: "I can reach B in 1 hop." C then knows it can reach B via A in 2 hops ($1+1$).
- **Link State (Dijkstra's Algorithm):** Routers build a complete map (topology) of the network and calculate the shortest path.
    - **Example:** Every router sends a "Link State Packet" (LSP) describing its immediate neighbors and costs. Router A receives LSPs from everyone, builds a full graph of the network, and runs Dijkstra's to find the best path to every other node.
- **Path Vector:** Tracks the sequence of Autonomous Systems (AS) to avoid loops and apply policies.

#### Algorithm Comparison: Bellman-Ford vs. Dijkstra

| Feature            | Bellman-Ford (Distance Vector)      | Dijkstra (Link State)                    |
| :----------------- | :---------------------------------- | :--------------------------------------- |
| **Knowledge**      | Only knows distance to neighbors.   | Knows the entire network topology.       |
| **Updates**        | Periodic (even if no change).       | Event-triggered (only on change).        |
| **Complexity**     | $O(V \times E)$                     | $O(E \log V)$ or $O(V^2)$                |
| **Negative Edges** | Can handle negative weights.        | Cannot handle negative weights.          |
| **Robustness**     | A single wrong entry can propagate. | More robust; errors don't spread easily. |

#### Dijkstra's Step-by-Step Example

**Goal:** Find shortest path from Source **A** to all nodes.

1.  **Initialization:** Set distance to A = 0, all others = $\infty$. Mark all nodes unvisited.
2.  **Selection:** Pick the unvisited node with the smallest distance (starts with A).
3.  **Relaxation:** For the current node, check all its unvisited neighbors. If `Dist(Current) + Edge(Current, Neighbor) < Dist(Neighbor)`, update the neighbor's distance.
4.  **Finalize:** Mark current node as visited. Repeat until all nodes are visited.

#### Bellman-Ford Step-by-Step Example

**Goal:** Find shortest path from Source **S** to all nodes in a graph with $V$ vertices.

1.  **Initialization:** Set distance to S = 0, all others = $\infty$.
2.  **Relaxation:** Repeat the following $V-1$ times:
    - For every edge $(u, v)$ with weight $w$:
    - If `Dist(u) + w < Dist(v)`, then `Dist(v) = Dist(u) + w`.
3.  **Negative Cycle Check:** Run relaxation one more time. If any distance decreases, a negative cycle exists (path cost is $-\infty$).

### 2.2 Comparison of Routing Protocols

| Protocol | Full Form                    | Algorithm       | Metric             | Scope | Convergence              |
| :------- | :--------------------------- | :-------------- | :----------------- | :---- | :----------------------- |
| **RIP**  | Routing Information Protocol | Distance Vector | Hop Count (Max 15) | IGP   | Slow (Count-to-infinity) |
| **OSPF** | Open Shortest Path First     | Link State      | Cost (Bandwidth)   | IGP   | Fast                     |
| **BGP**  | Border Gateway Protocol      | Path Vector     | Policy/Attributes  | EGP   | Slow (Global Scale)      |

_Note: **IGP** (Interior Gateway Protocol) is used within an organization; **EGP** (Exterior Gateway Protocol) is used between organizations._

### 2.3 Real-World Application

1. **Home/Small Office:** Usually **Static Routing** (manually configured) or simple RIP.
2. **Enterprise/Campus:** **OSPF** is the standard for fast, smart internal routing.
3. **Global Internet:** **BGP** is the "glue" that connects Internet Service Providers (ISPs).

### 2.4 Key Terminology

- **Autonomous System (AS):** A collection of IP networks under the control of a single entity (e.g., Google, an ISP).
- **Convergence:** The state where all routers have consistent and updated routing information after a change.
- **Count-to-Infinity:** A problem in Distance Vector routing where a routing loop causes hop counts to increase indefinitely.

## 3. IPv4 & IPv6 Addressing

- **IPv4 (Internet Protocol version 4):** A 32-bit logical address represented in dotted-decimal format (e.g., 192.168.1.1).
- **Classful Addressing:**
    - **Class A:** Range 0-127 | Net ID: 8 bits | Host ID: 24 bits (Large networks)
    - **Class B:** Range 128-191 | Net ID: 16 bits | Host ID: 16 bits (Medium networks)
    - **Class C:** Range 192-223 | Net ID: 24 bits | Host ID: 8 bits (Small networks)
    - **Class D:** Range 224-239 | Reserved for Multicasting.
    - **Class E:** Range 240-255 | Reserved for Experimental use.

- **CIDR (Classless Inter-Domain Routing):** Notation `A.B.C.D/n`.
    - `/n` is the subnet mask (number of network bits).
    - Number of hosts = $2^{(32-n)} - 2$ (Subtract Network and Broadcast addresses).

        _Note: Network address is all 0s in host bits, Broadcast address is all 1s in host bits._

- **Subnetting Example:**
    - **Given:** `192.168.1.0/26`
    - **Subnet Mask:** `255.255.255.192` (11111111.11111111.11111111.11000000)
    - **Total Hosts:** $2^{(32-26)} = 2^6 = 64$.
    - **Usable Hosts:** $64 - 2 = 62$.

- **IPv6 (Internet Protocol version 6):** A 128-bit address represented in hexadecimal (e.g., `2001:0db8:85a3:0000:0000:8a2e:0370:7334`).
    - **Address Space:** $2^{128}$ addresses.
    - **Features:** No fragmentation by routers (only source), no checksum (handled by upper layers), built-in IPsec support, and no broadcast (uses multicast/anycast).
    - **CIDR Notation:**
        - Uses a prefix length (e.g., `/64`) to denote the network portion.
        - Example: `2001:db8:abcd:12::/64`.
    - **Address Compression:**
        - Leading zeros in a block can be omitted (e.g., `:0db8:` becomes `:db8:`).
        - Consecutive blocks of zeros can be replaced by `::` (only once per address).
    - **IPv4 vs IPv6 Header Comparison**

| Feature           | IPv4 Header                         | IPv6 Header                       |
| :---------------- | :---------------------------------- | :-------------------------------- |
| **Size**          | Variable (20 to 60 bytes)           | Fixed (40 bytes)                  |
| **Fragmentation** | Handled by routers and source       | Handled by source only            |
| **Checksum**      | Included (recalculated at each hop) | Removed (handled by upper layers) |
| **Lifetime**      | Time to Live (TTL)                  | Hop Limit                         |
| **Options**       | Included in header (variable size)  | Extension Headers                 |

## 5. Packet Structure

- **IPv4 packet size:** 20 to 65,535 bytes.
- **IPv6 packet size:** 1280 to 65,535 bytes.

### IPv4 Header Fields

| Field               | Size (Bits) | Description                                                                     |
| :------------------ | :---------- | :------------------------------------------------------------------------------ |
| **Version**         | 4           | Indicates the IP version (e.g., 4 for IPv4).                                    |
| **IHL**             | 4           | Internet Header Length; length of the header in 32-bit words (Min: 5, Max: 15). |
| **Type of Service** | 8           | Used for Quality of Service (QoS) and priority.                                 |
| **Total Length**    | 16          | Total size of the datagram (Header + Data) in bytes.                            |
| **Identification**  | 16          | Unique ID for identifying fragments of a single datagram.                       |
| **Flags**           | 3           | Control flags for fragmentation (Reserved, Don't Fragment, More Fragments).     |
| **Fragment Offset** | 13          | Indicates where in the original datagram this fragment belongs.                 |
| **Time to Live**    | 8           | Hop counter to prevent infinite loops.                                          |
| **Protocol**        | 8           | Indicates the next level protocol (e.g., TCP=6, UDP=17).                        |
| **Header Checksum** | 16          | Error-checking for the header only.                                             |
| **Source IP**       | 32          | IP address of the sender.                                                       |
| **Destination IP**  | 32          | IP address of the intended receiver.                                            |
| **Options**         | Variable    | Optional padding or extra features (e.g., Record Route).                        |

### IPv6 Header Fields

| Field              | Size (Bits) | Description                                                          |
| :----------------- | :---------- | :------------------------------------------------------------------- |
| **Version**        | 4           | Indicates the IP version (6 for IPv6).                               |
| **Traffic Class**  | 8           | Used for Quality of Service (QoS) management.                        |
| **Flow Label**     | 20          | Identifies a sequence of packets (flow) for special handling.        |
| **Payload Length** | 16          | Size of the payload (data + extension headers) in bytes.             |
| **Next Header**    | 8           | Identifies the type of header immediately following the IPv6 header. |
| **Hop Limit**      | 8           | Replaces IPv4 TTL; decremented by 1 at each router.                  |
| **Source Address** | 128         | 128-bit address of the sender.                                       |
| **Dest Address**   | 128         | 128-bit address of the receiver.                                     |

### 6. Fragmentation

Occurs when Packet Size > MTU (Maximum Transmission Unit).

#### 6.1 How Fragmentation Works

When a router realizes a packet is bigger than the outgoing interface's MTU, it performs the following steps:

1. **Slicing:** The router divides the IP payload into smaller chunks.
2. **Re-headering:** It copies the original IP header into each fragment.
3. **Flagging:** It adjusts specific fields in the IP header so the receiving end knows how to put the "puzzle" back together.

#### 6.2 Key Header Fields Involved

To ensure the destination can reconstruct the original data, three fields in the IPv4 header are crucial:

- **Identification (16 bits):** All fragments of the same original packet share the same ID number.
- **Flags (3 bits):** Specifically the **More Fragments (MF)** bit. If it's 1, more pieces are coming; if it's 0, this is the last piece. There is also a **Don't Fragment (DF)** bit; if this is set and the packet is too big, the router simply drops it and sends an error message.
- **Fragment Offset (13 bits):** This tells the receiver exactly where this specific chunk fits in the original packet. It is measured in units of 8 bytes (Position in original data / 8).
    - _Note: Offset must be a multiple of 8 bytes._

#### 6.3 Fragmentation: IPv4 vs. IPv6

There is a massive difference in how the two protocols handle this:

| Feature            | IPv4                                        | IPv6                                                         |
| ------------------ | ------------------------------------------- | ------------------------------------------------------------ |
| **Who Fragments?** | Both source hosts and intermediate routers. | **Only** the source host.                                    |
| **Router Role**    | Routers slice packets on the fly if needed. | Routers drop the packet and send a "Packet Too Big" message. |
| **Efficiency**     | Slower (routers spend CPU cycles slicing).  | Faster (routers just forward or drop).                       |

#### 6.4 Why is Fragmentation "Bad"?

While fragmentation is a necessary fallback, network engineers generally try to avoid it for several reasons:

- **Overhead:** Every fragment needs its own header, increasing the total amount of data sent.
- **CPU Strain:** Routers and receiving hosts have to use extra processing power to fragment and reassemble.
- **Packet Loss:** If even **one** fragment is lost or corrupted, the entire original packet is useless and must be retransmitted.
- **Security:** Some firewalls struggle to inspect fragments because the transport layer info (like TCP ports) is only in the very first fragment.

#### 6.5 The Modern Solution: PMTUD

Most modern systems use **Path MTU Discovery (PMTUD)**. Instead of letting routers fragment packets, the source host sends packets with the "Don't Fragment" bit set to "scout" the path. If it hits a bottleneck, it receives an error, learns the smaller MTU, and adjusts its size from the start.

## 7. Support Protocols

- **ARP (Address Resolution Protocol):** IP Address $\rightarrow$ MAC Address. (Broadcast Request, Unicast Reply).
- **DHCP (Dynamic Host Configuration Protocol):** Assigns IP, Subnet Mask, Gateway, DNS to hosts. (DORA process: Discover, Offer, Request, Acknowledge).
- **ICMP (Internet Control Message Protocol):** Used for error reporting (TTL expired, Dest Unreachable) and queries (Ping/Echo). Does _not_ correct errors.
- **NAT (Network Address Translation):** Maps private IPs (LAN) to public IPs (WAN). Solves IPv4 exhaustion.
