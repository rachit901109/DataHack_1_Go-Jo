# main_app.py
import streamlit as st
from dashboard1 import main as dashboard1
from dashboard2 import main as dashboard2

def main():
    st.sidebar.title("Dashboards")
    selected_dashboard = st.sidebar.radio("Go to", ("Dashboard 1", "Dashboard 2"))

    if selected_dashboard == "Dashboard 1":
        dashboard1()
    elif selected_dashboard == "Dashboard 2":
        dashboard2()

if __name__ == "__main__":
    main()
