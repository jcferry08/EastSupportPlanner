import pandas as pd
import bcrypt
from utils.google_sheets import get_google_sheet

def authenticate_user(username, password, sheet_name):
    """Authenticate a user by username and password."""
    sheet = get_google_sheet(sheet_name)
    worksheet = sheet.get_worksheet(0)
    data = worksheet.get_all_records()
    credentials_df = pd.DataFrame(data)

    user_row = credentials_df[credentials_df["Username"] == username]
    if user_row.empty:
        return False, None
    user_data = user_row.iloc[0]
    hashed_password = user_data["Password"]

    if bcrypt.checkpw(password.encode(), hashed_password.encode()):
        return True, user_data
    else:
        return False, None