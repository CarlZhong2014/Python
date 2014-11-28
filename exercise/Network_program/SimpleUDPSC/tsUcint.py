#!/usr/bin/env python
from socket import *

HOST = '192.168.1.130'
PORT = 8080
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSocket = socket(AF_INET, SOCK_DGRAM)
try:
	while True:
		data = raw_input('>')
		if not data:
			break
		udpCliSocket.sendto(data, ADDR)
		data, ADDR = udpCliSocket.recvfrom(BUFSIZ)
		if not data:
			print 'received nothing...'
			break
		print data
except (EOFError, KeyboardInterrupt):
	udpCliSocket.close()
