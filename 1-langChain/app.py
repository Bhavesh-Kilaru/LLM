from fastapi import FastAPI 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

model = ChatGroq(model = "Gemma2-9b-It")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Translate the following into {language}"),
        ("user", "{input}")
    ]
)

parser = StrOutputParser()
chain = prompt| model | parser

##app definition
app=FastAPI(title="LangChain Server",
            version = "1.0",
            description="A simple API using langchain runnable interfaces")

add_routes(
    app
    , chain
    , path="/chain"
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)