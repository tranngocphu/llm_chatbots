import requests
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

HOST_IP = os.getenv("HOST_IP")
HOST_PORT = os.getenv("HOST_PORT")
API_SERVER = f"http://{HOST_IP}:{HOST_PORT}"

def query_openai(input_text):
    response = requests.post(
        f"{API_SERVER}/openai/invoke",
        json={'input': {'question': input_text}}
    )        
    return response.json()['output']['content']
     
     
def query_llama2(input_text):
    response = requests.post(
        f"{API_SERVER}/llama2/invoke",
        json={'input': {'question': input_text}}
    )        
    return response.json()['output']


def query_deepseek(input_text):
    response = requests.post(
        f"{API_SERVER}/deepseek/invoke",
        json={'input': {'question': input_text}}
    )        
    return response.json()['output']

st.set_page_config(layout="wide")
st.title("Compare OpenAI, Llama2, DeepSeek-r1")

input_text = st.text_input("Ask a question...")

col1, col2, col3 = st.columns(3)

if input_text:
    with col1:
        st.write("OpenAI:\n" + query_openai(input_text))
    
    with col2:
        st.write("Llama2:\n" + query_llama2(input_text))
    
    with col3:
        st.write("DeepSeek:\n" + query_deepseek(input_text))
