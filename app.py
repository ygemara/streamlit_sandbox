import streamlit as st
from google.cloud import storage
st.write("Hello World")
# Replace with your GCP project ID and bucket name
project_id = "applied-groove-420014"
bucket_name = "streamlit_bucket_yg"

# Assuming you're using Streamlit secrets to store the key
def get_credentials():
    import os
    from google.oauth2 import service_account

    key_dict = st.secrets["gcp_credentials"]
    credentials = service_account.Credentials.from_service_account_info(key_dict)
    return credentials

# Get credentials
creds = get_credentials()

# Create a storage client
storage_client = storage.Client(project=project_id, credentials=creds)
