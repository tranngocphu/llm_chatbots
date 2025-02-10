from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv
load_dotenv()

# Read API keys from .env
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Define server and routes
app=FastAPI(
    title="ChatBot App",
    version="1.0",
    description="ChatBot API Using Langserve"
)

llm1 = ChatOpenAI(model="gpt-3.5-turbo")
llm2 = Ollama(model="llama2")
llm3 = Ollama(model="deepseek-r1:1.5b")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You're a helpful assistant. Please respond to query from the user."),
        ("user", "Question: {question}")
    ]
)

add_routes(
    app,
    prompt|llm1,
    path="/openai"
)

add_routes(
    app,
    prompt|llm2,
    path="/llama2"
)

add_routes(
    app,
    prompt|llm3,
    path="/deepseek"
)

if __name__ == "__main__":
    ip = os.getenv("HOST_IP")
    port = int(os.getenv("HOST_PORT"))
    uvicorn.run(app, host=ip, port=port)

