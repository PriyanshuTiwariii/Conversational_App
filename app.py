import streamlit as st
from langchain.llms import HuggingFaceEndpoint

def load_answer(question):
    llm=HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-7B-Instruct-v0.2"
    )
    answer=llm.invoke(question)
    return answer

st.set_page_config(page_title="LangChain Demo",page_icon=":robot:")
st.header("LangChain")

def get_text():
    input_text=st.text_input("You: ",key="input")
    return input_text

user_input=get_text()
response=load_answer(user_input)
submit=st.button('Generate')

if submit:
    st.subheader("Answer: ")
    st.write(response)
    