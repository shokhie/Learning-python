# Project 0
Playing with [sockets](https://en.wikipedia.org/wiki/Network_socket).

## What is a socket ?
If two processes want to communicate with each other, then they do it using
sockets. There are many ways in which inter-process 
communincation ([ipc](https://en.wikipedia.org/wiki/Inter-process_communication#Approaches)) 
can be acheived but for cross platform communications, sockets are the best. 

If you want to understand it, think it as an endpoint for sending and receiving data across the network.

### Socket types
+ Datagram sockets - Connectionless sockets, which uses User Datagram Protocol(UDP). Used for making regular clients and servers.
+ Stream sockets - Connection-oriented sockets, which uses Transmission Control Protocol(TCP).Used for making regular clients and servers.
+ Raw sockets - Allow direct sending and receiving of ip packets without any protocol specific transport layer formatting.
  Used for **sniffing** and **injection**. Nmap uses raw sockets.

## Goals --
+ Create a simple echo server to handle 1 client.
  Once you have created the server, there are many ways to process clients.
  
+ Create a 



