from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser

### Configs ###
# Load model configurations from .env file
# Nice to keep configs in one place to ensure model stays same across files. 
# Changing model takes a long time for first load
import os
from dotenv import load_dotenv

env_path = 'C:/Users/groutgauss/Llama Index/env.txt'

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
