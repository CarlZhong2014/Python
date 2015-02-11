#coding=utf-8
#exercise
import threading
import time

loops = [4,2]
class Tloop(threading.Thread):
	def __init__(self, func, args, name=''):
		threading.Thread.__init__(self)
		self.name = name 
		self.func = func
		self.args = args

	def __call__(self):
		self.func(*self.args)

def loop(nloop, nsec):
	print 'start loop', nloop, 'at:', time.ctime()
	time.sleep(nsec)
	print 'loop', nloop, 'done at:', time.ctime()

def main():
	print 'starting at:', time.ctime()
	threads = []
	nloops = range(len(loops))

	for i in nloops:
		t = threading.Thread(
			target = Tloop(loop, (i,loops[i]),loop.__name__))
		threads.append(t)

	for i in nloops:
		threads[i].start()

	for i in nloops:
		threads[i].join()	
	print 'All threads has done at:', time.ctime()

if __name__ == '__main__':
	main()



