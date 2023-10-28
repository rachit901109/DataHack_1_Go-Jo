import streamlit as st
import pandas as pd
import os
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI API key
openai_api_key = os.environ.get("OPENAI_API_KEY")

# Instantiate LLM and PandasAI objects
llm = OpenAI(api_token=openai_api_key)
pandas_ai = PandasAI(llm)

# Function to load data, cached to avoid re-execution
@st.cache(allow_output_mutation=True)
def load_data(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")

# Function to perform chatbot response
def chatbot_response(question, data):
    try:
        # Use pandas_ai to generate response
        return pandas_ai.run(data, question)
    except Exception as e:
        st.error(f"Error generating chatbot response: {str(e)}")

# Function to display data and chatbot response
def display_data_and_response(data, question):
    st.subheader("Preview of the Data:")
    st.dataframe(data.head())

    st.subheader("Chatbot Response:")
    chatbot_reply = chatbot_response(question, data)
    st.markdown(f"_{chatbot_reply}_")

# Main function
def query():
    st.title("DataWiz - Chatbot and Table")

    # Load the data, cached to avoid re-execution
    file_path = r"C:\Users\VARUN\Desktop\DataHack\startup_funding_all_years.csv"
    df_startup = load_data(file_path)

    # Display the first few rows of the data and chatbot response
    user_input = st.text_input("You:", "Type your question here...")

    if user_input:
        display_data_and_response(df_startup, user_input)

        # Add a button to trigger the chatbot
        if st.button("Ask Chatbot"):
            display_data_and_response(df_startup, user_input)  # Use user's question

if __name__ == "__main__":
    query()
