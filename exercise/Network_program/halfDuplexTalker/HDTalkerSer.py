#coding=utf-8
from socket import *
from time import ctime

HOST = ''
PORT = 3300
BUSIZ = 1024
ADDR = (HOST, PORT)

TSerSock = socket(AF_INET, SOCK_STREAM)
TSerSock.bind(ADDR)
TSerSock.listen(1)

while True:
	print u'Waitting for connection...'
	TCntSock, cntAddr = TSerSock.accept()
	print u'...connection from:', cntAddr
	rData = TCntSock.recv(BUSIZ)
	if not rData:
		TCnSock.close()
		break

	print u'From [%s] %s \n%s' % (cntAddr[0], ctime(), rData)
	
	sData = raw_input(u'>')
	TCntSock.send(u'From [%s] %s \n%s' %
		(cntAddr[0], ctime(), sData))
	TCntSock.close()

TSerSock.close()

