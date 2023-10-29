# dashboard4.py
import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    # Load data
    file_path = r"startup_funding_all_years.csv"
    df_startup = pd.read_csv(file_path)

    st.title("Interactive Dashboard 3: Top Investors and Sectors by Total Funding Amount")

    # Group by investor and calculate total funding amount
    investor_funding = df_startup.groupby('Investor')['Amount($)'].sum().reset_index()

    # Create a slider for selecting the number of top investors to display
    num_investors = st.slider("Select the number of top investors to display:", min_value=1, max_value=20, value=10)

    # Select top investors based on user's selection
    top_investors = investor_funding.nlargest(num_investors, 'Amount($)')

    # Create an interactive horizontal bar plot for top investors using Plotly Express
    fig1 = px.bar(
        top_investors,
        x='Amount($)',
        y='Investor',
        color='Amount($)',
        orientation='h',  # horizontal orientation
        labels={'Amount($)': 'Total Funding Amount ($100 B)'},
        title=f'Top {num_investors} Investors by Total Funding Amount',
    )

    # Customize layout for the first plot
    fig1.update_layout(
        height=800,
        width=1200,
        xaxis_title='Total Funding Amount ($100 B)',
        yaxis_title='Investor',
    )

    # Display the first interactive plot
    st.plotly_chart(fig1)

    # Filter the data for the years 2018-2021
    df_startup = df_startup[(df_startup["Year"] >= 2018) & (df_startup["Year"] <= 2021)]

    # Group the data by investor and sector, and sum the amount raised by each sector for each investor
    investor_sector_funding = df_startup.groupby(['Investor', 'Sector'])["Amount($)"].sum().reset_index()

    # Sort the data by the amount raised in descending order
    investor_sector_funding = investor_sector_funding.sort_values("Amount($)", ascending=False)

    # Print the top 5 sectors by funding amount
    st.subheader("Top 10 Sectors by Funding Amount:")
    st.dataframe(investor_sector_funding.head(10))

    # Create a dropdown to select an investor
    selected_investor_name = st.selectbox('Select an Investor:', top_investors['Investor'])

    # Filter data for the selected investor
    selected_investor_data = investor_sector_funding[investor_sector_funding['Investor'] == selected_investor_name]

    # Create an interactive sunburst chart for sectors using Plotly Express for the selected investor
    fig2 = px.sunburst(
        selected_investor_data,
        path=['Investor', 'Sector'],
        values='Amount($)',
        title=f'Investment Amounts by Sector for {selected_investor_name}',
        hover_data=['Amount($)']
    )

    # Customize layout for the second plot
    fig2.update_layout(
        height=800,
        width=1200,
    )

    # Display the second interactive plot
    st.plotly_chart(fig2)

    # Display the data used to create the second plot
    st.subheader(f'Data for {selected_investor_name} - Investment Amounts by Sector:')
    st.dataframe(selected_investor_data[['Investor', 'Sector', 'Amount($)']])

    # Additional insights based on the selected investor's data
    st.subheader("Investor Insights:")

    # Average investment amount for the selected investor
    avg_investment = selected_investor_data['Amount($)'].mean()
    st.markdown(
        """
        - **Average Investment Amount:** ${:.2f} Billion USD
        """.format(avg_investment / 1e9)
    )

if __name__ == "__main__":
    main()
