# -*- coding: utf-8 -*- 
from socket import *
HOST = 'localhost'
PORT = 3300				#设置端口号
BUFSIZ = 1024				#设置缓冲区大小，设定为1K
ADDR = (HOST, PORT)	

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)	#与服务端链接

while True:
	data = raw_input('>')	#输入要发送的数据
	if not data:			#判断数据是否为空
		break
	tcpCliSock.send(data)	#发送数据
	print u'Waitting...\n'
	data = tcpCliSock.recv(BUFSIZ)	#接收服务器返回的数据
	if not data:
		break
	print data 				#输出服务器返回的数据

tcpCliSock.close()