# dashboard6.py
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def main():
    # Load data
    file_path = r"C:\Users\VARUN\Desktop\DataHack\startup_funding_all_years.csv"
    df_startup = pd.read_csv(file_path)

    st.title("Interactive Dashboard 5: Number of New Startups Formed Each Year")

    # Group the DataFrame by 'Year' and calculate the number of new startups each year
    num_startups_by_year = df_startup['Year'].value_counts().sort_index()

    # Sidebar with user input for selecting a range of years
    st.sidebar.header("Select Year Range")
    selected_years = st.sidebar.slider("Select Year Range", min_value=int(num_startups_by_year.index.min()), max_value=int(num_startups_by_year.index.max()), value=(2018, 2021))

    # Filter data based on the selected year range
    filtered_startups = num_startups_by_year.loc[selected_years[0]:selected_years[1]]

    # Create an interactive bar chart using Plotly Express
    fig = px.bar(
        x=filtered_startups.index,
        y=filtered_startups.values,
        labels={'y': 'Number of New Startups'},
        title=f'Number of New Startups Formed Each Year ({selected_years[0]} to {selected_years[1]})',
        template='plotly_dark',
    )

    # Add a line connecting the top of each histogram bar
    line_trace = go.Scatter(
        x=fig.data[0].x,
        y=fig.data[0].y,
        mode='lines+markers',
        marker=dict(color='red'),
        line=dict(color='red', width=2),
        name='Line at the Top',
    )

    # Update layout to include both bar chart and line plot
    fig.update_layout(
        height=600,
        width=800,
        xaxis_title='Year',
        yaxis_title='Number of New Startups',
        margin=dict(l=0, r=0, t=50, b=0),
    )

    # Add the line plot to the existing figure
    fig.add_trace(line_trace)

    # Display the interactive plot
    st.plotly_chart(fig)

    # Additional interactivity
    st.sidebar.header("Additional Options")

    # Option for summary statistics
    st.sidebar.header("Summary Statistics")
    st.sidebar.write(f"Total number of years: {len(num_startups_by_year)}")
    st.sidebar.write(f"Average startups per year: {num_startups_by_year.mean():.2f}")

if __name__ == "__main__":
    main()
