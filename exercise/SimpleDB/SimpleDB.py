#coding=utf-8

contactDB={								#contact数据库字典
	'Carl' : {
		'Phone' : '2442',	
		'Birthday' : '93:11:11',
		'Addr' : 'Software street 8'
	},

	'Tom' : {
		'Phone' : '3300',
		'Birthday' : '93:11:01',
		'Addr' : 'wuyi street 200'
	}
}

funDict = {								#将函数存放在字典中方便调用
	'n' : 'SearchName()', 
	'p' : 'SearchPhone()', 
	'm' : 'addMember()', 
	'd' : 'delMember()'
}

def SearchName():
	prompt = """
 Who are you wants to searching? \n
 Name : """
	name = raw_input(prompt)
	if name in contactDB:
		print "Name: %s \n Phone: %s \n Birthday: %s \n Addr: %s." % \
		(name, contactDB[name]['Phone'], contactDB[name]['Birthday'], contactDB[name]['Addr'])
	else:
		print "%s is not existing!!!"

def SearchPhone():
	prompt = """
What phone number are you want to searching!!\n
Phone number: """
	phone = raw_input(prompt)
	for element in contactDB.items():
		if element[1]["Phone"] == phone:
			print "Name: %s \n Phone: %s \n Birthday: %s \n Addr: %s." % \
			(element[0], element[1]['Phone'],element[1]['Birthday'],element[1]['Addr'])
			return None
	print "%s is not existing!!!" % phone
	
def addMember():
	print "add"
def delMember():
	print "del"

def menu():
	prompt="""								
This is my contact:	
	Search by (N)ame;
	Search by (P)hone;
	Add a new (M)ember;
	(D)el a member;
	(Q)uit
Please enter Your choice:"""										#菜单内容
	done = False							#退出标志
	while not done:
		try:
			choice = raw_input(prompt).strip()[0].lower()		#获取输入的第一个字符，并将该字符转为小写。
		except (EOFError, KeyboardInterrupt):					#当有错误时，choice=q，退出程序。避免中断。
			choice = 'q'
		print "\n Your choice is %s" % choice					#显示用户的选择
		if choice in "npmd":
			exec funDict[choice]								#根据用户选择执行相应的函数
		elif choice == 'q':
			done = True
		else:
			print "\n Please enter right option!!!"

if __name__ == "__main__":
	menu()
else:
	print "nothing"