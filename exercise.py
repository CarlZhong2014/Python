#coding=utf-8
#exercise
import threading
import time

loops = [4,2]
timeout = [2, 1]
def loop(nloop, nsec):
	print 'start loop', nloop, 'at:', time.ctime()
	time.sleep(nsec)
	print 'loop', nloop, 'done at:', time.ctime()

def main():
	print 'starting at:', time.ctime()
	threads = []
	nloops = range(len(loops))

	for i in nloops:
		t = threading.Thread(target=loop,
			args=(i,loops[i]))
		threads.append(t)

	for i in nloops:
		threads[i].start()

	for i in nloops:
		threads[i].join(timeout[i])	
	print 'All threads has done at:', time.ctime()

if __name__ == '__main__':
	main()



