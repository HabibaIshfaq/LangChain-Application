import openai
import os
from dotenv import load_dotenv
import streamlit as st

# Load environment variables from the .env file
load_dotenv()

# Function to get OpenAI response
def get_openai_response(question):
    # Get API key from environment variables
    api_key = os.getenv("OPENAI_API_KEY")
    
    # Set API key for OpenAI
    openai.api_key = api_key
    
    # Request response from the chat model using the correct method
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Chat model
        messages=[{"role": "user", "content": question}],  # Format the prompt as a chat message
        temperature=0.5,         # Control randomness of the response
        max_tokens=150           # Limit the response length
    )
    
    # Extract and return the response text
    return response['choices'][0]['message']['content']

# Initialize Streamlit app
st.set_page_config(page_title="Q/A demo")

st.header("Langchain Application")
input = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

# If the button is clicked, get the response from OpenAI
if submit:
    response = get_openai_response(input)
    st.subheader("The response is")
    st.write(response)
