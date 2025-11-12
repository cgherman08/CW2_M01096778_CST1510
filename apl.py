import bcrypt

def hash_password(pwd):
    password_bytes = pwd.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password.decode('utf-8')

def validate_password(pwd, hashed):
    password_bytes = pwd.encode('utf-8')
    hashed_bytes = hashed.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_bytes)
    

def register_user():
    exist = False
    user_name = input('Enter username: ')
    password = input('Enter password: ')
    hashed_password = hash_password(password)
    with open('users.txt', 'r') as f:
        for i in f:
            if i.strip().split(',')[0] == user_name:
                exist = True
            else:
                continue
    if exist == False:
         with open('users.txt', 'a') as f:
            f.write(f'{user_name},{hashed_password}\n')
            print('User Registerd Successfuly')
    else:
        print('Username in use, please choose another username')    
        

def login_user(username, pwd):
    with open('users.txt', 'r') as f:
        for line in f.readlines():
            user, stored_hash = line.strip().split(',', 1)
            if user == username:
                if validate_password(pwd, stored_hash):
                    return 'Welcome'
                else:
                    return 'Invalid password'
    return 'User not found' 