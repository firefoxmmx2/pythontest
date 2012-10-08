#!/usr/bin/env python2
#coding:utf8
#Filename:pysockettest.py
#Description: an example for pysocket.

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

class Mysocket(socket):
    def __exit__(self):
        super(Mysocket, self).__exit__()
        self.close()
    def __enter__(self):
        return super(Mysocket, self).__init__()

#tcpCliSock = socket(AF_INET, SOCK_STREAM)
with Mysocket(AF_INET, SOCK_STREAM) as tcpCliSock:
    tcpCliSock.connect(ADDR)
    while True:
        data = raw_input('> ')
        if not data:
            break
        tcpCliSock.send(data)
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        print data
