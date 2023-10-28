# dashboard5.py
import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    # Load data
    file_path = r"C:\Users\VARUN\Desktop\DataHack\startup_funding_all_years.csv"
    df_startup = pd.read_csv(file_path)

    st.title("Interactive Dashboard 4: Funding Trend Over the Years")

    # Convert 'Year' column to pandas Datetime object
    df_startup['Year'] = pd.to_datetime(df_startup['Year'], format='%Y')

    # Sort the DataFrame by 'Year' column
    df_startup = df_startup.sort_values(by='Year')

    # Group the DataFrame by 'Year' and calculate the total funding amount for each year
    df_funding_by_year = df_startup.groupby('Year')['Amount($)'].sum().reset_index()

    # Create an interactive line plot using Plotly Express
    fig = px.line(
        df_funding_by_year,
        x='Year',
        y='Amount($)',
        labels={'Amount($)': 'Total Funding Amount($ Billion)'},
        title='Trend in the Amount of Funding Received over the Years',
        line_shape='linear',
        template='plotly_dark',
        hover_name='Amount($)',
    )

    # Customize layout for the plot
    fig.update_layout(
        height=600,
        width=800,
        xaxis_title='Year',
        yaxis_title='Total Funding Amount($ Billion)',
        showlegend=False,
        margin=dict(l=0, r=0, t=50, b=0),
    )

    # Display the interactive plot
    st.plotly_chart(fig)

    # Additional interactivity
    st.sidebar.header("Additional Options")

    # Option to show raw data
    if st.sidebar.checkbox("Show Raw Data"):
        st.subheader("Raw Funding Data")
        st.dataframe(df_startup)

    # Option for interactive summary statistics
    st.sidebar.header("Interactive Summary Statistics")
    selected_year = st.sidebar.selectbox("Select a Year", df_funding_by_year['Year'].dt.year.unique())
    year_summary = df_startup[df_startup['Year'].dt.year == selected_year]['Amount($)'].describe()
    
    st.subheader(f"Summary Statistics for {selected_year}")
    st.write(year_summary)

if __name__ == "__main__":
    main()
