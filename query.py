import streamlit as st
import pandas as pd
import os
from pandasai import PandasAI
from pandasai.llm import Falcon
from pandasai import SmartDataframe
from dotenv import load_dotenv

# Load OpenAI API key from .env file
load_dotenv()
hfat = os.getenv("HUGGINGFACE_API_KEY")

# Instantiate LLM and PandasAI objects
llm = Falcon(api_key=hfat, use_auth_token=True)


# @st.cache(allow_output_mutation=True)
# def initialize_falcon_model():
#     llm = Falcon(api_token=hfat, use_Auth_token=True)
#     return llm

# llm = initialize_falcon_model()

# Function to load data, cached to avoid re-execution
# @st.cache(allow_output_mutation=True)
# def load_data(file_path):
#     try:
#         return pd.read_csv(file_path)
#     except Exception as e:
#         st.error(f"Error loading data: {str(e)}")

# Function to perform chatbot response
# def chatbot_response(question, data):
#     try:
#         # Use pandas_ai to generate response
#         return pandas_ai.run(data, question)
#     except Exception as e:
#         st.error(f"Error generating chatbot response: {str(e)}")

# Function to display data and chatbot response
def display_data_and_response(data, question):
    st.subheader("Preview of the Data:")
    st.dataframe(data.head(5))

    st.subheader("Chatbot Response:")
    chatbot_reply = data.chat(question)
    
    # if chatbot_reply is none assign a default value of no answer
    if chatbot_reply is None:
        chatbot_reply = "Answer not found. Sorry!"
    
    print("this is reply",chatbot_reply)
    st.markdown(f"_{chatbot_reply}_")

# Main function
def query():
    st.title("DataWiz - Chatbot and Table")

    # Load the data, cached to avoid re-execution
    file_path = r"startup_funding_all_years.csv"
    # df_startup = load_data(file_path)
    df = pd.read_csv(file_path)
    df_startup = SmartDataframe(df, config={"llm": llm})
    


    # Display the first few rows of the data and chatbot response
    user_input = st.text_input("You:", "Type your question here...")

    if user_input:
        display_data_and_response(df_startup, user_input)

        # Add a button to trigger the chatbot
        if st.button("Ask Chatbot"):
            display_data_and_response(df_startup, user_input)  # Use user's question

if __name__ == "__main__":
    query()
