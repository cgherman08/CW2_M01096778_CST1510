import streamlit as st
from services.database_manager import DatabaseManager

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if 'username' not in st.session_state:
    st.session_state['username'] = ''

st.title('Data Science Dashboard')

if not st.session_state['logged_in']:
    st.switch_page('pages/1_🔐 _Login.py')

datasets = DatabaseManager().load_datasets()

if datasets.empty:
    st.info('No datasets found. Load metadata to get started.')
else:
    st.markdown('**Available datasets**')
    st.dataframe(datasets, width='stretch')
