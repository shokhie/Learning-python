#!/usr/bin/python
import socket

# Create a tcp socket
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Fix error address already in use
tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind socket to an address
address = ("192.168.1.7", 1337)
tcpSocket.bind(address)

# Enable the server to accept connections
tcpSocket.listen()

print("Waiting for connection...")

# Accept a connection
(client, (clientIp, clientPort)) = tcpSocket.accept()

print("Connected to client:", clientIp, "on port", clientPort)

# Receive data from the socket
data = "foo"
while len(data):
    data = client.recv(2048)
    print(data.decode("utf-8"), end="")

print("Closing connection...")
client.close()

print("Shutting down the server...")
tcpSocket.close()



