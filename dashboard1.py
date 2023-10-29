# dashboard2.py
import streamlit as st
import pandas as pd
import plotly.express as px

def load_and_preprocess_data():
    # Load datasets from 2018 to 2021
    # data_2018 = pd.read_csv(r"C:\Users\VARUN\Desktop\DataHack\2018_2021_funding\startup_funding2018.csv")
    # data_2019 = pd.read_csv(r"C:\Users\VARUN\Desktop\DataHack\2018_2021_funding\startup_funding2019.csv")
    # data_2020 = pd.read_csv(r"C:\Users\VARUN\Desktop\DataHack\2018_2021_funding\startup_funding2020.csv")
    # data_2021 = pd.read_csv(r"C:\Users\VARUN\Desktop\DataHack\2018_2021_funding\startup_funding2021.csv")

    data_2018 = pd.read_csv(r"datasets\kaggle_18_21\startup_funding2018.csv")
    data_2019 = pd.read_csv(r"datasets\kaggle_18_21\startup_funding2019.csv")
    data_2020 = pd.read_csv(r"datasets\kaggle_18_21\startup_funding2020.csv")
    data_2021 = pd.read_csv(r"datasets\kaggle_18_21\startup_funding2021.csv")
    # Concatenate datasets
    all_data = pd.concat([data_2018, data_2019, data_2020, data_2021], ignore_index=True)

    # Remove duplicates based on all columns
    all_data = all_data.drop_duplicates(subset=['Company Name', 'Industry', 'Round/Series', 'Amount', 'Location', 'About Company'])

    # Filter data for specific funding rounds
    target_rounds = ['Seed', 'Series A', 'Series B', 'Series C', 'Angel', 'Post-IPO Equity', 'Post-IPO Debt']
    filtered_data = all_data[all_data['Round/Series'].isin(target_rounds)]

    return filtered_data


def generate_bubble_chart(data):
    # Count the number of startups for each unique round type
    round_counts = data['Round/Series'].value_counts()

    # Create a DataFrame for the bubble chart
    bubble_data = pd.DataFrame({
        'Round': round_counts.index,
        'Number of Startups': round_counts.values
    })

    # Take only the top 19 funding rounds
    bubble_data = bubble_data.head(19)

    # Create a bubble chart with larger dimensions and increased bubble size
    fig = px.scatter(
        bubble_data,
        x='Round',
        y='Number of Startups',
        size='Number of Startups',
        labels={'Number of Startups': 'Number of Startups'},
        title='Number of Startups in Different Funding Rounds',
        size_max=100  # Adjust the size of the bubbles
    )

    # Set the size of the plot
    fig.update_layout(
        height=800,  # Set the height in pixels
        width=1000    # Set the width in pixels
    )

    return fig

# Main function for Streamlit application
def main():
    st.title("Startup Funding Insights")

    # Load and preprocess data
    data = load_and_preprocess_data()

    # Display section text
    st.write("Exploring Funding Rounds and Startup Growth")

    # Generate and display the bubble chart
    st.plotly_chart(generate_bubble_chart(data))

    # Highlight key insights
    st.subheader("Key Insights:")
    st.markdown(
        """
        1. Maturation and Growth:
            The progression from Seed to Series A indicates the startup's successful navigation through initial stages, demonstrating market validation and readiness for significant growth.
        2. Market Confidence:
            Series A funding suggests a higher level of investor scrutiny, reflecting confidence in the business model and market potential.
        3. Strategic Angel Support:
            Ongoing involvement of angel investors in later stages signifies strategic support beyond initial funding, bringing industry expertise and mentorship.
        """
    )

if __name__ == "__main__":
    main()