import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()

# Print results.
for row in df.itertuples():
    st.write("Hello")
