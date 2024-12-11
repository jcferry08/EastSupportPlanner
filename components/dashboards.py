import streamlit as st
from components.projects import manage_projects_tab

def admin_dashboard():
    st.title("Admin Dashboard")
    tabs = st.tabs(["Projects", "Tasks", "Expenses", "User Management", "Profile"])

    with tabs[0]:
        manage_projects_tab()

    with tabs[1]:
        st.subheader("Manage Tasks")
        st.button("Create New Task")
    
    with tabs[2]:
        st.subheader("Manage Expenses")
        st.button("Log Expense")
    
    with tabs[3]:
        st.subheader("User Management")
        st.button("Add New User")
        st.button("Remove User")

    with tabs[4]:
        st.subheader("Profile Settings")
        st.button("Change Password")
    
def manager_dashboard():
    st.title("Manager Dashboard")
    tabs = st.tabs(["Projects", "Tasks", "Expenses", "Profile"])

    with tabs[0]:
        st.subheader("Manage Projects")
        st.button("Create New Project")

    with tabs[1]:
        st.subheader("Manage Tasks")
        st.button("Create New Task")
    
    with tabs[2]:
        st.subheader("Manage Expenses")
        st.button("Log Expense")

    with tabs[3]:
        st.subheader("Profile Settings")
        st.button("Change Password")

def user_dashboard():
    st.title("Manager Dashboard")
    tabs = st.tabs(["Projects", "Tasks", "Expenses", "Profile"])

    with tabs[0]:
        st.subheader("Current Projects")
        st.write("View all current Projects.")

    with tabs[1]:
        st.subheader("Manage Tasks")
        st.button("Create New Task")
    
    with tabs[2]:
        st.subheader("Manage Expenses")
        st.button("Log Expense")

    with tabs[3]:
        st.subheader("Profile Settings")
        st.button("Change Password")