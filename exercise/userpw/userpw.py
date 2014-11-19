#创建用户名：密码字典
db={}

#创建新用户
def newuser():
    prompt = 'login desired:'
    while True:
        name = raw_input(prompt)
        if db.has_key(name):       #判断该用户是否存在（判断该key是否存在）
            prompt = 'name taken, try another\n again:'
            continue
        else:
            break
    pwd = raw_input('password:')
	#在db中创建用户名-密码对（key-value）
    db[name] = pwd              

#用户登录
def olduser():
    name = raw_input("login:")
    pwd = raw_input("password:")
	
	#判断该用户是否存在（判断该key是否存在）
	
    if db.has_key(name) == 0:
        print "Account is not exist"
    else:
		#提取用户密码（将变量name的值作为key，并获取该key的值）
        passwd = db[name]
		#比较密码
        if pwd == passwd:
            print "Welcome back", name
        else:
            print "login incorrect"

#菜单
def showmenu():
        prompt = """
            (N)ew User Login:
            (E)xisting User Login:
            (Q)uit:
            Enter choice:
        """
        done = False

        while not done:
                try:
                    choice = raw_input(prompt).strip()[0].lower()        #取输入的字符串第一个字符
                except (EOFError, KeyboardInterrupt):
                    choice = 'q'										 #抛出异常，即ctrl+D或者Ctrl+C等同于输入q
                print "\nYou picked: [%s]" % choice
                if choice not in 'neq':									 #判断选择是否在‘neq’中
                    print "invalid option ,try again"
                else:
                    chosen = True

                if choice == 'q' :done =True
                if choice == 'n' :newuser()
                if choice == 'e' :olduser()

if __name__ == '__main__':												#如果__name__='__main__'则表示脚本被直接运行。而不是通过import调用。
    showmenu()			