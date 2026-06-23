import os
from dotenv import load_dotenv
from langchain_nvidia_ai_endpoints import ChatNVIDIA

load_dotenv()

print("KEY LOADED:", os.getenv("NVIDIA_API_KEY")[:10] + "...")

llm = ChatNVIDIA(
    model=os.getenv("NVIDIA_MODEL", "meta/llama-3.3-70b-instruct"),
    api_key=os.getenv("NVIDIA_API_KEY"),
    temperature=0.1
)

res = llm.invoke("Say hello in one line.")
print(res.content)