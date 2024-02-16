#!/usr/bin/env python
'''
Simple echo server which handles 1 client. 
'''
import socket
import sys

# Create a tcp socket
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Fix error, address already in use
tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind socket to an address
host, port = sys.argv[1], int(sys.argv[2])
address = (host, port)
tcpSocket.bind(address)

# Enable the server to accept connections
tcpSocket.listen()

print("Waiting for connection...", host, port)

# Accept a connection
(client, (clientIp, clientPort)) = tcpSocket.accept()

print("Connected to client:", clientIp, "on port", clientPort)

# Receive data from the socket
data = "foo"
while len(data):
    data = client.recv(2048)
    print(data.decode(), end='')

print("Closing connection...")
client.close()

print("Shutting down the server...")
tcpSocket.close()



