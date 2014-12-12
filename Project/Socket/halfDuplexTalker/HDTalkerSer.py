#coding=utf-8				
import socket               	#加载socket模块
from time import ctime			#加载time模块ctime类

HOST = ''						#设置主机IP，为空则表示本机上所有的网卡ip。
PORT = 3300						#设置端口号
BUSIZ = 1024					#设置数据缓冲区，1KB
ADDR = (HOST, PORT)				

def closeTCnt():				#
	TCntSock.close()
	print "Session closing.."
	
TSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	#创建一个TCP sokcet
TSerSock.bind(ADDR)				#绑定TCP socket的地址和端口
TSerSock.listen(1)				#只接收一个请求，如后续后其他请求则会被拒绝
try:
	while True:
		print 'Waitting for connection...'
		(TCntSock, cntAddr) = TSerSock.accept()		#TSerSock.accept 返回一个(conn, addr)的元组。 conn是一个socket对象，而addr是客户端IP地址和端口
		print '...connection from:', cntAddr
		
		try: 

			while True:
				rData = TCntSock.recv(BUSIZ)		#接收客户端信息
				if not rData:
					continue
				elif rData == 'quit':				#当收到‘quit’后关闭TCntSock并等待下一次链接
					break
				else:
					print 'From [%s] %s \n  %s' % (cntAddr[0], ctime(), rData)	
					
			
				while True:
					sData = raw_input('I:>  ')		
					if not sData:
						continue
					else:	
						TCntSock.send('From [%s] %s \n  %s' %
							(cntAddr[0], ctime(), sData))		#发送服务器信息。
						break
		
		except 	socket.error ,detail:			#发生错误是关闭TCntSock,输出错误信息并等待下一次链接
			print detail
		closeTCnt()

finally:
	TSerSock.close()



