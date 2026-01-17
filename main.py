"""
LangChain Azure OpenAI Integration Demo

This module demonstrates how to use LangChain with Azure OpenAI to create
a conversational AI assistant specialized in movie-related queries.

Environment Variables Required:
    - AZURE_OPENAI_API_VERSION: The API version for Azure OpenAI
    - AZURE_AI_AGENT_MODEL_DEPLOYMENT_NAME: The deployment name of the Azure OpenAI model
"""

import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve Azure OpenAI configuration from environment variables
openai_api_version = os.getenv('AZURE_OPENAI_API_VERSION')
openai_model = os.getenv('AZURE_AI_AGENT_MODEL_DEPLOYMENT_NAME')


from langchain_openai import AzureChatOpenAI

# Initialize Azure OpenAI language model with configuration
# Temperature of 0.6 provides a balance between creativity and consistency
llm = AzureChatOpenAI(
	azure_deployment=openai_model,
    api_version=openai_api_version,
	temperature=0.6,
)

# Define conversation messages
# System message sets the assistant's behavior and expertise domain
# Human message contains the user's query
messages = [
    (
        "system",
        "You are a helpful assistant that helps with Movies related queries.",
    ),
    ("human", "What are the top rated movies on IMDB?"),
]

# Invoke the language model with the messages and get the AI response
ai_msg = llm.invoke(messages)

# Display the AI-generated response
print(ai_msg)