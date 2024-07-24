import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
# Define the scope

creds_dict = dict(st.secrets["gsheets"])

# Ensure private key has correct line breaks
creds_dict["private_key"] = creds_dict["private_key"].replace("\\n", "\n")

# Define the scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)

# Authorize the clientsheet 
client = gspread.authorize(creds)
