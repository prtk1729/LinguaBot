import streamlit as st
from linguabot.helper import get_voice_input, text_to_speech, get_response_from_llm



def main():
    st.title("Cross-Language AI Companion 🤖")
    
    if st.button("Ask me anything"):
        # viz the spinner to listen
        with st.spinner("Listening..."):
            text = get_voice_input() # speech to text
            response = get_response_from_llm(text)
            text_to_speech(response) # back to speech
            
            
            audio_file=open("speech.mp3","rb")
            audio_bytes=audio_file.read()
            
            
            st.text_area()
            st.audio()
            st.download_button()


if __name__=='__main__':
    main()