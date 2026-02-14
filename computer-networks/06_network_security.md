# 06 Network Security

## 1. Cryptography Basics

- **Plaintext vs. Ciphertext:** The original readable message vs. the encrypted unreadable output.

- **Symmetric Encryption:** Uses a **single shared key** for both encryption and decryption (e.g., AES, DES).
    - _Pros:_ Extremely fast; ideal for large data.
    - _Cons:_ Requires a secure way to share the key (The Key Distribution Problem).

- **Asymmetric Encryption:** Uses a **Key Pair**: a Public Key (to encrypt) and a Private Key (to decrypt) (e.g., RSA, Elliptic Curve).
    - _Pros:_ No need to share secret keys; enables digital signatures.
    - _Cons:_ Computationally slow; usually used only for the initial handshake.

## 2. Message Integrity & Authentication

- **Hash Functions:** A one-way function producing a fixed-size string (MD5, SHA-256).
    - **Integrity:** Verified via the **Avalanche Effect** (small input change = massive hash change).
    - **Collision Resistance:** It should be nearly impossible for two different inputs to produce the same hash.

- **Digital Signature:** A hash of a message encrypted with the sender's **Private Key**.
    - **Authentication:** Proves the sender's identity.
    - **Non-Repudiation:** The sender cannot deny the message since only they have the private key.

- **Digital Certificates:** A file that binds a Public Key to an identity, signed by a **Certificate Authority (CA)**. This prevents Man-in-the-Middle (MITM) attacks by ensuring you aren't using a "fake" public key.

## 3. Network Security Protocols

- **Firewalls:** Monitors/filters traffic based on rules.
    - _Stateless (Packet Filter):_ Inspects IP/Port in isolation. Fast but "dumb."
    - _Stateful (SPI):_ Tracks the "state" of a connection (e.g., is this packet part of an existing TCP handshake?).
    - _Application Gateway (Proxy):_ Inspects Layer 7 content (e.g., blocking specific SQL commands in an HTTP request).

- **IPSec (Layer 3):** Used primarily for VPNs.
    - _Transport Mode:_ Encrypts only the payload.
    - _Tunnel Mode:_ Encrypts the **entire packet** (payload + original headers) and adds a new IP header.

- **SSL/TLS (Transport/Application Layer):**
    1. **Handshake:** Agreement on cipher suites and version.
    2. **Authentication:** Server sends its Certificate.
    3. **Key Exchange:** Uses Asymmetric encryption (RSA or Diffie-Hellman) to establish a "Pre-master Secret."
    4. **Session Key:** Both parties derive a **Symmetric Session Key**.
    5. **Secure Transmission:** Data flows using the fast symmetric key (e.g., HTTPS).

## 4. Types of Attacks

- **Passive Attacks:** Goal is to intercept info without changing it.
    - _Eavesdropping:_ Sniffing packets.
    - _Traffic Analysis:_ Guessing intent based on communication frequency/volume.

- **Active Attacks:** Goal is to alter data or disrupt service.
    - **Masquerade:** Faking an identity (spoofing).
    - **Replay:** Capturing a valid session (like a login) and "re-playing" it later to gain access. (Thwarted by **Nonces** or timestamps).
    - **Modification:** Altering the message content.
    - **Denial of Service (DoS/DDoS):** Overwhelming a server so legitimate traffic can't get through.
