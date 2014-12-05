#coding=utf-8
import ftplib
import os
import socket

HOST = '192.168.1.42' 	#设置ftp主机
USER = 'why'			#ftp账号

try:					#测试链接目标主机
	fObj = ftplib.FTP(HOST)
except (socket.error, socket.gaierror), e:
	print 'ERROR: cannot reach %s\nbyebye' % HOST
	exit()
print '*** connected to host "%s"' % HOST

try:					#登陆ftp服务器
	fObj.login(USER,'yhw')
except ftplib.error_perm:
	print 'ERROR: cannot login %s' % USER
	fObj.quit()
	exit()				#退出程序
print '*** Logged in as %s' % USER
fObj.dir()				#显示当前目录下的内容
fObj.cwd('anonymous')	#切换到anonymous目录
print fObj.pwd()
fObj.dir()
fObj.quit()				#登出
