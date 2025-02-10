"""
Descriptions:
    Entry point of OpenAI-based chatbot
    through LangChain and OpenAI API.
    All process monitored using LangSmith.   
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

# Read API keys from .env
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


# Define a prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You're a helpful assistant. Please respond to query from the user."),
        ("user", "Question: {question}")
    ]
)


# Create user guide via streamlit
st.title("A chatbot using OpenAI API")
input_text = st.text_input("Ask me any question...")


# Create a OpenAI LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

# Respond to a user input
if input_text:
    st.write(chain.invoke({'question': input_text}))
