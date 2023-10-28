# dashboard1.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title("Dashboard 1")

    # Your dashboard content for the first dashboard

    # Section: Top 10 Startups by Revenue
    st.header("Top 10 Startups by Revenue (Last 5 Years)")

    # Sample data for demonstration purposes
    startup_data = {
        "Startup 1": {"Revenue": 1000000},
        "Startup 2": {"Revenue": 900000},
        "Startup 3": {"Revenue": 800000},
        "Startup 4": {"Revenue": 700000},
        "Startup 5": {"Revenue": 600000},
        "Startup 6": {"Revenue": 500000},
        "Startup 7": {"Revenue": 400000},
        "Startup 8": {"Revenue": 300000},
        "Startup 9": {"Revenue": 200000},
        "Startup 10": {"Revenue": 100000}
    }

    # Convert data to a DataFrame for plotting
    df = pd.DataFrame(startup_data).T

    # Plot a bar chart
    fig, ax = plt.subplots()
    df["Revenue"].sort_values(ascending=False).plot(kind="bar", ax=ax, color='skyblue')
    ax.set_xlabel("Startups")
    ax.set_ylabel("Revenue ($)")
    ax.set_title("Top 10 Startups by Revenue")

    # Display the bar chart in the Streamlit app
    st.pyplot(fig)

if __name__ == "__main__":
    main()
