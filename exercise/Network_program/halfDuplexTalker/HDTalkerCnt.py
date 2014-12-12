#coding=utf-8
import socket
HOST = 'localhost'			#设置要链接的主机的IP
PORT = 3300					#设置要链接的主机端口号
BUFSIZ = 1024				#设置缓冲区大小，设定为1K
ADDR = (HOST, PORT)	
tryCon = 0

def TCnt():
	tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	while True:
		try:
			tcpCliSock.connect(ADDR)	#与服务端链接
		except:
			print u"正在尝试连接远程主机 "
			tryCon+=1		
			if tryCon == 3:
				print u"无法连接上远程主机，请稍后再试"
				exit()
		else:
			break
	print u'登陆成功（通讯结束请输入"quit"退出）\n'

	try:
		while True:
			data = raw_input('I:>  ')
			if not data:			
				continue
			elif data == 'quit':		#通知服务端工作完成
				tcpCliSock.send(data)	
				break
			else:
				tcpCliSock.send(data)	

			while True:
				data = tcpCliSock.recv(BUFSIZ)	

				if not data:
					continue
				else:
					print data 	
					break			
	except socket.error, e:
		print "Session closing"
		print e
	tcpCliSock.close()

if __name__=="__main__":
	TCnt()