#!/usr/bin/python3           # This is server.py file
import socket                                         
import signal
import sys

def signal_handler(signal, frame):
	clientsocket.close()
	#print ('Closed socket %s' % str(clientsocket))
	print (mgs);
	sys.exit(0)

def WriteFile(str):
    # Open a file
    fo = open("store.txt", "w+", encoding='utf8')
    fo.write(str)
    # Close opend file
    fo.close()
# create a socket object
serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM) 
# Reuse socket addr
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# get local machine name
host = socket.gethostname()                           
print(host)
port = 1234                                          

# bind to the port
serversocket.bind(('127.0.0.1', port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           


signal.signal(signal.SIGINT, signal_handler)
print ('Press Ctrl+C')
#signal.pause()   
print ('Waitting a connection') 
while True:
    # establish a connection
    global clientsocket
    clientsocket,addr = serversocket.accept()      

    print("Got a connection from %s" % str(addr))
    #msg='Thank you for connecting'+ "\r\n"
    #print(msg)
    mgs = 'test message'
    DataRecv = clientsocket.recv(1024);
    print(DataRecv.decode('utf-8'))
    WriteFile(DataRecv.decode('utf-8'))
    
    #clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()
    
    
