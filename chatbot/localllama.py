from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

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
st.title("A chatbot using local Llama 2 ")
input_text = st.text_input("Ask me any question...")


# Create a OpenAI LLM
llm = Ollama(model="llama2")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser


# Respond to a user input
if input_text:
    st.write(chain.invoke({'question': input_text}))