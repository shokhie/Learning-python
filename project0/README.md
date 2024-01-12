# Project 0
Playing with [sockets](https://en.wikipedia.org/wiki/Network_socket).

## What is a socket ?
If two processes want to communicate with each other, they do it using
sockets. There are many ways in which inter-process 
communincation ([ipc](https://en.wikipedia.org/wiki/Inter-process_communication#Approaches)) 
can be acheived but for cross platform communications, sockets are the best. 

If you want to understand it, think it as an endpoint for sending and receiving data across the network.

### Socket types
+ Datagram sockets - Connectionless sockets, which uses User Datagram Protocol(UDP). Used for 
  making regular clients and servers.
+ Stream sockets - Connection-oriented sockets, which uses Transmission Control Protocol(TCP). 
  Used for making regular clients and servers.
+ Raw sockets - Allow direct sending and receiving of ip packets without any protocol specific 
  transport layer formatting. Used for **sniffing** and **injection**. Nmap uses raw sockets.

## Goals 
+ Create a simple echo server to handle 1 client.
  - Once you have created the server [socket](https://docs.python.org/3/howto/sockets.html#creating-a-socket) , you need some way to handle server clientsocket.There is actually 3 general ways to handle
    clients \- dispatching a thread to handle clientsocket, create a new process to handle clientsocket,
    or use non-blocking sockets, and multiplex between our “server” socket and any active clientsockets
    using select. we are going to implement all these three.
+ Implement threading to handle client sockets.
+ Create a Multi-Process echo server.
+ Create a Non-blocking Multiplexed Echo Server using Select().

## References
[A nice how to on socket programming.](https://docs.python.org/3/howto/sockets.html)  
[sockets](https://en.wikipedia.org/wiki/Network_socket)  
[ipc](https://en.wikipedia.org/wiki/Inter-process_communication)  
