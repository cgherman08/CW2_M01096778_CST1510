from app.users import user_registration, user_login
from app.db import conn, DATA_PATH

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
            user_registration(conn)
        elif choice == '2':
            print(user_login(conn))
        elif choice == '3':
            print('Good bye!')
            break
            
if __name__ == '__main__':
    main()


