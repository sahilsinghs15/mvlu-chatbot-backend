
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import PromptTemplate, LLMChain

import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file if available

API_KEY = os.getenv("API_KEY")


if not API_KEY:
    raise ValueError("API Key is not set")

# Initialize the LLM (Google Gemini model) with temperature setting and API key
llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.5, google_api_key=API_KEY)

# Create a prompt template
prompt_template = PromptTemplate(
    input_variables=["query"],
    template="You are a helpful assistant. Answer the following question: {query}"
)

# Create a simple sequential chain using LLMChain
chain = LLMChain(llm=llm, prompt=prompt_template)

def get_llm_response(query: str) -> str:
    input_data = {"query": query}
    response = chain.run(input_data)
    return response
