#coding=utf-8
#�����ǽ��ļ�������������Ϊutf-8��
#����md5����
#����timeģ��
import time

#��ʼ���û��б�
User = {}

def u_lock(password):
      import md5                                       #����MD5ģ��
      Md5 = md5.new()                                   #����һ��md5����
      Md5.update(password)                              #��password�ַ�����ֵתΪmd5
      return Md5.digest()                              #����һ��md5���ַ���

#�����û�
def newer():
    user_prompt = "Enter a name you want to use:"       #�����û�����ʾ
    user_pw = "Enter a pw you want to use:"             #����������ʾ
    username = raw_input(user_prompt)                   #�����û���

    if username in User.keys():                        #����û����Ƿ����
        print "This username was exist.."
    else:
        userpw = raw_input(user_pw)                     #��ȡ������
        userpw = u_lock(userpw)                         #���ü��ܺ���
        User[username] = [userpw,str(time.ctime())]     #��username��userpw,logintime��¼��User�ֵ��У�����userpw,logintime�Ǵ����б���

#��½����
def login():
    user_prompt = "Name:"                               #���õ�½�û�����ʾ
    user_pw = "Password:"                               #����������ʾ
    username = raw_input(user_prompt)                   #�����û���

    if username not in User.keys():                    #ȷ���û���
        print "his user is not exist"
    else:
        userpw = raw_input(user_pw)
        userpw = u_lock(userpw)                        #���ý��ܺ���
        if userpw not in User[username][0]:           #�ȶ�����
            print "incorrect"
        else:
            print "hello  %s \n You last log time is %s" % (username, User[username][1])        #����û���Ϣ�Լ��ϴε�¼ʱ��
            User[username][1] = str(time.ctime())      #�����û���½ʱ��

#ɾ��һ���û�
def Del_user():
    prompt = "Who will be deleted in this system:"
    Duser = raw_input(prompt)
    if Duser not in User.keys():
        print "%s isn't exist!!"
    else:
        print User[Duser]
        del User[Duser]

#��ʾ�����û���Ϣ
def Show_user():
    if len(User) == 0:
        print "No User in this system"
    else:
        print "Showing all user"
        for key in User.keys():
            print "Username = %s \t Password = %s \t Last login time = %s  " % (key, User[key][0], User[key][1])
        print "Out of all!!"


#���˵�
def menu():
    " Show the main menu "                             #����__doc__
    display = """
                Main menu
        (R)egister:
        (L)og in:
        (D)elete User:
        (S)how Every user:
        (Q)uit:
        Enter your choice:
        """                                           #���ò˵�
    done = False                                      #��ʶ�Ƿ��������

    while not done:
        chosen = False                                #��ʶ�Ƿ�ѡ��

        while not chosen:
            try :                                    #�����쳣�������ʹ��crtl+c ���쳣��ֱ���൱��ѡ���˳�����
                choice = raw_input(display).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = "q"

            print "\n You picked: [%s]" % choice     #����û���ѡ��

            if choice not in "rlqds":                  #ȷ���û�ѡ���Ƿ���ȷ
               print "invalid option, try again"
            else:
               chosen = True

            if choice == 'r': newer()                #��Ϊ���ú���
            if choice == 'l': login()
            if choice == 'd': Del_user()
            if choice == 's': Show_user()
            if choice == 'q': done = True

if __name__ == '__main__':                           #���ȷ�ϱ������Ƿ�Ϊ������
    menu()