# coding=utf-8
import threading
import sys
import socket

HOST = 'localhost'
PORT = 3388
BUFSIZ = 1024
ADDR = (HOST, PORT)
CntSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def CntTest():
	tryCon = 0
	while True:
		try:
			CntSock.connect(ADDR)
		except socket.error:
			print u"正在尝试连接远程主机 "
			tryCon = tryCon + 1
			if tryCon == 3:
				print u"无法连接上远程主机，请稍后再试"
				exit()
			else:
				break
	print u'登陆成功（通讯结束请输入"quit"退出）\n'


def CntRec(DSock, DLocal):
    while True:
        RData = DSock.recv(BUFSIZ)
        Rstr = '\n' + DLocal + ' say: ' + RData + '\n'
        sys.stdout.write(Rstr)


def CntSend(DSock):
    while True:
        SData = raw_input('\n >')
        DSock.send(SData)


def main():
    threads = []
    CntTest()
    print type(CntSock)
    while True:
        CT = threading.Thread(
            target=CntRec,
            args=(CntSock, HOST))
        threads.append(CT)
        CT = threading.Thread(
            target=CntSend,
            args=(CntSock,))
        threads.append(CT)
        for i in range(len(threads)):
            threads[i].start()
        threads[0].join()

if __name__ == "__main__":
    main()
else:
    print "Nothing to do"
