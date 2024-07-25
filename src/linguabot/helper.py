import google.generativeai as genai
from dotenv import load_dotenv
import os
from gtts import gTTS
import speech_recognition as sr


# load env vars
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY

def get_voice_input():
    pass

def text_to_speech():
    pass

def get_response_from_llm():
    pass

