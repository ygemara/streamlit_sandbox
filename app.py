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

# Read the Google Sheets URL from Streamlit secrets
sheet_url = st.secrets["private_gsheets_url"]  # Ensure this secret is set in Streamlit secrets
sheet = client.open_by_url(sheet_url)
worksheet = sheet.worksheet("Sheet1")  # Access the first sheet by name

# Define additional data as a dictionary
additional_data = {
    'col 1': ['New Data 1', 'New Data 2', 'New Data 3'],
    'col 2': ['More Data 1', 'More Data 2', 'More Data 3'],
    'col 3': ['Extra Data 1', 'Extra Data 2', 'Extra Data 3'],
    'col 4': ['Additional Data 1', 'Additional Data 2', 'Additional Data 3'],
    'col 5': ['Further Data 1', 'Further Data 2', 'Further Data 3']
}

# Read existing data from the sheet
existing_data = worksheet.get_all_values()

# Combine existing data with additional data (assuming headers are already present)
data = existing_data + [list(v) for v in additional_data.values()]  # Convert dict values to lists

# Clear existing content before updating (optional)
worksheet.clear() 

# Update the worksheet with the combined data
worksheet.update(data)

# Display success message
st.success('Data has been written to Google Sheets')
