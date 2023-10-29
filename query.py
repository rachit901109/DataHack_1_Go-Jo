import streamlit as st
import pandas as pd
import os
from pandasai import PandasAI
from pandasai.llm import GooglePalm  # Import GooglePalm
from pandasai import SmartDataframe
from dotenv import load_dotenv

# Load Google Palm API key from .env file
load_dotenv()
google_palm_api_key = os.getenv("GOOGLE_PALM_API_KEY")

# Instantiate LLM and PandasAI objects using GooglePalm
llm = GooglePalm(api_key=google_palm_api_key)

# Function to display data and chatbot response
def display_data_and_response(data, question):
    st.subheader("Preview of the Data:")
    st.dataframe(data.head(5))

    st.subheader("Chatbot Response:")
    chatbot_reply = data.chat(question)
    print(chatbot_reply)

    # Check if chatbot_reply is a dictionary
    # if isinstance(chatbot_reply, dict):
    #     # Check if "type" is in the dictionary
    #     if "type" in chatbot_reply:
    #         # If chatbot_reply["type"] is None or empty, assign a default value of no answer
    #         response_type = chatbot_reply["type"] or "Answer not found. Sorry!"
    #         st.markdown(f"_{response_type}_")
    #     else:
    #         st.markdown("_Answer not found. Sorry!_")
    # else:
    #     st.markdown("_Answer not found. Sorry!_")

    # Display chatbot reply in Streamlit
    st.write("Chatbot Reply:", chatbot_reply)

# Main function
def query():
    st.title("DataWiz - Chatbot and Table")

    # Load the data
    file_path = "startup_funding_all_years.csv"
    df = pd.read_csv(file_path)
    df_startup = SmartDataframe(df, config={"llm": llm})

    # Display the first few rows of the data and chatbot response
    user_input = st.text_input("You:", "")
    # user_input = st.text_input("You:", "")
    if user_input:
        display_data_and_response(df_startup, user_input)

        # Add a button to trigger the chatbot
        if st.button("Ask Chatbot"):
            display_data_and_response(df_startup, user_input)  # Use user's question

if __name__ == "__main__":
    query()
