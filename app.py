import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

# Read data from the Google Sheet.
df = conn.read()

# Display the data in Streamlit.
st.write(df)

# Append a new row (example data)
new_row = ["value1", "value2", "value3"]

# Function to append data to Google Sheet
def append_to_gsheet(connection, values):
    # Access the sheet object through the connection
    sheet = connection.sheet  # Assuming connection has a sheet object
    sheet.append_row(values)  # Append the row to the sheet

# Button to trigger the append function
if st.button('Append new row'):
    append_to_gsheet(conn, new_row)
    st.success("Data appended successfully!")
