'''
    Example：
    Using list object to analog all operation of stack.
'''
stack = []


def push_stack():
    stack.append(raw_input(' Push new data in stack: '))


def pop_stack():
    if len(stack) == 0:
        print("The stack is empty that couldn't pop element.")
    else:
        print("The [ %s ] had been popped out at stack." % stack.pop())


def view_stack():
    if len(stack) == 0:
        print("The stack is empty. It's nothing to show.")
    else:
        print stack

# FCs is a dictionary object, which be used to choice stack operation funciton.
FCs = {'u': push_stack, 'o': pop_stack, 'v': view_stack}


def show_menu():
    prompt = """
    P(u)sh
    P(o)p
    (V)iew
    (Q)uit
    """
    option = 'uovq'
    while True:
        choice = raw_input(prompt).split()[0].lower()
        print("\nYou picked:[%s]" % choice)
        if choice not in option:
            print("Invalid option, try again!!")
            continue
        elif choice == 'q':
            break
        else:
            FCs[choice]()


if __name__ == '__main__':
    show_menu()
