#coding=utf-8
#创建线程方法之三：从Thread类派生一个子类，并实例化子类。
import time
import threading

class ThreadFunc(threading.Thread):			#创建一个Thread派生的子类hreadFunc
	def __init__(self, func, args, name=''):	
		threading.Thread.__init__(self)		#调用了父类的构造器
		self.name = name
		self.func = func
		self.args = args

	def run(self):							#调用函数。
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
		t = ThreadFunc(loop,				#实例化ThreadFunc对象。传入loops函数及其参数。
			(i,loops[i]), 	
			loop.__name__) 	
		threads.append(t)						#将实例后的Thread对象追加到threads列表中

	for i in nloops:							#启动启动线程
		threads[i].start()

	for i in nloops:							#结束线程
		threads[i].join()						#join将线程挂起，直到进程结束。或这是timeout，当超时后，线程挂起。

	print 'all DONE at:', time.ctime()

if __name__ == '__main__':
	main()