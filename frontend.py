import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# ==============================================================================
# 1. API Setup & Configuration
# ==============================================================================
load_dotenv()
api_key = os.getenv("OPEN_AI_SECRET_KEY")
client = OpenAI(api_key=api_key)


def ask_gpt(prompt):
    try:
        # Calls your specified model API endpoint
        response = client.responses.create(
            model="gpt-5.6-terra",
            input=prompt,
        )
        return response.output_text
    except Exception as e:
        return f"Error connecting to model: {str(e)}"


# ==============================================================================
# 2. UI Layout & Session Initialization
# ==============================================================================
st.set_page_config(page_title="GPT Chat UI", page_icon="💬", layout="centered")
st.title("GPT-5.6 Terra Chat")

# Initialize persistent message history list
if "messages" not in st.session_state:
    st.session_state.messages = []

# ==============================================================================
# 3. Chat Rendering & Input Processing
# ==============================================================================
# Display previous messages sequentially
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Capture new user text interaction
if prompt := st.chat_input("Message GPT-5.6 Terra..."):
    # Immediately render user text locally
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Process and render model feedback
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        with st.spinner("Thinking..."):
            answer = ask_gpt(prompt)
        message_placeholder.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
