import streamlit as st

from groq import Groq

client = Groq(api_key='')

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if 'username' not in st.session_state:
    st.session_state['username'] = ''

if not st.session_state['logged_in']:
    st.switch_page('pages/1_🔐 _Login.py')
else:
    st.success(f'Welcome, {st.session_state["username"]}!')

st.title('AI Assistant')

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input('Enter your question here... ')

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=st.session_state.messages
    )
    
    reply = completion.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply) 
   