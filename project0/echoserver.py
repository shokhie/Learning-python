#!/usr/bin/env python
'''
A echo server
'''
import socket

HOST = ''
PORT = 1337
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcpsocket:
    tcpsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpsocket.bind((HOST, PORT))
    tcpsocket.listen()
    conn, addr = tcpsocket.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
           # print('Received data', len(data), 'bytes')
           # print(type(data))
            if not data: 
                break
            sent = conn.sendall(data)
