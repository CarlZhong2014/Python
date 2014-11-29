#!/usr/bin/env python
# -*- coding: utf-8 -*-  
from socket import *
from time import ctime

HOST = ''
PORT = 8080		#设置端口号
BUFSIZ = 1024		#设置缓冲大小为1k
ADDR = (HOST, PORT)	#通信地址

udpSocket = socket(AF_INET, SOCK_DGRAM)
udpSocket.bind(ADDR)
try:

	while True:
		print 'waiting for message...'
		data, addr = udpSocket.recvfrom(BUFSIZ)
		print data
		udpSocket.sendto('[%s] %s' % (
			ctime(), data), addr)
		print '...recevied from and returned to:', addr
except (EOFError, KeyboardInterrupt):
	udpSocket.close()
