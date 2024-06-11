import streamlit as st
import mysql.connector

# MySQL connection details
db_config = {
    'user': 'root',
    'password': '',  # Set the correct password if needed
    'host': '127.0.0.1',
    'database': 'maskdetect',
    'port': 3307,  # Ensure this matches your MySQL server port
    'connection_timeout': 2000
}

def connect_db():
    """Create a connection to the MySQL database."""
    return mysql.connector.connect(**db_config)

def fetch_data_from_db():
    """Fetch data from the mask_detection table."""
    conn = connect_db()
    cursor = conn.cursor()
    query = "SELECT image, result FROM mask_detection"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

def show_welcome_page():
    st.title('Welcome Page')

    # Fetch data from the database
    data = fetch_data_from_db()

    if data:
        for image_data, result in data:
            st.image(image_data, caption=f'Result: {result}', use_column_width=True)
    else:
        st.write("No data found.")

# Uncomment below if you want to run this as a standalone script
# if __name__ == "__main__":
#     show_welcome_page()
