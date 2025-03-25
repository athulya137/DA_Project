#!/usr/bin/env python
# coding: utf-8

# In[35]:


import warnings
warnings.filterwarnings('ignore')


# In[56]:


import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# Load Data
file_path = "DataAnalyst_Assesment_Dataset.xlsx"
df = pd.read_excel(file_path)

# Data Cleaning
df.drop_duplicates(inplace=True)
df.fillna("Unknown", inplace=True)
df['Booking Date'] = pd.to_datetime(df['Booking Date'], errors='coerce')

# Create SQLite Database
conn = sqlite3.connect(":memory:")
df.to_sql("bookings", conn, index=False, if_exists="replace")

# Streamlit UI
st.title("📊 Booking Data Analysis Dashboard")

# Dropdown Filter for Booking Type
booking_types = st.selectbox("Select Booking Type", df["Booking Type"].unique())

# Query for Selected Booking Type
query1 = f"""
    SELECT "Booking Type", COUNT(*) as Total_Bookings 
    FROM bookings 
    WHERE "Booking Type" = '{booking_types}'
    GROUP BY "Booking Type"
    ORDER BY Total_Bookings DESC;
"""
bookings_by_type = pd.read_sql(query1, conn)
st.subheader("📌 Total Bookings by Type")
st.dataframe(bookings_by_type)

# Monthly Trend Visualization
st.subheader("📈 Monthly Booking Trends")
df["Month"] = df["Booking Date"].dt.strftime("%Y-%m")
monthly_trend = df.groupby("Month").size().reset_index(name="Count")
fig = px.line(monthly_trend, x="Month", y="Count", title="Monthly Booking Trends")
st.plotly_chart(fig)

# Dynamic SQL Query Input
st.subheader("📝 SQL Query Executor")
query_input = st.text_area("Enter your SQL Query", "SELECT * FROM bookings LIMIT 5")
if st.button("Run Query"):
    result = pd.read_sql(query_input, conn)
    st.dataframe(result)

# Download Cleaned Data
st.subheader("📥 Download Cleaned Data")
csv = df.to_csv(index=False).encode('utf-8')
st.download_button("Download CSV", csv, "cleaned_data.csv", "text/csv")


# In[ ]:





# In[ ]:




