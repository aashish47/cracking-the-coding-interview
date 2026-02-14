# 01 Basics Layering Switching

## 1. Concept of Layering

### OSI Model (Open Systems Interconnection) - The Theoretical Framework

A 7-layer theoretical reference model developed by ISO to standardize communication functions. It provides a modular framework where each layer performs specific tasks and serves the layer above it.
_Mnemonic: Please Do Not Throw Sausage Pizza Away_

| Layer | Name             | PDU (Unit) | Key Responsibility                                       | Protocols/Devices |
| :---- | :--------------- | :--------- | :------------------------------------------------------- | :---------------- |
| 7     | **Application**  | Data       | Direct interaction with software (Browsers/Email).       | HTTP, FTP, SMTP   |
| 6     | **Presentation** | Data       | Ensures data is in a readable format (Syntax/Semantics). | SSL/TLS, JPEG     |
| 5     | **Session**      | Data       | Manages connections (Start, Stop, Restart).              | RPC, NetBIOS      |
| 4     | **Transport**    | Segment    | Reliability, segmentation, and reassembly.               | TCP, UDP          |
| 3     | **Network**      | Packet     | Finding the best path (Routing) across networks.         | IP, Routers       |
| 2     | **Data Link**    | Frame      | Error-free transfer between two physically linked nodes. | Ethernet, Switch  |
| 1     | **Physical**     | Bit        | Transmission of raw bits over a physical medium.         | Hubs, Cables      |

### TCP/IP Model - The Real-World Implementation

The actual protocol suite used by the Internet today. It is more streamlined than OSI.

1.  **Application Layer**: Handles high-level protocols (Combines OSI 5, 6, 7).
2.  **Transport Layer**: Manages end-to-host communication (TCP/UDP).
3.  **Internet Layer**: Handles routing and logical addressing (IP).
4.  **Link Layer**: Handles physical hardware and MAC addressing (Combines OSI 1, 2).

---

## 2. What is Switching?

Switching is the process of forwarding data arriving on one input port to a specific output port that leads to the intended destination. It enables the connection of multiple devices in a network without requiring a direct physical link between every pair of nodes.

---

## 3. Switching Techniques

### Circuit Switching

- **Mechanism:** A dedicated physical path (channel) is reserved between two nodes for the entire duration of the communication.
- **Phases:** Setup -> Data Transfer -> Teardown.
- **Pros:** Guaranteed bandwidth, zero congestion once connected, in-order delivery.
- **Cons:** Inefficient (resources are blocked even if no data is sent), long setup time.
- **Example:** PSTN (Telephone networks).

### Packet Switching (Datagram)

- **Mechanism:** Data is broken into small "packets." Each packet contains a destination address and can take different paths to reach the target.
- **Pros:** Highly efficient (multiple users share the same link), resilient to link failures.
- **Cons:** Packets may arrive out of order, potential for congestion/delay (jitter).
- **Example:** The Internet (IP).

### Virtual Circuit Switching

- **Mechanism:** A hybrid approach. A logical path is "pre-planned" during a setup phase. All packets follow this same path using a Virtual Circuit Identifier (VCI).
- **Pros:** Guaranteed in-order delivery, faster forwarding (switches look at short VCIs instead of long IP addresses).
- **Cons:** If a single switch on the path fails, the entire connection is lost.
- **Example:** X.25, Frame Relay, ATM.

---

## 4. Network Devices

- **Hub (Layer 1):** Non-intelligent device; broadcasts all incoming data to every port. High collision domain.
- **Switch (Layer 2):** Intelligent device; uses MAC addresses to forward frames to specific ports. Reduces collisions.
- **Bridge (Layer 2):** Connects two LAN segments; filters traffic based on MAC addresses to reduce traffic on segments.
- **Router (Layer 3):** Connects different networks; uses IP addresses to determine the best path for packets.
- **Gateway:** A node that acts as an entrance to another network, often performing protocol translation (e.g., connecting a LAN to the Internet).
