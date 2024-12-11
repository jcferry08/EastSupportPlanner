import streamlit as st
from components.login import authenticate_user
from components.dashboards import admin_dashboard, manager_dashboard, user_dashboard
from utils.google_sheets import get_google_sheet


SHEET_NAME = "Team Project Tracker"

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
    st.session_state["user"] = None

if not st.session_state["logged_in"]:
    st.sidebar.title("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    login_button = st.sidebar.button("Login")

    if login_button:
        success, user = authenticate_user(username, password, SHEET_NAME)
        if success:
            st.session_state["logged_in"] = True
            st.session_state["user"] = user
            st.sidebar.success(f"Welcome, {user['Full Name']}")
            st.rerun()
        else:
            st.sidebar.error("Invalid username or password.")
else:
    user = st.session_state["user"]
    st.sidebar.success(f"Logged in as {user['Full Name']} ({user['Role']})")
    if st.sidebar.button("Logout"):
        st.session_state["logged_in"] = False
        st.session_state["user"] = None
        st.rerun()

if st.session_state["logged_in"]:
    role = user["Role"]

    if role == "Admin":
        admin_dashboard()
    elif role == "Manager":
        manager_dashboard()
    else:
        user_dashboard()