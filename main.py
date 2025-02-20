import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables securely
dotenv_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path)

# Get API key and verify it's available
api_key = os.getenv('GOOGLE_API_KEY')
if not api_key:
    st.error("Google API key not found. Please check your .env file.")
    st.stop()

# Initialize Gemini API with error handling
try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    st.error(f"Failed to initialize Gemini API: {str(e)}")
    st.stop()

# Page configuration
st.set_page_config(
    page_title="Jarvis Chat Bot (Powered by Gemini)",
    page_icon="💭",
    layout="centered"
)

# Load custom CSS safely
try:
    with open('styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
except Exception as e:
    st.warning(f"Failed to load custom styles: {str(e)}")

def initialize_session_state():
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'chat' not in st.session_state:
        st.session_state.chat = model.start_chat(history=[])
    if 'error' not in st.session_state:
        st.session_state.error = None

def send_message(message):
    try:
        response = st.session_state.chat.send_message(message)
        return response.text if response else "No response received."
    except genai.APIError as e:
        st.session_state.error = f"API Error: {str(e)}"
    except Exception as e:
        st.session_state.error = f"Unexpected Error: {str(e)}"
    st.error(st.session_state.error)
    return None

def main():
    initialize_session_state()

    st.markdown('<div class="chat-header">'
                '<h1>💭 Jarvis AI Chat Bot</h1>'
                '<p>Ask me anything and I'll help you out!</p>'
                '</div>', unsafe_allow_html=True)

    if st.session_state.error:
        st.warning(st.session_state.error)
        if st.button("Clear Error"):
            st.session_state.error = None
            st.rerun()

    for message in st.session_state.messages:
        role_class = "user-message" if message["role"] == "user" else "assistant-message"
        st.markdown(f'<div class="{role_class}">{message["content"]}</div>', unsafe_allow_html=True)

    with st.form("chat_form"):
        user_input = st.text_area("Your message:", key="user_input", height=100)
        send_button = st.form_submit_button("Send")

        if send_button and user_input.strip():
            st.session_state.messages.append({"role": "user", "content": user_input})
            with st.spinner("AI is thinking..."):
                ai_response = send_message(user_input)
                if ai_response:
                    st.session_state.messages.append({"role": "assistant", "content": ai_response})
            st.rerun()

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.session_state.chat = model.start_chat(history=[])
        st.session_state.error = None
        st.rerun()

if __name__ == "__main__":
    main()
