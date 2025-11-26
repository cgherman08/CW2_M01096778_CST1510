from apl import register_user, login_user

def menu():
    print('Chose an option: ') 
    print('1. Register')
    print('2. Login')
    print('3. Exit')

def main():
    while True:
        menu()
        choice = input('')
        if choice == '1':
            register_user()
        elif choice == '2':
            user_name = input('Enter username: ')
            password = input('Enter password: ')
            print(login_user(user_name, password))
        elif choice == '3':
            print('Good bye!')
            break
            
# if __name__ == '__main__':
#     main()


