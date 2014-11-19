#coding=utf-8
dashes = '\n' + '-' * 50    #分界线，全是破折号
exec_dict = {				#字典：用于exec在执行中生成代码，f为for循环，s为迭代序列的while循环，n为计数while循环。
	
	'f': """
for %s in %s:
	print %s"""
	,

	's':"""
%s = 0
%s = %s
while %s < len(%s):
	print %s[%s]
	%s = %s + 1 
"""
	,

	'n':"""
%s = %d
whiel %s < %d:
	print %s
	%s = %s + %d
"""
}

def main():
	ltype = raw_input( 'Loop type? (For/While)')			#输入循环类型
	dtype = raw_input('Data type?(Number/seq)')				#输入传的类型

	if dtype in 'Nn':										#如果是数字，则设置数字范围，并使用range产生一个数字列表，最后将列表赋予迭代序列seq
		start = input('Starting value?')
		stop = input('Ending value (non-inclusive)?')
		step = input('Stepping value? ')
		seq = str(range(start, stop, step))
	
	else:
		seq = raw_input('Enter sequence:')					#否则，要求用户输入一个序列
	
	var = raw_input('Iterative variable name?')				#输入迭代器变量的名字

	if ltype in 'fF':										#判断是否使用for循环，如果是将相应的参数传入
		exec_str = exec_dict['f'] % (var, seq, var)

	elif ltype in 'Ww':										#判断是否使用while循环
		if dtype in 'sS':									#判断数据类型是否为seq
			svar = raw_input("Enter sequence name?")
			exec_str = exec_dict['s'] % \
			(var, svar, seq, var, svar, svar, var, var, var)
		elif dtype in 'Nn':									#判断数据类型是否为number
			exec_str = exec_dict['n'] % \
			(var, svar, var, stop, var, var, var, step)

	print dashes											
	print "Your custom-generated cod:" + dashes				
	print exec_str + dashes									#输出生成的代码
	print 'Text execution of the code:' + dashes
	exec exec_str											#输出执行结果
	print dashes

if __name__ == '__main__':
	main()

