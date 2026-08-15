## 3 essential network protocols for system design : IP, TCP, and HTTP.


### IP (Internet Protocol): 
- AInformation is sent in IP packets, containing headers (source/destination address, size) and data. 
- Packet size is limited, large files must be broken into multiple packets.
### TCP (Transmission Control Protocol): 
- Built on top of IP, it guarantees that data is received in the correct order and without damage. 
- It requires a handshake to establish a connection between the client and server before data transfer begins.
### HTTP (HyperText Transfer Protocol): 
- Provides a high-level abstraction on top of TCP, allowing for a structured request-response paradigm that developers use to build web applications.

### Additional Concepts:
- REST vs. HTTP:  REST is an architectural style for distributed systems, whereas HTTP is the underlying network protocol used for communication.


### What is a TCP handshake?
- A TCP handshake is the essential process of establishing a reliable connection between a client and a server before any actual data transfer begins.
- During this handshake, the machines follow a structured exchange to ensure both parties are ready to communicate:

- Initiation: The client sends a packet to the server to request a connection.
- Acknowledgement: The server responds to confirm that it is available and ready to connect.
- Confirmation: Finally, the client sends a message back to acknowledge the server's response, officially establishing the connection.