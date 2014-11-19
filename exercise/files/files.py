#coding=utf-8
"""
1、列出指定目录”c:\”所有的后缀名为*.txt 的文件(包括子文件夹内所有文件)，并输出每个文件的创建日期和大小
2、针对上述文件，取内容倒数 2 行，存入新文件，取名“list.txt”
3、将上述文件按照创建时间进行正向排序（从早到晚），存入新文件，取名“排序.txt”
"""
import os.path 
fileList = []                        					#用于存储获取到的txt文件的文件路径和创建时间，是一个二维列表            

def getLines(fileSite):              					#将符合要求的文件的最后两行写入list.txt中。其中fileSite是dirList传来的参数
	tarFile = open("list.txt","a")   					#创建/打开list.txt文件
	rawFile = open(fileSite,"r")                        #打开要读取的txt文件
	fileLines = rawFile.readlines()						#读取整个txt文件
	rawFile.close										#关闭该txt文件
	lC = len(fileLines)									#获取txt文件行数
	if lC >= 2 :										#判断txt文件的行数
		tarFile.writelines("%s\n" % fileLines[lC-2]) 
		tarFile.writelines("%s\n" % fileLines[lC-1]) 
	elif lC ==1 :										#如果txt文件为1行则直接写入list.txt。如果为空则直接忽略
		tarFile.writelines("%s\n" % fileLines) 
	tarFile.close										#关闭list.txt文件
	return None


def dirList(rootDir):
	for root,dirs,files in os.walk(rootDir):			#root为文件所在目录，dirs为子目录，files为文件名
		for fileName in files:							#遍历文件名
			if '.c' in fileName:						#判断文件是否为.c文件
				filePath = os.path.join(root,fileName)	#获取文件完整路径
				fileCtime =os.path.getmtime(filePath)   #获取文件的创建时间
				fileAtt = (filePath,fileCtime)          #将文件的完成路径和创建时间放在元组fileAtt里
				fileList.append(fileAtt)      			#将该元组存入fileList中
				getLines(filePath)						#调用getLines
			else:
				continue
def sortFile():
	fileCount = len(fileList)							#获取fileList的元素个数，及文件个数

#简单按照时间排序
	for head in range(0,fileCount):						
		for tail in range(1,fileCount):
			dif = cmp(str(fileList[head][1]),str(fileList[tail][1]))
			if  dif == 1:
				tmp = head
				head = tail
				tail = head
				break
			else:
				continue

#将排序后的文件名输入到排序.txt文件中
	tarFile = open(u"排序.txt","a")	
	for echo in fileList:				
		tarFile.writelines("%s\n" % echo[0])
	tarFile.close
	return None

#主，如果是非调用则执行下列函数，如果为调用则输出字符串“Nothing to do!!!”		
if __name__=="__main__":
	dirList('E:\\Program\\C')
	sortFile()
else:
	print "Nothing to do!!!"
