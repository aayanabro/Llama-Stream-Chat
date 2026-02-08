import streamlit as st
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
## Streamlit UI
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey,Lets Chat")

Chat= ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct",
                 temperature=0.2)

if "flowmeassges" not in st.session_state:
  st.session_state['flowmessages']=[
      SystemMessage(content="You are a helpful assistant")
  ]
## Function to load OpenAI model amd get response

def get_groq_response(query):

    st.session_state['flowmessages'].append(HumanMessage(content=query))
    answer=Chat.invoke(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content



inout=st.text_input("input:",key="input")
response=get_groq_response(inout)

submit=st.button("Ask the question")
 ##If ask button is called

if submit:
    st.subheader('The response is ')
    st.write(response)