import streamlit as st
from dashboard1 import main as dashboard1
from dashboard2 import main as dashboard2
from dashboard3 import main as dashboard3
from dashboard4 import main as dashboard4
from dashboard5 import main as dashboard5
from dashboard6 import main as dashboard6
from query import query

def main():
    st.set_page_config(
        page_title="DataWiz",
        page_icon=":bar_chart:",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title("DataWiz - Dashboard Hub")

    st.sidebar.title("Dashboards")

    # Create an expander for Dashboards
    with st.sidebar.expander("Select Dashboard"):
        dashboard_options = {
            "Startup Funding Insights": "Explore insights into startup funding.",
            "Top Funding Amounts": "Discover the top funding amounts for startups.",
            "Top Investors and Sectors by Total Funding Amount": "See top investors and sectors by total funding.",
            "Funding Trend Over the Years": "Visualize the funding trend over the years.",
            "Number of New Startups Formed Each Year": "Explore the number of new startups each year.",
            "Total Funding in each region": "View total funding in each region.",
        }

        selected_dashboard = st.radio("Go to", list(dashboard_options.keys()))

        # Display description of the selected dashboard
        st.write(f"**Dashboard Description:** {dashboard_options[selected_dashboard]}")

    # Flag to determine if chatbot section should be displayed
    show_chatbot_section = st.sidebar.button("Chatbot and Table")

    # Display selected dashboard or chatbot section
    if not show_chatbot_section:
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
    else:
        query()

if __name__ == "__main__":
    main()
