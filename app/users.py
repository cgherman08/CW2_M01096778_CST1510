from schema import hash_password, validate_password

def register_user():
    exist = False
    user_name = input('Enter username: ')
    password = input('Enter password: ')
    hashed_password = hash_password(password)
    with open('DATA/users.txt', 'r') as f:
        for i in f:
            if i.strip().split(',')[0] == user_name:
                exist = True
            else:
                continue
    if exist == False:
         with open('DATA/users.txt', 'a') as f:
            f.write(f'{user_name},{hashed_password}\n')
            print('User Registerd Successfuly')
    else:
        print('Username in use, please choose another username')    
        

def login_user(username, pwd):
    with open('DATA/users.txt', 'r') as f:
        for line in f.readlines():
            user, stored_hash = line.strip().split(',', 1)
            if user == username:
                if validate_password(pwd, stored_hash):
                    return 'Welcome'
                else:
                    return 'Invalid password'
    return 'User not found' 