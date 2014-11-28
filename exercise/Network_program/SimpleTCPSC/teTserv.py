# -*- coding: utf-8 -*- 
from socket import *
from time import ctime

def cliSockClose():					#客户端断开处理
	tcpCliSock.close()				#关闭与客户端的Socket （必）
	print 'IP:%s PORT:%d is quit' % (addr[0],addr[1])

HOST = ''					#设置主机ip，如果为空则表示所有网卡上的所有ip
PORT = 4322					#设置端口号（数字）
BUFSIZ = 1024				#设置缓冲区大小，设定为1K
ADDR = (HOST, PORT)			

tcpSerSock = socket(AF_INET, SOCK_STREAM)	 #创建一个TCP socket。
tcpSerSock.bind(ADDR)						 #将TCP socket绑定到网卡上
tcpSerSock.listen(5)						 #Socket最多允许5个链接

while True:
	print "waiting for connection"
	tcpCliSock, addr = tcpSerSock.accept()	#accept（单线程）阻塞式。收到请求时，返回一个单独的socket给tcpCliSock。并将客户端地址给addr
	print '...connection from:', addr

	while True:
		try:
			data = tcpCliSock.recv(BUFSIZ)	#接收客户端发来的数据
		except error:
			cliSockClose()					#客户端断开处理
			break

		if not data:
			break
		if data == 'exit':
			cliSockClose()					#客户端断开处理
			break
		else:
			tcpCliSock.send('[%s] %s' % 
			(ctime(), data ))			#给客户端发来的数据加上个时间戳后返回
		


tcpSerSock.close()						#关闭TCP Socket （必）