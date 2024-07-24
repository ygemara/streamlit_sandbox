import streamlit as st
import pandas as pd
from google.cloud import storage

st.write("Hello World")
# Replace with your GCP project ID and bucket name
project_id = "applied-groove-420014"
bucket_name = "streamlit_bucket_yg"

# # Assuming you're using Streamlit secrets to store the key
# def get_credentials():
#     import os
#     from google.oauth2 import service_account

#     key_dict = st.secrets["gcp_credentials"]
#     credentials = service_account.Credentials.from_service_account_info(key_dict)
#     return credentials

# # Get credentials
# creds = get_credentials()

import streamlit as st
from st_files_connection import FilesConnection

# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.
conn = st.connection('gcs', type=FilesConnection)
df = conn.read("streamlit-bucket/myfile.csv", input_format="csv", ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.Owner} has a :{row.Pet}:")

