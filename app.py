import streamlit as st
import pandas as pd #if you will
import gspread
from google.oauth2 import service_account

# Create a connection object.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive"
    ],
)
conn = connect(credentials=credentials)
client=gspread.authorize(credentials)

sheet_id = '18jiBJagQ2ybfeTt4rUBnbuqZXPYjqaGz7KSSSjMvDis'
csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
database_df = pd.read_csv(csv_url, on_bad_lines='skip')
st.write(database_df)
# database_df = database_df.astype(str)
# sheet_url = st.secrets["private_gsheets_url"] #this information should be included in streamlit secret
# sheet = client.open_by_url(sheet_url).sheet1
# sheet.update([database_df.columns.values.tolist()] + database_df.values.tolist())
# st.success('Data has been written to Google Sheets')
