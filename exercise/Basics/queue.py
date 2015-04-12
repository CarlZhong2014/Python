'''
    Example：
    Using list object to analog all operation of queue.
'''
queue = []


def enQ():
    queue.append(raw_input('Enter new data enqueue :'))


def deQ():
    if len(queue) == 0:
        print('The queue is empty!!!')
    else:
        print('The [ %s ] had been dequeued at queue' % queue.pop(0))


def viewQ():
    if len(queue) == 0:
        print('The queue is empty!!')
    else:
        print(queue)

# FCs is a dictionary object, which be used to choice queue operation funciton.
FCs = {'e': enQ, 'd': deQ, 'v': viewQ}


def show_menu():
    prompt = '''
    (E)nqueue
    (D)nqueue
    (V)iew queue
    (Q)uit
    please enter your choice : '''
    while True:
        choice = raw_input(prompt).strip()[0].lower()
        if choice not in 'edvq':
            print('Invalid option, try agin')
        elif choice == 'q':
            break
        else:
            FCs[choice]()

if __name__ == "__main__":
    show_menu()
