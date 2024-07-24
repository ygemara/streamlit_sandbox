import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
creds_dict = st.secrets["gsheets"]
# Define the scope

if isinstance(creds_dict["private_key"], str):
    creds_dict["private_key"] = creds_dict["private_key"].replace("\\n", "\n")

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)

# Authorize the clientsheet 
client = gspread.authorize(creds)
