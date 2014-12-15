#coding=utf-8
#创建线程方法之二：创建线程实例，传入一个可调用的类对象（ThreadFunc）。
import time
import threading

class ThreadFunc(object):						#创建一个ThreadFunc类
	def __init__(self, func, args, name=''):	#通过构造器将传入的函数等设置为类属性。
		self.name = name
		self.func = func
		self.args = args

	def __call__(self):							#调用函数。
		self.func(*self.args)

loops = [4, 2]
def loop(nloop, nsec):
	print 'start loop', nloop, 'at:', time.ctime()
	time.sleep(nsec)
	print 'loop ', nloop, 'done at:', time.ctime()

def main():
	print 'starting at:', time.ctime()
	threads = []
	nloops = range(len(loops))

	for i in nloops:
		t = threading.Thread(
			target = ThreadFunc(loop, (i,loops[i]), 	#实例化Thread对象。将loop函数和函数的参数传入ThreadsFunc类。得到一个ThreadFunc实例对象，并传入Thread。
			loop.__name__) )	
		threads.append(t)						#将实例后的Thread对象追加到threads列表中

	for i in nloops:							#启动启动线程
		threads[i].start()

	for i in nloops:							#结束线程
		threads[i].join()						#join将线程挂起，直到进程结束。或这是timeout，当超时后，线程挂起。

	print 'all DONE at:', time.ctime()

if __name__ == '__main__':
	main()