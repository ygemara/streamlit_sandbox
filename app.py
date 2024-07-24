import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

# Load credentials from secrets
creds_dict = st.secrets["connections.gsheets"]
creds_json = json.dumps(creds_dict)

# Define the scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_dict(json.loads(creds_json), scope)
