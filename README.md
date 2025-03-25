# Data Analyst Assessment - Booking Data Analysis

## 📌 Project Overview
This project focuses on analyzing booking data for a multi-service business. The dataset includes class bookings, subscriptions, facility rentals, and event reservations. The analysis is presented in an interactive **Streamlit dashboard** that allows users to explore key insights, trends, and summaries of the booking data.

## 🛠️ Technologies Used
- **Python** (pandas, sqlite3, plotly, streamlit)
- **SQL** (for querying data)
- **Streamlit** (for interactive dashboard)
- **Jupyter Notebook** (for exploratory data analysis)


## 🚀 How to Run the Project

### 1 Install Dependencies
```bash
pip install -r requirements.txt
```

### 2 Run the Streamlit Dashboard
```bash
streamlit run app.py
```

## 📊 Key Features
✅ **Data Cleaning & Processing:**
- Removed duplicates
- Handled missing values
- Standardized date formats
- Filtered out inconsistencies

✅ **Interactive Dashboard:**
- Booking trends visualization (line charts, bar charts)
- SQL query execution
- Downloadable cleaned dataset

✅ **Customizable Filters:**
- Dropdown selection for booking type
- Dynamic SQL query execution

## 📌 Sample Queries
You can execute SQL queries directly in the Streamlit dashboard. Example:
```sql
SELECT "Booking Type", COUNT(*) as Total_Bookings
FROM bookings
GROUP BY "Booking Type"
ORDER BY Total_Bookings DESC;
```




