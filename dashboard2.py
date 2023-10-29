# dashboard3.py
import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    # Load data
    file_path = r"startup_funding_all_years.csv"
    df = pd.read_csv(file_path)

    st.title("Interactive Dashboard 2: Top Funding Amounts")

    # Create a slider for selecting the number of top companies to display
    num_companies = st.slider("Select the number of top companies to display:", min_value=1, max_value=20, value=10)

    # Filter top funding data based on the user's selection
    df_top_funding = df[['Amount($)', 'Company/Brand', 'Sector']].sort_values(by='Amount($)', ascending=False).head(num_companies)

    # Create an interactive bar plot using Plotly Express with a different color scale (Blues)
    fig = px.bar(
        df_top_funding,
        x='Amount($)',
        y='Company/Brand',
        color='Amount($)',
        orientation='h',  # horizontal orientation
        labels={'Amount($)': 'Funding Amount (in $100 Billions)'},
        title=f'Top {num_companies} Funding Amounts for Companies/Brands',
        color_continuous_scale='Blues',  # Change color scale here
    )

    # Customize layout
    fig.update_layout(
        height=600,
        width=800,
        xaxis_title='Funding Amount (in $100 Billions)',
        yaxis_title='Company/Brand',
    )

    # Display the interactive plot
    st.plotly_chart(fig)

    # Additional statistics and insights
    st.subheader("Additional Insights:")
    st.markdown(
        """
        - **Total Funding Amount:** ${:.2f} Billion USD
        - **Average Funding Amount:** ${:.2f} Billion USD
        - **Maximum Funding Amount:** ${:.2f} Billion USD (Company: {})
        """.format(
            df['Amount($)'].sum() / 1e9,
            df['Amount($)'].mean() / 1e9,
            df['Amount($)'].max() / 1e9,
            df.loc[df['Amount($)'].idxmax(), 'Company/Brand']
        )
    )

    # Dominant sectors in terms of funding amounts
    st.subheader("Dominant Sectors:")
    top_sectors = df.groupby('Sector')['Amount($)'].sum().sort_values(ascending=False).head(3)
    st.write(top_sectors)

    # Additional insights for investors
    st.subheader("Investor Insights:")
    
    # Diversification
    sectors_count = df['Sector'].nunique()
    st.markdown(
        """
        - **Diversification:** Consider diversifying investments across the available {} sectors to mitigate risks.
        """.format(sectors_count)
    )

    # Sector Trends
    sector_trends = df.groupby('Sector')['Amount($)'].mean().sort_values(ascending=False)
    st.markdown(
        """
        - **Sector Trends:** Identify sectors with consistently high average funding amounts, indicating sustained growth. For example, the top sectors by average funding are:
            - {}
        """.format(', '.join(sector_trends.head(3).index))
    )

    # Research Top Companies
    st.markdown(
        """
        - **Research Top Companies:** Investigate the top-funded companies for potential investment opportunities. For example, consider exploring opportunities with the company '{}' that received the maximum funding amount.
        """.format(df.loc[df['Amount($)'].idxmax(), 'Company/Brand'])
    )

if __name__ == "__main__":
    main()
