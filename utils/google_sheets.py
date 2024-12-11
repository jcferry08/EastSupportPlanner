import gspread
from google.oauth2.service_account import Credentials

def get_google_sheet(sheet_name):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]

    credentials = Credentials.from_service_account_file(
        "credentials/credentials.json", scopes=scope
    )

    gc = gspread.authorize(credentials)

    sheet = gc.open(sheet_name)

    return sheet