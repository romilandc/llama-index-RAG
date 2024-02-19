import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load model configurations from .env file
env_path = 'C:/Users/~/env.txt' #update path to where you saved .env file

load_dotenv(env_path)
model=os.getenv("MODEL")
base_url=os.getenv("BASE_OLLAMA_URL")

#Test connection
llm = ChatOllama(
    model=model,
    base_url=base_url
)

prompt = ChatPromptTemplate.from_template("Tell me a short joke about rain")

chain = prompt | llm | StrOutputParser()

print(chain.invoke( { "topic": "AI" } ))
