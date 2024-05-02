from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"
)

llm=Ollama(model="llama2")

prompt=ChatPromptTemplate.from_template("Give me caption for {topic} with 20 words")

add_routes(
    app,
    prompt|llm,
    path="/caption"
)


if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)