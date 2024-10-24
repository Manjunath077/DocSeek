# import streamlit as st


# st.title("Gpt Clone")



from dotenv import load_dotenv
import os
from openai import OpenAI
import streamlit as st
from streamlit_extras.let_it_rain import rain

st.set_page_config(layout="wide")  # Set page layout to wide

st.title("Generative AI")

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
    st.stop()

client = OpenAI(api_key=api_key)

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to reset chat and display previous question tag in sidebar
def reset_chat():
    st.session_state.messages.clear()

# Sidebar with New Chat button
if st.sidebar.button("New Chat"):
    reset_chat()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.text_input("What's up?")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})

# Display previous questions in the sidebar
for message in st.session_state.messages:
    if message["role"] == "user":
        st.sidebar.markdown(f"Previous Question: {message['content']}")


# Function to apply snowfall effect
def run_snow_animation():
    rain(emoji="❄️", font_size=20, falling_speed=5, animation_length="infinite")

# Run snowfall animation
run_snow_animation()

