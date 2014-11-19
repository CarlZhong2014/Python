#coding:utf-8
#递归实现斐波那契数列
def fib(n):
	if n<=2:
		return 1
	else:
		return fib(n-1) + fib(n-2) #递归生成

def main():
	lis=[]
	ennum = int(raw_input("输入一个数"))  #用户输入
	
	for i in range(1,ennum+1):			  
		lis.append(fib(i))

	for i in lis:						#打印数列
		print i

if __name__=="__main__":
	main()