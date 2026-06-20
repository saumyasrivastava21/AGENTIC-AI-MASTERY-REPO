import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url=os.getenv("NVIDIA_BASE_URL"),
    api_key=os.getenv("NVIDIA_API_KEY")
)

completion = client.chat.completions.create(
    model=os.getenv("NVIDIA_MODEL"),
    messages=[
        {
            "role": "user",
            "content": "Explain AI agents in 5 lines."
        }
    ],
    temperature=0.2,
    top_p=0.7,
    max_tokens=512
)

print(completion.choices[0].message.content)