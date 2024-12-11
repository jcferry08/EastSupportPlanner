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
    
    col1, col2, col3 = st.columns(3)

    with col1:
        with st.expander ("Add New Project"):
            with st.form("add_project_form", clear_on_submit=True):
                project_name = st.text_input("Project Name")
                total_budget = st.number_input("Total Budget", min_value=0.0)
                start_date = st.date_input("Start Date")
                end_date = st.date_input("End Date")
                description = st.text_input("Project Description")
            
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
                        "",
                        description
                    ]
                    try:
                        worksheet.append_row(new_project)
                        st.success(f"Project '{project_name}' added successfully!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Failed to add project: {e}")

    with col2:
        with st.expander("Edit Existing Project"):
            selected_project_id = st.selectbox(
                "Select Project ID to Edit", options=projects_data["Project ID"].tolist()
            )
            if selected_project_id:
                selected_project = projects_data[projects_data["Project ID"] == selected_project_id].iloc[0]
                with st.form("edit_project_form", clear_on_submit=True):
                    project_name = st.text_input(
                        "Project Name", value=selected_project["Project Name"]
                    )
                    total_budget = st.number_input(
                        "Total Budget", value=float(selected_project["Total Budget"]), step=100.0
                    )
                    start_date = st.date_input(
                        "Start Date", value=pd.to_datetime(selected_project["Start Date"])
                    )
                    end_date = st.date_input(
                        "End Date", value=pd.to_datetime(selected_project["End Date"])
                    )
                    description = st.text_input(
                        "Descripton", value=selected_project["Description"]
                    )

                    submitted = st.form_submit_button("Save Changes")
                    if submitted:
                        updated_project = [
                            selected_project["Project ID"],
                            project_name,
                            total_budget,
                            selected_project["Total Expenses"],
                            selected_project["ROI"],
                            start_date.strftime("%Y-%m-%d"),
                            end_date.strftime("%Y-%m-%d"),
                            selected_project["Assigned Users"],
                            description
                        ]
                        row_index = selected_project.name + 2
                        try:
                            worksheet.update(f"A{row_index}:H{row_index}", [updated_project])
                            st.success(f"Project '{project_name}' updated successfully!")
                            st.rerun
                        except Exception as e:
                            st.error(f"Failed to update project: {e}")