import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('path_to_your_credentials.json', scope)

# Authorize the clientsheet 
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open("Your Sheet Name").sheet1

# Function to append data to Google Sheet
def append_to_gsheet(values):
    sheet.append_row(values)

# Read data from the Google Sheet
data = sheet.get_all_records()

# Display the data in Streamlit
st.write(data)

# Append a new row (example data)
new_row = ["value1", "value2", "value3"]
append_to_gsheet(new_row)

st.success("Data appended successfully!")
