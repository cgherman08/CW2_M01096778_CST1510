from .db import conn, DATA_PATH
import bcrypt


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_password(stored_password: str, provided_password: str) -> bool:
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))

def user_registration(conn):
    # exist = False
    name = input('Enter username: ')
    password = input('Enter password: ')
    hash = hash_password(password)
    set_user(conn, name, hash)
    print('User Registerd Successfuly')
    
    # with open('DATA\users.txt', 'r') as f:
    #     for i in f:
    #         if i.strip().split(',')[0] == name: 
    #             exist = True
    #         else:
    #             continue
    # if exist == False:
    #     #  with open('DATA/users.txt', 'a') as f:
    #     #     f.write(f'{user_name},{hashed_password}\n')
    #     #     print('User Registerd Successfuly')
        
    # else:
    #     print('Username in use, please choose another username')    
        

# def user_login(conn):
#     name = input('Enter your name to log in: ')
#     password = input('Enter your password: ')
#     id,name_db,hash_db = get_one_user(conn, name)
#     if name == name_db:
#         return verify_password(hash_db, password)
    
def user_login(conn):
    name = input('Enter your name to log in: ')
    password = input('Enter your password: ')
    user = get_one_user(conn, name)
    if user:
        id, name_db, hash_db = user
        if name == name_db:
            print('Welcome')
            return verify_password(hash_db, password)
    return False

def set_user(conn, name, hash):
    curr = conn.cursor()
    sql = """INSERT INTO users (user_name, password_hash) VALUES (?,?)"""
    param = (name, hash)
    curr.execute(sql, param)
    conn.commit()

def get_all_users():
    curr = conn.cursor()
    sql = """SELECT * FROM user"""
    curr.execute(sql)
    all_users = curr.fetchall()
    for i in all_users:
        print(i)
    user = curr.execute()
    conn.close()
    return user

def get_one_user(conn, name):
    curr = conn.cursor()
    sql = """SELECT * FROM users WHERE user_name = ?"""
    param = (name,)
    curr.execute(sql, param)
    user = curr.fetchone()
    return(user)

def delete_user(conn, name):
    curr = conn.cursor()
    sql = """DELETE FROM users  WHERE user_name = ?"""
    param = (name,)
    curr.execute(sql, param)
    conn.commit()
    print(f'{name} was successfully deleted!')
        

def update_user(conn, old_name, new_name):
    curr = conn.cursor()
    sql = """UPDATE users SET user_name = ? WHERE user_name = ?"""
    param = (new_name, old_name)
    curr.execute(sql, param)
    conn.commit()
    

def migrate_users():
    with open('DATA\\users.txt', 'r') as f:
        users = f.readlines()
        for user in users:
            name, hash = user.strip().split(',')
            set_user(conn, name, hash)
        conn.close()
    
    
