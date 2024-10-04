import streamlit as st
from chat import init_cs_bot_session

st.title('AI Chatbot Kabinet Baskara HIMA IF Universitas Telkom 2024')

# Initialize the chatbot session and message history
if 'chat_bot' not in st.session_state:
    st.session_state['chat_bot'] = init_cs_bot_session()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Set a welcome message tailored for Kabinet Baskara
if "welcome_message" not in st.session_state:
    st.session_state.welcome_message = "Selamat datang di AI Chatbot Kabinet Baskara HIMA IF 2024! Saya di sini untuk membantu menjawab pertanyaan seputar kabinet ini, termasuk struktur organisasi, program kerja, dan peran departemen. Apa yang ingin Anda ketahui hari ini?"

# Display the welcome message before any user input
if len(st.session_state.messages) == 0:
    st.session_state.messages.append({"role": "assistant", "content": st.session_state.welcome_message})

# Capture user input
user_input = st.chat_input()

# Process user input and handle the logo query
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # If the user asks about the logo, display the logo after the user's input
    if "logo" in user_input.lower():
        st.session_state.messages.append({"role": "assistant", "content": "Berikut adalah logo Kabinet Baskara HIMA IF 2024:"})
        st.session_state.messages.append({"role": "assistant", "content": "image"})  # Placeholder for image in message history
    else:
        model_answer = st.session_state['chat_bot'].send_message(user_input).candidates[0].content.parts[0].text.strip()
        st.session_state.messages.append({"role": "assistant", "content": model_answer})

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["content"] == "image":
            st.image("Logo_Kabinet_Baskara.png")  # Make sure the logo file is accessible in the directory
        else:
            st.markdown(message["content"])
