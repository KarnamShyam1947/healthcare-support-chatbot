from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

def analyze_image_with_query(query: str, encoded_image: str, model: str="llama-3.2-90b-vision-preview") -> str:
    print("call with query and image")
    client=Groq(
        api_key=os.getenv("GROQ_API_KEY")
    )  
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }
    ]
    
    chat_completion=client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content

def analyze_with_query(query: str, model: str="llama-3.2-90b-vision-preview") -> str:
    client=Groq(
        api_key=os.getenv("GROQ_API_KEY")
    )  
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": query
                },
            ],
        }
    ]
    
    chat_completion=client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content

def analyze_with_image(encoded_image: str, model: str="llama-3.2-90b-vision-preview") -> str:
    client=Groq(
        api_key=os.getenv("GROQ_API_KEY")
    )  
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }
    ]
    
    chat_completion=client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content
