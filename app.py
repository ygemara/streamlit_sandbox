import streamlit as st
import pandas as pd
from google.cloud import storage
from st_files_connection import FilesConnection
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from streamlit_gsheets import GSheetsConnection

st.write("hello world")
# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
