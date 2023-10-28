# dashboard7.py
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def main():
    # Assuming df_startup is already defined and contains the necessary data
    # If not, load your data and perform the required processing
    # Load data
    file_path = r"C:\Users\VARUN\Desktop\DataHack\startup_funding_all_years.csv"
    df_startup = pd.read_csv(file_path)

    # Group the DataFrame by 'HeadQuarter' and calculate the total funding amount received by startups in each region
    funding_by_region = df_startup.groupby('HeadQuarter')['Amount($)'].sum()

    # Sort the regions by total funding amount and take only the top 20
    top20 = funding_by_region.sort_values(ascending=False)[:20]

    # Create an interactive scatter plot using Plotly Express with a different color scale (Viridis)
    fig = px.scatter(
        x=top20.index,
        y=[1] * len(top20),
        size=top20.values / 5000000,
        size_max=50,
        color=top20.values,
        labels={'size': 'Total Funding Amount ($ Billions)'},
        title='Total Funding Received by the Top 20 Startups in Each Region',
        template='plotly_dark',
        color_continuous_scale='teal',  # Change color scale here
        hover_name=top20.index,  # Show region names on hover
    )

    # # Customize layout for the plot
    # fig.update_layout(
    #     xaxis_title='Region',
    #     yaxis_title='Size of bubble represents total funding amount ($ Billions)',
    #     xaxis=dict(tickangle=45),
    # )
    
    fig.update_layout(
    height=600,  # Adjust the height
    width=800,   # Adjust the width
    )


    # Display the interactive plot
    st.plotly_chart(fig)

    # Additional interactivity
    st.markdown("## Additional Options")

    # Option for selected region details
    selected_region = st.selectbox('Select a Region:', top20.index)
    st.write(f"Total funding received by {selected_region}: ${funding_by_region[selected_region] / 1e9:.2f} Billion")

    # Highlight the selected region on the plot
    selected_city_mask = df_startup['HeadQuarter'] == selected_region
    fig.add_trace(
        go.Scatter(
            x=[selected_region],
            y=[1],
            mode='markers',
            marker=dict(size=funding_by_region[selected_region] / 5000000, color='red'),
            name=f'Selected: {selected_region}',
            showlegend=False,
        )
    )

    # Option for summary statistics
    st.markdown("## Summary Statistics")
    st.write(f"Total funding received by the top 20 startups: ${top20.sum() / 1e9:.2f} Billion")

if __name__ == "__main__":
    main()
