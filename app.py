import streamlit as st
import pandas as pd
import gspread
from google.oauth2 import service_account

# Create a connection object using credentials from Streamlit secrets.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ],
)

# Authorize the client using the credentials
client = gspread.authorize(credentials)

# Define the Google Sheet ID and URL for the CSV export
sheet_id = '18jiBJagQ2ybfeTt4rUBnbuqZXPYjqaGz7KSSSjMvDis'
csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

# Read the CSV data into a DataFrame
database_df = pd.read_csv(csv_url, on_bad_lines='skip')

# Display the DataFrame in the Streamlit app
st.write(database_df)

# Read the Google Sheets URL from Streamlit secrets
sheet_url = st.secrets["private_gsheets_url"]  # Ensure this secret is set in Streamlit secrets
sheet = client.open_by_url(sheet_url)
worksheet = sheet.worksheet("Sheet1")  # Access the first sheet by name
worksheet.update([database_df.columns.values.tolist()] + database_df.values.tolist())
st.success('Data has been written to Google Sheets')
