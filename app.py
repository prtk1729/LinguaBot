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
            
            # after getting the response from llm, we have saved in "sppech.mp3"
            audio_file=open("speech.mp3","rb")
            audio_bytes=audio_file.read()
            
            
            st.text_area(label="Response", 
                         value=response, 
                         height=350)
            st.audio(audio_bytes)
            st.download_button(label="Download Speech", 
                               data=audio_bytes, 
                               file_name="speech.mp3", 
                               mime="audio/mp3")


if __name__=='__main__':
    main()