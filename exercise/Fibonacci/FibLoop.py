#coding:utf-8
#列表和循环实现斐波那契数列
def main():
	lis=[]
	ennum = int(raw_input("输入一个数"))  
	
	for i in range(0,ennum):			  
		if i<=1:
			lis.append(1)
		else:
			nextlis = lis[i-1] + lis[i-2]    #实现数列
			lis.append(nextlis)

	for i in lis:						
		print i

if __name__=="__main__":
	main()