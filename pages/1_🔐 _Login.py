import streamlit as st
from services.auth_manager import AuthManager, SimpleHasher
from services.database_manager import DatabaseManager   

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    
if not st.session_state['logged_in']:
    tab_login, tab_register = st.tabs(['Log In', 'Register'])

    with tab_login:
        st.header('Log In')
        login_username = st.text_input('Username', key='login_username')
        login_password = st.text_input('Password', type='password', key='login_password')
        if st.button('Log In'):
            if AuthManager().login_user(login_username, login_password):
                st.success('Login successful!')
                st.session_state['logged_in'] = True
                st.success('You are now logged in!')
                st.session_state['username'] = login_username
                st.switch_page('Home.py') 
            else:
                st.error('Invalid username or password. Please try again.')
            
    with tab_register:
        st.header('Register')
        register_username = st.text_input('Choose a Username', key='register_username')
        register_password = st.text_input('Choose a Password', type='password', key='register_password')
        hash = SimpleHasher().hash_password(register_password)   
        if st.button('Register'):
            if DatabaseManager().get_one_user(register_username):
                st.error('Username already exists. Please choose another username.')    
            else:
                DatabaseManager().set_user(register_username, hash)
                st.success('Registration successful! You can now log in.')
else:
    st.success(f'You are already logged in as {st.session_state["username"]}.')
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button('Log Out', type='primary', width='stretch'):
            st.session_state['logged_in'] = False
            st.info('You have been logged out.')
            st.switch_page('pages/1_🔐 _Login.py')
    
    st.divider()
    
    st.subheader('Account Management')
    
    with st.expander('Change Username'):
        new_username = st.text_input('Enter your new username', key='new_username')
        if st.button('Update Username', width='stretch'):
            if not new_username:
                st.warning('Please enter a new username.')
            elif DatabaseManager().get_one_user(new_username):
                st.error('Username already exists. Please choose another username.')
            else:
                DatabaseManager().update_user(st.session_state['username'], new_username)
                st.session_state['username'] = new_username
                st.success('Your username has been updated.')
    
    st.divider()
    
    with st.expander('⚠️ Delete Account', expanded=False):
        st.warning('This action cannot be undone. Your account and all data will be permanently deleted.')
        confirm_delete = st.checkbox('I understand and want to delete my account')
        if st.button('Delete my account', type='primary', disabled=not confirm_delete, width='stretch'):
            DatabaseManager().delete_user(st.session_state['username'])
            st.session_state['logged_in'] = False
            st.info('Your account has been deleted.')
            st.switch_page('pages/1_🔐 _Login.py')