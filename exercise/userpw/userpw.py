#�����û����������ֵ�
db={}

#�������û�
def newuser():
    prompt = 'login desired:'
    while True:
        name = raw_input(prompt)
        if db.has_key(name):       #�жϸ��û��Ƿ���ڣ��жϸ�key�Ƿ���ڣ�
            prompt = 'name taken, try another\n again:'
            continue
        else:
            break
    pwd = raw_input('password:')
	#��db�д����û���-����ԣ�key-value��
    db[name] = pwd              

#�û���¼
def olduser():
    name = raw_input("login:")
    pwd = raw_input("password:")
	
	#�жϸ��û��Ƿ���ڣ��жϸ�key�Ƿ���ڣ�
	
    if db.has_key(name) == 0:
        print "Account is not exist"
    else:
		#��ȡ�û����루������name��ֵ��Ϊkey������ȡ��key��ֵ��
        passwd = db[name]
		#�Ƚ�����
        if pwd == passwd:
            print "Welcome back", name
        else:
            print "login incorrect"

#�˵�
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
                    choice = raw_input(prompt).strip()[0].lower()        #ȡ������ַ�����һ���ַ�
                except (EOFError, KeyboardInterrupt):
                    choice = 'q'										 #�׳��쳣����ctrl+D����Ctrl+C��ͬ������q
                print "\nYou picked: [%s]" % choice
                if choice not in 'neq':									 #�ж�ѡ���Ƿ��ڡ�neq����
                    print "invalid option ,try again"
                else:
                    chosen = True

                if choice == 'q' :done =True
                if choice == 'n' :newuser()
                if choice == 'e' :olduser()

if __name__ == '__main__':												#���__name__='__main__'���ʾ�ű���ֱ�����С�������ͨ��import���á�
    showmenu()			