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
    ]
)

# Authorize the client using the credentials
client = gspread.authorize(credentials)

# Define the Google Sheet ID and URL for the CSV export
sheet_id = st.secrets["sheet_id"]
csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

# Read the CSV data into a DataFrame
database_df = pd.read_csv(csv_url, on_bad_lines='skip')

# Add additional rows to the DataFrame
additional_data = {
    'col 1': ['New Data 1', 'New Data 2', 'New Data 3'],
    'col 2': ['More Data 1', 'More Data 2', 'More Data 3'],
    'col 3': ['Extra Data 1', 'Extra Data 2', 'Extra Data 3'],
    'col 4': ['Additional Data 1', 'Additional Data 2', 'Additional Data 3'],
    'col 5': ['Further Data 1', 'Further Data 2', 'Further Data 3']
}
additional_df = pd.DataFrame(additional_data)

# Concatenate the original DataFrame with the additional rows
database_df = pd.concat([database_df, additional_df], ignore_index=True)

# Display the updated DataFrame in the Streamlit app
st.write(database_df)

# Read the Google Sheets URL from Streamlit secrets
sheet_url = st.secrets["private_gsheets_url"]  # Ensure this secret is set in Streamlit secrets
sheet = client.open_by_url(sheet_url)
worksheet = sheet.worksheet("Sheet1")  # Access the first sheet by name

# Verify that the column headers match
google_sheet_headers = worksheet.row_values(1)
dataframe_headers = database_df.columns.tolist()
st.write("hello")
if google_sheet_headers != dataframe_headers:
    st.error("Column headers do not match!")
else:
    # Convert DataFrame to a list of lists for updating Google Sheets
    data = [dataframe_headers] + database_df.values.tolist()

    # Try updating the worksheet with the DataFrame content
    try:
        worksheet.clear()  # Clear existing content before updating
        worksheet.update(data)
        st.success('Data has been written to Google Sheets')
    except Exception as e:
        st.error(f'An error occurred: {e}')
