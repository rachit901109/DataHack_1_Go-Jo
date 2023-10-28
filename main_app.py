import streamlit as st
from dashboard1 import main as dashboard1
from dashboard2 import main as dashboard2
from dashboard3 import main as dashboard3  # Placeholder for Dashboard 3
from dashboard4 import main as dashboard4  # Placeholder for Dashboard 4
from dashboard5 import main as dashboard5  # Placeholder for Dashboard 5
from dashboard6 import main as dashboard6  # Placeholder for Dashboard 6
# from dashboard7 import main as dashboard7  # Placeholder for Dashboard 7

def main():
    st.set_page_config(
        page_title="DataWiz",
        page_icon=":bar_chart:",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title("DataWiz")

    st.sidebar.title("Dashboards")

    # Create an expander for Dashboards
    with st.sidebar.expander("Dashboards"):
        selected_dashboard = st.radio("Go to", ("Startup Funding Insights", "Top Funding Amounts", "Top Investors and Sectors by Total Funding Amount", "Funding Trend Over the Years", "Number of New Startups Formed Each Year", "Total Funding in each region"))

    if selected_dashboard == "Startup Funding Insights":
        dashboard1()
    elif selected_dashboard == "Top Funding Amounts":
        dashboard2()
    elif selected_dashboard == "Top Investors and Sectors by Total Funding Amount":
        dashboard3()
    elif selected_dashboard == "Funding Trend Over the Years":
        dashboard4()
    elif selected_dashboard == "Number of New Startups Formed Each Year":
        dashboard5()
    elif selected_dashboard == "Total Funding in each region":
        dashboard6()
    # elif selected_dashboard == "Dashboard 7":
    #     dashboard7()


if __name__ == "__main__":
    main()
