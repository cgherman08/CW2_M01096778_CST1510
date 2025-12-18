import streamlit as st
from app.cyber_incidents import get_all_cyber_incidents
from app.db import get_connection
import pandas as pd


conn = get_connection()
data = get_all_cyber_incidents(conn)

st.title('Cyber Incidents Dashboard')



if not st.session_state['logged_in']:
    st.warning('Please log in to access the dashboard.')
    st.stop()
else:
    st.success(f'Welcome, {st.session_state["username"]}!')
    
with st.sidebar:
    st.header('Navigation')
    severity_ = st.selectbox('Severity', data['severity'].unique())
    
data['timestamp'] = pd.to_datetime(data['timestamp'], errors='coerce')

filtered_data = data[(data['severity'] == severity_)] 

col1, col2 = st.columns(2)

with col1:
    st.write('Data 1st column')
    st.bar_chart(filtered_data['status'].value_counts())
    
with col2:
    st.write('Data 2nd column')
    st.line_chart(filtered_data, x='timestamp', y='incident_id')
    

st.write(filtered_data)
 
 