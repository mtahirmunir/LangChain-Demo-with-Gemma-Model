import os
import streamlit as st
from langchain.chat_models import ChatOpenAI  # Use ChatOpenAI for chat-based models
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

# Set up OpenAI API key using Streamlit secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
# Groq api key
groq_api_key = st.secrets["GROQ_API_KEY"]

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the question asked."),
        ("user", "Question: {question}")
    ]
)

# Streamlit UI
st.title("LangChain Demo with OpenAI ChatGPT")
input_text = st.text_input("What question do you have in mind?")

# OpenAI GPT Model (Chat)
# llm = ChatOpenAI(model="gpt-4", openai_api_key=os.getenv("OPENAI_API_KEY"))
llm = ChatGroq(model="Gemma2-9b-It",groq_api_key=groq_api_key)
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Generate response
if input_text:
    try:
        response = chain.invoke({"question": input_text})
        st.write(response)
        st.text_input("")
    except Exception as e:
        st.error(f"An error occurred: {e}")
