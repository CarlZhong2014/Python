#config=utf-8
import socket
import time
import threading
import sys
HOST = 'localhost'
PORT = 3380
BUSIZ = 1024
ADDR = (HOST, PORT)

def Trec(Rsocket, CLocal):
	while True:
		RData = Rsocket.recv(BUSIZ)
		if not RData :
			continue
		elif RData in ('quit', 'QUIT'):
			Rsocke.close 
		else:
			Rstr = '\nFrom ' + CLocal[0] + ' say: ' + RData
			sys.stdout.write(Rstr)
		print 'aa'
		

def Tsend(ConLocal):
	
	
def main():
	TSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	TSerSock.bind(ADDR)
	TSerSock.listen(1)

	threads = []
	while True:
		print 'waiting for connnection'
		ConSock, ConLocal = TSerSock.accept()
		print '... Connect from', ConLocal
		CT = threading.Thread(
			target = Trec, 
			args = (ConSock, ConLocal))
		
		threads.append(CT)

		CT = threading.Thread(
			target = Tsend,
			args = (ConLocal))
		for i in range(len(threads)):
			threads[i].start()

if __name__ == '__main__':
	main()
else:
	print 'Nothing to do!!!'


