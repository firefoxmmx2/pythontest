#!/usr/bin/env python2
#coding:utf8

#Filename:pysockettestServ.py
#Description:an server example for socket

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpServSock = socket(AF_INET, SOCK_STREAM) 
tcpServSock.bind(ADDR)
tcpServSock.listen(5)

while True:
    print 'waiting for connection ...'
    tcpCliSock, addr = tcpServSock.accept()
    print '...connected from: ', addr

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send('[%s] %s' % (ctime(), data))
        tcpCliSock.close()
tcpServSock.close()
