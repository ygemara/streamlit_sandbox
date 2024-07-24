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

def write_to_gcs(data):
  """Writes data to a GCS bucket."""

  bucket = storage_client.bucket(bucket_name)
  blob = bucket.blob("your_file_name.txt")  # Replace with desired file name

  # Convert data to a string if necessary
  data_str = str(data)

  blob.upload_from_string(data_str)

  st.success("Data written to GCS successfully!")

def main():
  # Example data
  data = {"message": "Hello from Streamlit to GCP!"}

  if st.button("Write to GCS"):
    write_to_gcs(data)

if __name__ == "__main__":
  main()
