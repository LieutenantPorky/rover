#!/usr/bin/env python3

import socketserver
import sys
print("TCP server program start")

#read stdin for server address and port
address, port = None, None
if (len(sys.argv) > 2):
    address = sys.argv[1]
    port = int(sys.argv[2])
else :
    address = 'localhost'
    port = 9999

#define TCP handler class - should extend socketserver.BaseRequestHandler

class tcpHandle(socketserver.StreamRequestHandler):
    def handle(self):
        #self.rfile is an IO buffer from which we can read
        #recieved data

        self.data = self.rfile.readline().strip()

        #print debug info on connection
        print("recieved data from {}:".format(self.client_address[0]))
        print(self.data)

#create TCP socket
print("binding server to address {} with port {}".format(address, port))
with socketserver.TCPServer((address, port), tcpHandle) as server:
    print("server init finished")
    print("|------------------|")
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
