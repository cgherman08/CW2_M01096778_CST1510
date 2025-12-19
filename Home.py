import streamlit as st

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

st.title("Operational Intelligence Hub")
st.subheader("One place for incidents, tickets, datasets, and AI assistance")

# Quick actions
col_login, col_register = st.columns([1, 1])
with col_login:
    if st.button("Log In", type="primary"):
        st.switch_page("pages/1_🔐 _Login.py")
with col_register:
    if st.button("Register"):
        st.switch_page("pages/1_🔐 _Login.py")

st.write(
    "Use the sidebar to access each module. Data and actions live on their dedicated pages after you sign in."
)

st.markdown(
    """
    **Pages**
    - Login: access your account and session.
    - Cybersecurity: review incidents, timelines, and status.
    - Data Science: browse datasets and metadata.
    - IT Operations: manage IT tickets and assignments.
    - AI Assistant: ask questions, draft summaries, and get quick help.
    """
)

st.info("Please log in to work with live data on other pages.")


    

    
    