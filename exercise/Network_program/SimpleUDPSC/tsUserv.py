#!/usr/bin/env python

from socket import *
from time import ctime

HOST = ''
PORT = 8080
BUFSIZ = 1024
ADDR = (HOST, PORT)

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
