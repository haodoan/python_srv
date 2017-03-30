#!/usr/bin/python3           # This is client.py file

import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 1234

# connection to hostname on the port.
s.connect((host, port))                               

# Receive no more than 1024 bytes
msg = 'Hao Doan'
msg = s.send(msg.encode('utf-8'))                                     

s.close()
