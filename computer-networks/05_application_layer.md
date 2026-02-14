# 05 Application Layer

## 1. DNS (Domain Name System)

- **Function:** A distributed database that maps Hostname (www.google.com) $\rightarrow$ IP Address.
- **Transport:** Uses UDP port 53 for queries (fast), TCP port 53 for Zone Transfers.
- **Hierarchy:** Root (.) $\rightarrow$ TLD (.com, .org) $\rightarrow$ Authoritative.
- **Resolution Types:**
    - **Recursive:** The DNS server does all the work to find the IP and returns it to the client.
    - **Iterative:** The DNS server returns the address of the next DNS server in the hierarchy for the client to ask.

## 2. Email Protocols

- **SMTP (Simple Mail Transfer Protocol):**
    - **Port:** 25.
    - **Type:** Push protocol (Client to Server, Server to Server).
    - **Encoding:** Requires MIME for non-text data.
- **POP3 (Post Office Protocol):**
    - **Port:** 110.
    - **Type:** Pull protocol. Downloads and (usually) deletes from server.
- **IMAP (Internet Message Access Protocol):**
    - **Port:** 143.
    - **Type:** Pull protocol. Manages email on server (syncs folders).

## 3. HTTP (HyperText Transfer Protocol)

- **Port:** 80 (HTTP), 443 (HTTPS).
- **Characteristics:** Stateless.
- **Methods:** GET, POST, PUT, DELETE, HEAD.
- **Persistence:**
    - **Non-Persistent (HTTP 1.0):** One object per TCP connection. Requires 2 RTTs per object.
    - **Persistent (HTTP 1.1):** Multiple objects over a single TCP connection.
    - **HTTP/2:** Uses multiplexing to send multiple requests over one connection simultaneously.
- **Cookies:** Used to maintain state (e.g., shopping carts, logins) on a stateless protocol.

## 4. FTP (File Transfer Protocol)

- **Architecture:** Out-of-band control.
- **Connections:**
    1.  **Control Connection (Port 21):** Persistent, sends commands.
    2.  **Data Connection (Port 20):** Opened/Closed for every file transfer.

## 5. Other Key Protocols

- **Telnet (Port 23):** Remote terminal access; sends data in plaintext (Insecure).
- **SSH (Secure Shell - Port 22):** Secure alternative to Telnet; uses encryption.
- **SNMP (Simple Network Management Protocol - Port 161/162):** Used for managing and monitoring network devices.
- **TFTP (Trivial FTP - Port 69):** Simplified version of FTP using UDP; no authentication.
