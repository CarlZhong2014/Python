#coding=utf-8
import threading
from time import ctime,sleep

class ThreadFunc(threading.Thread):
	def __init__(self, func, args, name=''):
		threading.Thread.__init__(self)
		self.func = func
		self.args = args
		self.name = name

	def getResult(self):
		return self.res

	def run(self):
		print 'start function', self.name, 'at:', ctime()
		self.res = self.func(*self.args)
		print 'Function ', self.name, 'done at:', ctime()

def flib(x):						#斐波那契数列实现
	sleep(0.01)
	if x < 2 : return 1
	return (flib(x-2) + flib(x-1))

def fac(x):							#阶乘函数
	sleep(0.1)
	if x < 1 : return 0
	elif x == 1: return 1
	return (x * fac(x-1))

def sum(x):							#累加函数
	sleep(0.1)
	if x < 1 : return 0
	elif x == 1: return 1
	return (x + sum(x-1))

funcs = [flib, fac, sum]			
n = 12								#输入

def main():
	nfuncs = range(len(funcs))
	threads = []

	print '*** SINGLE THREAD'		#单线程实现
	for i in nfuncs:
		print 'start function', funcs[i].__name__, 'at:', ctime()
		print funcs[i](n)
		print 'Function ', funcs[i].__name__, 'done at:', ctime()

	print '*** MULTIPLE THREADS'	#多线程实现
	for i in nfuncs:
		t = ThreadFunc(funcs[i], (n,), funcs[i].__name__) #实例化ThreadFunc类
		threads.append(t)

	for i in nfuncs:
		threads[i].start()

	for i in nfuncs:
		threads[i].join()
		print threads[i].getResult()
	
	print 'all Done'
	

if __name__=='__main__':
	__doc__ = """
	对比单线程和多线程处理斐波那契数列，阶乘，累加求和所花费事件。
	"""
	main()