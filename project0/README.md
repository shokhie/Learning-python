# Project 0
Playing with [sockets](https://en.wikipedia.org/wiki/Network_socket).

## What is a socket?
If two processes want to communicate with each other, they do it using
sockets. There are many ways in which inter-process 
communication ([ipc](https://en.wikipedia.org/wiki/Inter-process_communication#Approaches)) 
can be achieved but for cross-platform communications, sockets are the best. 

In layman's terms, think of this as an endpoint for sending and receiving data across the network.

### Socket types
+ Datagram sockets - Connectionless sockets, which use User Datagram Protocol(UDP).   
  Used for making regular clients and servers.
+ Stream sockets - Connection-oriented sockets, which use Transmission Control Protocol(TCP). 
  Used for making regular clients and servers.
+ Raw sockets - Allow direct sending and receiving of IP packets without any protocol-specific transport layer formatting. Used for **sniffing** and **injection**. Nmap uses raw sockets.  
  After this whenever we talk about sockets, it will be stream sockets i.e. TCP sockets.

## Goals 
+ Create a simple echo server to handle 1 client.
  - Once you have created the server [socket](https://docs.python.org/3/howto/sockets.html#creating-a-socket) , you need some way to handle the server client socket. There are 3 general ways to handle
    clients \- dispatching a thread to handle client sockets, creating a new process to handle client sockets,
    or using non-blocking sockets, and multiplexing between our “server” socket and any active client sockets
    using select. we are going to implement all these three.
+ Implement threading to handle client sockets.
+ Create a Multi-Process echo server.
+ Create a Non-blocking Multiplexed Echo Server using Select().
+ Implement a proper way in which data can be exchanged between client and server.

## References
[A nice how to on socket programming.](https://docs.python.org/3/howto/sockets.html)  
[sockets](https://en.wikipedia.org/wiki/Network_socket)  
[ipc](https://en.wikipedia.org/wiki/Inter-process_communication)  
[Beej's Guide to Network Programming](https://beej.us/guide/bgnet/html/split/)
