# config=utf-8
import socket
import threading
import sys
HOST = ''
PORT = 3388
BUSIZ = 1024
ADDR = (HOST, PORT)


def Trec(Rsocket, CLocal):
    while True:
        RData = Rsocket.recv(BUSIZ)
        if not RData:
            continue
        elif RData in ('quit', 'QUIT'):
            Rsocket.close()
        else:
            Rstr = '\nFrom ' + CLocal[0] + ' say: ' + RData
            sys.stdout.write(Rstr)


def Tsend(Dsocket):
    while True:
        SData = raw_input('\n>')
        Dsocket.send(SData)


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
            target=Trec,
            args=(ConSock, ConLocal))

        threads.append(CT)

        CT = threading.Thread(
            target=Tsend,
            args=(ConSock,))
        threads.append(CT)
        for i in range(len(threads)):
            threads[i].start()
        threads[0].join()
    TSerSock.close()
if __name__ == '__main__':
    main()
else:
    print 'Nothing to do!!!'
