import streamlit as st
import pandas as pd
from utils.google_sheets import get_google_sheet

def manage_projects_tab():

    sheet = get_google_sheet("Team Project Tracker")
    worksheet = sheet.worksheet("Projects")
    projects_data = pd.DataFrame(worksheet.get_all_records())

    st.write("### Current Projects")
    if not projects_data.empty:
        st.dataframe(projects_data)
    else:
        st.write("No projects found.")

    st.write("### Add New Project")
    with st.form("add_project_form", clear_on_submit=True):
        project_name = st.text_input("Project Name")
        total_budget = st.number_input("Total Budget", min_value=0.0)
        start_date = st.date_input("Start Date")
        end_date = st.date_input("End Date")

        submitted = st.form_submit_button("Add Project")

        if submitted:
            new_project_id = f"P{len(projects_data) + 1:03}"

            new_project = [
                new_project_id,
                project_name,
                total_budget,
                0.0,
                "",
                start_date.strftime("%Y-%m-%d"),
                end_date.strftime("%Y-%m-%d"),
                ""
            ]
        
            worksheet.append_row(new_project)
            st.success(f"Project '{project_name} added successfully!")
            st.rerun()