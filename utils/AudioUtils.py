from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

import asyncio
from googletrans import Translator

filename = "./OSR_in_000_0062_16k.wav" 

def get_text_from_audio(file_path, language_code, model="whisper-large-v3-turbo"):
    with open(file_path, "rb") as file:
        
        transcription = client.audio.transcriptions.create(
          file=(filename, file.read()), 
          model=model,
          language=language_code 
        )
        
        return transcription.text

def get_text_from_audio_bytes(audio_bytes, language_code, model="whisper-large-v3-turbo"):
        
    transcription = client.audio.transcriptions.create(
        file=("query_audio.wav", audio_bytes), 
        model=model,
        language=language_code 
    )
    
    return transcription.text

async def translate_text(text):
    translator = Translator()
    
    translated = await translator.translate(text, dest='en')
    return translated.text
    
async def convert_to_english(text):
    translated_text = await translate_text(text)
    return translated_text

def get_en_text_from_audio_bytes(audio_bytes, language_code, model="whisper-large-v3-turbo"):
        
    transcription = client.audio.transcriptions.create(
        file=("query_audio.wav", audio_bytes), 
        model=model,
        language=language_code 
    )
    
    translated_text = asyncio.run(convert_to_english(transcription.text))
    return translated_text

async def translate_to_lang(text, dest, src='en'):
    translator = Translator()
    translation = await translator.translate(text, src=src, dest=dest)
    return translation.text



if __name__ == "__main__":
    text = "Hello, how are you?"
    ans = asyncio.run(translate_to_lang(text, "te"))
    print(ans)
    
