#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 12345

# connection to hostname on the port.
s.connect(("127.0.0.1", port))                               

# Receive no more than 1024 bytes
msg = 'Hảo Đoàn Đại Học Giao Thông'
msg = s.send(msg)                                     

s.close()
