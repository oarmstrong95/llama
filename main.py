# /**********************************************************************************************************
# Import modules
# /**********************************************************************************************************
# Import general modules in 
import json
import os
from dotenv import load_dotenv

# Import modules required for API call
from langchain_ollama import ChatOllama
from langchain.prompts.chat import ChatPromptTemplate

# Load in yaml file for environment level variables
load_dotenv('env.yaml')

# Create an instance of the model
llm = ChatOllama(model="llama3", temperature=0)

# Create a prompt
prompt = ChatPromptTemplate(
    [
        (
            "system",
            "You are a helpful assistant that translates {input_language} to {output_language}.",
        ),
        ("human", "{input}"),
    ]
)

# Define the chain
chain = prompt | llm

# Invoke the chain
chain.invoke(
    {
        "input_language": "English",
        "output_language": "German",
        "input": "I love programming.",
    }
)