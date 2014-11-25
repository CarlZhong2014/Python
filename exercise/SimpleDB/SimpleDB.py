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

def SearchName(name=""):
	prompt = """
 Who are you wants to searching? \n
 Name : """
 	if name =="":
		name = raw_input(prompt)

	if name in contactDB:
		print "Name: %s \n Phone: %s \n Birthday: %s \n Addr: %s." % \
		(name, contactDB[name]['Phone'], contactDB[name]['Birthday'], contactDB[name]['Addr'])
	else:
		print "%s is not existing!!!" % name

def SearchPhone():
	prompt = """
What phone number are you want to searching!!\n
Phone number: """
	phone = raw_input(prompt)
	for element in contactDB.items():		#items方法以list形式返回contactDB的key-value。即list[0]为key，list[1]为value。
		if element[1]["Phone"] == phone:    #通过以上方法，以phone为关键字，输出phone主的信息
			print "Name: %s \n Phone: %s \n Birthday: %s \n Addr: %s." % \
			(element[0], element[1]['Phone'],element[1]['Birthday'],element[1]['Addr'])
			return None
	print "%s is not existing!!!" % phone
	
def addMember():
	prompt = """
This is addition menu
Who are you want to add? """
	name = raw_input(prompt)
	if name not in contactDB:						#判断信息是否存在，不存在则添加。存在则提示存在。
		phone = raw_input("Whose number is : ")
		birth = raw_input("Whose birthday is : ")
		addr = raw_input("Where are who live : ")
		contactDB[name] = {							#将数据加入contactDB中。
			"Phone":phone, 
			"Birthday":birth,
			"Addr":addr
			}
	else:
		print name,"is existing in contact."	

def delMember():
	prompt = """
This is delete module
Who will out of this contact? 
name: """
	name = raw_input(prompt)
	if name in contactDB:
		SearchName(name)
		choice = raw_input("Do you want to delete who?[Y/N]").strip()[0].lower()
		if choice == "y":
			del contactDB[name]
			print "%s is deleted in this contact." % name
	else:
		print name,"is not existing in contact."
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
	print "This module couldn't use by other module."