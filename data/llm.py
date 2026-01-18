from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

def get_llm():
    load_dotenv()
    llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.3-70b-versatile")
    return llm

if __name__ == "__main__":
    llm = get_llm()
    response = llm.invoke("Hello, how are you?")
    print(response.content)





