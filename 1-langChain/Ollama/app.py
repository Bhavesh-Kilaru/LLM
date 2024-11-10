import os
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM
import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
#Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

## designing prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', "You are a helpful assistant. Please respond to the question asked."),
        ("user", "Question:{question}")
    ]
)

## streamlit framework
st.title("Lang Chain demo with google gemma model")
input_text = st.text_input("what question you have in mind?")

## calling gemma 2 model
llm=OllamaLLM(model="gemma2:2b")
outputParser = StrOutputParser()
chain=prompt| llm| outputParser

if input_text:
    st.write(
        chain.invoke(
            {"question":input_text}
            )
    )