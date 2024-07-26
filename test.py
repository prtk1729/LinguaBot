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
    # recognizer object
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening... Say something!")
        audio_obj = recognizer.listen(source)

    try:
        # speech to text
        text = sr.recognize_google(audio_obj)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print(f"Couldn't understand what you just said")
    except sr.RequestError as e:
        print(f"Couldn't access Google's speech recognition service: {e} ")

def get_response_from_llm(user_text):
    '''
    Args:
        - user_text: User's speech through Mic converted to text
    '''
    model_name = "gemini-pro"
    model = genai.GenerativeModel(model_name)
    prompt = user_text
    response = model.generate_content(prompt)
    result = response.text
    return result

def text_to_speech(llm_response_text):
    '''
    Args:
        - llm_response_text: Takes LLM response as input
    Action:
        - Sets up the tts
        - Saves the final audio in a mp3 file
    '''
    tts = gTTS(text = llm_response_text, lang = "en")
    tts.save("speech.mp3")
    return




    

