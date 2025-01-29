
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

def groq_llm():
    os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
    if "GROQ_API_KEY" not in os.environ:
        raise ValueError("GROQ_API_KEY is not set in the environment. Please set it before running the script.")
    
    llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    )
    return llm

