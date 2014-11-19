#coding=utf-8
#上述是将文件编码事先申明为utf-8。
#包含md5加密
#导入time模块
import time

#初始化用户列表
User = {}

def u_lock(password):
      import md5                                       #加载MD5模块
      Md5 = md5.new()                                   #创建一个md5对象
      Md5.update(password)                              #将password字符串的值转为md5
      return Md5.digest()                              #返回一个md5的字符串

#创建用户
def newer():
    user_prompt = "Enter a name you want to use:"       #设置用户名提示
    user_pw = "Enter a pw you want to use:"             #设置密码提示
    username = raw_input(user_prompt)                   #输入用户名

    if username in User.keys():                        #检查用户名是否存在
        print "This username was exist.."
    else:
        userpw = raw_input(user_pw)                     #获取用密码
        userpw = u_lock(userpw)                         #调用加密函数
        User[username] = [userpw,str(time.ctime())]     #将username，userpw,logintime记录入User字典中，其中userpw,logintime是存在列表中

#登陆函数
def login():
    user_prompt = "Name:"                               #设置登陆用户名提示
    user_pw = "Password:"                               #设置密码提示
    username = raw_input(user_prompt)                   #输入用户名

    if username not in User.keys():                    #确认用户名
        print "his user is not exist"
    else:
        userpw = raw_input(user_pw)
        userpw = u_lock(userpw)                        #调用解密函数
        if userpw not in User[username][0]:           #比对密码
            print "incorrect"
        else:
            print "hello  %s \n You last log time is %s" % (username, User[username][1])        #输出用户信息以及上次登录时间
            User[username][1] = str(time.ctime())      #更新用户登陆时间

#删除一个用户
def Del_user():
    prompt = "Who will be deleted in this system:"
    Duser = raw_input(prompt)
    if Duser not in User.keys():
        print "%s isn't exist!!"
    else:
        print User[Duser]
        del User[Duser]

#显示所用用户信息
def Show_user():
    if len(User) == 0:
        print "No User in this system"
    else:
        print "Showing all user"
        for key in User.keys():
            print "Username = %s \t Password = %s \t Last login time = %s  " % (key, User[key][0], User[key][1])
        print "Out of all!!"


#主菜单
def menu():
    " Show the main menu "                             #设置__doc__
    display = """
                Main menu
        (R)egister:
        (L)og in:
        (D)elete User:
        (S)how Every user:
        (Q)uit:
        Enter your choice:
        """                                           #设置菜单
    done = False                                      #标识是否结束程序

    while not done:
        chosen = False                                #标识是否选择

        while not chosen:
            try :                                    #设置异常处理，如果使用crtl+c 或报异常则直接相当于选择退出程序
                choice = raw_input(display).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = "q"

            print "\n You picked: [%s]" % choice     #输出用户的选择

            if choice not in "rlqds":                  #确认用户选择是否正确
               print "invalid option, try again"
            else:
               chosen = True

            if choice == 'r': newer()                #均为调用函数
            if choice == 'l': login()
            if choice == 'd': Del_user()
            if choice == 's': Show_user()
            if choice == 'q': done = True

if __name__ == '__main__':                           #如果确认本程序是否为主程序
    menu()