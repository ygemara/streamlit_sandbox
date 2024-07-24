import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

# Read data from the Google Sheet.
df = conn.read()

# Display the data in Streamlit.
st.write(df)

# Function to append data to Google Sheet
def append_to_gsheet(values):
    # Assuming the connection object has a method to append data
    conn.append_row(values)

# Append a new row (example data)
new_row = ["value1", "value2", "value3"]

# Button to trigger the append function
if st.button('Append new row'):
    append_to_gsheet(new_row)
    st.success("Data appended successfully!")
