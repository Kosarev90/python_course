import os

FILE_PATH = r'C:\Users\admin\OneDrive\Рабочий стол\python course\HW\address.txt'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_user():
    with open(FILE_PATH, 'a') as f:
        f.write('\n')
        f.write(input('Input data: '))

def read_all_users():
    with open(FILE_PATH, 'r') as f:
        for line in f:
            print(line)

def search_user():
    with open(FILE_PATH, 'r') as f:
        search = input('Input search post: ')
        found = False
        for line in f:
            if search.lower() in line.lower():
                print(line.strip())
                found = True
        if not found:
            print('Not found')

def remove_user():
    with open(FILE_PATH, 'r') as f:
        lines = f.readlines()
    with open(FILE_PATH, 'w') as f:
        remove = input('Input name to delete user: ')
        removed = False
        for line in lines:
            if remove.lower() not in line.lower():
                f.write(line)
            else:
                removed = True
        if removed:
            print('user delete')
        else:
            print('user not found')

def modify_user():
    with open(FILE_PATH, 'r') as f:
        lines = f.readlines()
    with open(FILE_PATH, 'w') as f:
        modify = input('Input data whose change:')
        new_data = input('new data user: ')
        modified = False
        for line in lines:
            if modify.lower() in line.lower():
                f.write(new_data + '\n')
                modified = True
            else:
                f.write(line)
        if modified:
            print('Data successfully')
        else:
            print('User not found')

def info_func():
    print('1 - Show phonebook')
    print('2 - Add user')
    print('3 - search user')
    print('4 - delete user')
    print('5 - change user')
    print('6 - exit')

def phonebook():
    clear_screen()
    info_func()

    while True:
        user_action = input("Input number - ")
        clear_screen()
        if user_action == '1':
            read_all_users()
        elif user_action == '2':
            add_user()
        elif user_action == '3':
            search_user()
        elif user_action == '4':
            remove_user()
        elif user_action == '5':
            modify_user()
        elif user_action == '6':
            break
        else:
            print('Error')

        input('Intput Enter, to be continue...')
        clear_screen()
        info_func()

phonebook()
