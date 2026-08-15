## 3 essential network protocols for system design : IP, TCP, and HTTP.


### IP (Internet Protocol): 
- Information is sent in IP packets, containing headers (source/destination address, size) and data. 
- Packet size is limited, large files  broken into multiple packets.
### TCP (Transmission Control Protocol): 
- Built on top of IP, data is received in the correct order without damage. 
- It requires a handshake to establish a connection between the client and server, before data transfer begins.
- reliable delivery, but gets slow if 1 packet in streams is lost.
### HTTP (HyperText Transfer Protocol): 
- Provides a high-level abstraction on top of TCP,
- standard protocol for transferring text and data across the web.
- allowing for a structured request-response that developers (java, python) use to build web applications.


### What is a TCP Handshake?
- Essential process of establishing a reliable connection between a client and a server before any actual data transfer begins.
- During this handshake, the machines follow a structured exchange to ensure both parties are ready to communicate:

- Initiation: The client sends a packet to the server to request a connection.
- Acknowledgement: The server responds to confirm that it is available and ready to connect.
- Confirmation: Finally, the client sends a message back to the server's response, officially establishing the connection.

### Additional Concepts:
### REST vs. HTTP:
- REST is an architectural style for distributed systems,
- whereas HTTP is the underlying network protocol used for communication.


## Transition to QUIC (Quick UDP Internet Connections):
-  previous versions relied on TCP, HTTP/3 replaces TCP with QUIC , which operates over UDP (User Datagram Protocol).

### Key Issues Solved: Head-of-Line (HoL) Blocking :
- HTTP/1.1 : Suffers HOL, client sends one request at one time over a TCP connection, if one completes than second can come. 
- HTTP/2 : Solves  application-level HOL blocking, by Multiplexing, client can request data and download it simultaneously, transfers as many packets over a single TCP connections,
- HTTP/3 Solution via HTTP/2 + QUIC : Supports ORTTs (0 Round Trip Time), handles streams independently, If a packet in a stream is lost, only that stream is delayed—other streams does not stop.
