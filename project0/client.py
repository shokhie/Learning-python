#!/usr/bin/python
import socket
import sys

# Connect to an internet address
(host, port) = sys.argv[1], sys.argv[2]

# Create connection to a host
client = socket.create_connection((host, port))

# Send some data
while True:
    data = input("client:")
    client.send(data.encode())
    msg = client.recv(2048)
    print("server:", msg.decode())

# Close the connection
client.close()





