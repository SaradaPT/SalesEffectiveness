import streamlit as st
import mysql.connector
import pandas as pd

# MySQL Connection
def get_data():
    conn = mysql.connector.connect(
        host="18.136.157.135",
        user="dm_team2",
        password="DM!$Team&27@9!20!",
        database="project_sales"
    )
    query = "SELECT * FROM data;"  # Modify as per your table
    data = pd.read_sql(query, conn)
    conn.close()
    return data

# Streamlit UI
st.title("📊 Sales Effectiveness Analysis")

# Fetch and display data
data = get_data()
st.write(data.head())

# Visualization
if "Status" in data.columns:
    st.bar_chart(data["Status"].value_counts())
else:
    st.error("⚠️ Column 'Status' not found in the database! Check column names above.")

