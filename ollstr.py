import streamlit as st
import ollama
import time

# Function to stream data with a delay
def stream_data(text, delay: float = 0.02):
    for word in text.split():
        yield word + " "
        time.sleep(delay)

# Chat input for user prompt
prompt = st.chat_input("Ask anything")

if prompt:
   
    st.write(f"You: {prompt}")

    with st.spinner("Thinking..."):
        
        result = ollama.chat(model="llama2", messages=[{
            "role": "user",
            "content": prompt, 
        }])

        response = result["message"]["content"]

        response_placeholder = st.empty()

        full_response = ""
        for word in stream_data(response):
            full_response += word
            response_placeholder.markdown(full_response)



