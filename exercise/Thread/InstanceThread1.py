#coding=utf-8
#创建线程方法之一：创建线程实例，传入函数
import time
import threading

loops = [4, 2]
def loop(nloop, nsec):
	print 'start loop', nloop, 'at:', time.ctime()
	time.sleep(nsec)
	print 'loop', nloop, 'done at:', time.ctime()

def main():
	print 'starting at:', time.ctime()
	threads = []
	nloops = range(len(loops))

	for i in nloops:
		t = threading.Thread(target = loop, 	#实例化Thread对象，将loop函数和函数的参数传入。得到一个Thread实例。
			args = (i, loops[i]) ) 
		threads.append(t)						#将实例后的Thread对象追加到threads列表中

	for i in nloops:							#启动启动线程
		threads[i].start()

	for i in nloops:							#结束线程
		threads[i].join()						#join将线程挂起，直到进程结束。或这是timeout，当超时后，线程挂起。

	print 'all DONE at:', time.ctime()

if __name__ == '__main__':
	main()