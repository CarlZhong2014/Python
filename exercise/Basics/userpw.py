"""
    This program is an example：
    Using dictionary object like db to saving username and username's password.
"""
import string
user_passwd = {}


def identify_username(user_nm):
	"""
		this function is order to check the username which is can accept or not.
	"""
    user_nm = str(user_nm)
    if user_nm in user_passwd:
        print("The user name is exist.")
        return 0
    alph = string.letters
    alph_num = alph + string.digits
    user_nm_len = len(user_nm)
    ele = 0
    while ele < user_nm_len:
        if user_nm[0] not in alph:
            print("error: The frist charater must be letter.")
            return 0
        elif user_nm[ele] not in alph_num:
            print("error: The username must consists of letters and digits.")
            return 0
        ele = ele + 1
    else:
        return 1


def add_newuser():
	"""
		This function will be used to create new user. 
		It will call identify_username() to check the username which is legal or not.
	"""
    a_username = raw_input("What name you want to create?  ")
    a_id = identify_username(a_username)
    if a_id == 0:
        return
    while a_id == 1:
        a_password = raw_input("%s's password :" % a_username)
        if a_password == raw_input("Confirm password"):
            print("Successfully!!!")
            user_passwd[a_username] = a_password
            break
        else:
            print("Retype\n")


def login_user():
    if len(user_passwd) == 0:
        print("Nobody in this system, please create one.")
    else:
        l_username = raw_input("username: ")
        l_password = raw_input("password: ")
        l_spw = user_passwd.get(l_username)
        if l_spw == l_password:
            print("welcome back"), l_username
        else:
            print("login incorrect")

FS = {'n':add_newuser, 'l':login_user}
def show_menu():
    prompt = """
    (N)ew User:
    (L)ogin:
    (Q)uit.
    Enter choice: """
    while True:
        choice = raw_input(prompt).strip()[0].lower()
        print "\n Your picked:", choice
        if choice not in "nlq":
            print("invalid option, try again")
            continue
        elif choice != 'q':
            FS[choice]()
        else:
            break


if __name__ == "__main__":
    show_menu()


