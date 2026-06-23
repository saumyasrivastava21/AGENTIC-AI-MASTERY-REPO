import os
from dotenv import load_dotenv
from langchain_nvidia_ai_endpoints import ChatNVIDIA
load_dotenv()


def get_llm(temperature: float = 0.1):
    api_key = os.getenv("NVIDIA_API_KEY")
    model = os.getenv("NVIDIA_MODEL", "meta/llama-3.3-70b-instruct")

    if not api_key:
        raise ValueError("NVIDIA_API_KEY missing in .env")

    return ChatNVIDIA(
        model=model,
        api_key=api_key,
        temperature=temperature
    )