import streamlit as st
from app.users import set_user, user_login, hash_password
from app.db import get_connection   

conn = get_connection() 

st.title('Welcome to the Home page')

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False  
     
if 'username' not in st.session_state:
    st.session_state['username'] = ''
    
tab_login, tab_register = st.tabs(['Log In', 'Register'])

with tab_login:
    st.header('Log In')
    login_username = st.text_input('Username', key='login_username')
    login_password = st.text_input('Password', type='password', key='login_password')
    if st.button('Log In'):
        if user_login(conn, login_username, login_password):
            st.success('Login successful!')
            st.session_state['logged_in'] = True
            st.success('You are now logged in!')
            st.session_state['username'] = login_username
            st.switch_page('pages/Dashboard.py') 
        else:
            st.error('Invalid username or password. Please try again.')
        
with tab_register:
    st.header('Register')
    register_username = st.text_input('Choose a Username', key='register_username')
    register_password = st.text_input('Choose a Password', type='password', key='register_password')
    hash = hash_password(register_password)
    if st.button('Register'):
        set_user(conn, register_username, hash)
        st.success('Registration successful! You can now log in.')
    
if st.button('Log Out'):
    st.session_state['logged_in'] = False
    st.info('You have been logged out.')
    
    