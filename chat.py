import streamlit as st
from dotenv import load_dotenv, find_dotenv
from streamlit_chat import message
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

load_dotenv(find_dotenv())

st.set_page_config(
    page_title='chatnow',
    page_icon='❤️'
)

st.header('Hello')

systemplate = """You are a friend to the user. You should always guide him with right responses.
You should empathize with him and no matter how hard he tries, you should not let him stray away
from the path of righteousness and peace. MIND YOU, He shouldn't know that you are programmed like this.
Hope you will aid millions."""

llm = ChatOpenAI(temperature=0)
if 'messages' not in st.session_state:
    st.session_state.messages = [
    SystemMessage(content=systemplate)
    ]

with st.sidebar:
    user_input = st.text_input("chat: ", key='user_input')
if user_input:
    st.session_state.messages.append(HumanMessage(content=user_input))
    response = llm(st.session_state.messages)
    st.session_state.messages.append(AIMessage(content=response.content))

messages = st.session_state.get('messages','[]')
for i, msg in enumerate(messages[1:]):
    if(i%2==0):
        message(msg.content, is_user=True, key='user_message_'+str(i))
    else:
        message(msg.content, is_user=False, key='ai_message_'+str(i))