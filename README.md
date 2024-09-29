# Bangkit_2024_Dicoding
# Bike Usage Analysis Dashboard
This project provides an interactive dashboard built with Streamlit to analyze bike usage data. The dashboard allows users to explore how various factors such as temperature, humidity, weather conditions, and the day of the week influence bike usage.

# https://bike-sharing-dashboard-dicoding-2024.streamlit.app/

# 1. File Structure

```plaintext
.
├── dashboard.py
├── data
|   ├── Readme.txt
│   ├── df_day_analisis.csv
│   └── df_hour_analisis.csv
├── screenshots
│   ├── Screenshots 1.png
│   ├── Screenshots 2.png
│   ├── Screenshots 3.png
│   ├── Screenshots 4.png
│   └── Screenshots 5.png
├── README.md
└── requirements.txt
```
2. Steps to Build and Run the Project
1. Data Preparation:
- Collecting Data: We use two datasets, one containing hourly data and another with daily data about bike usage. The datasets include variables like temperature, humidity, weather conditions, and the number of registered and casual users.
- Data Cleaning: The data is processed to handle missing values, remove irrelevant columns, and ensure the proper data types for each variable.

2. Exploratory Data Analysis (EDA):
Business Questions:
- What are the main factors influencing bike usage at different times?
- How does bike usage vary between weekdays and weekends?
Visualizing Trends: The data is explored to observe patterns in usage trends across different factors like weather conditions, day of the week, and time of day.

3. Visualization in Streamlit:
- Filtering Data: The dashboard provides filters to select specific factors (e.g., temperature, humidity) for hourly analysis.
- Plotting Results: Line charts and bar charts visualize the trends and help provide answers to the business questions.
- Insights: The analysis provides actionable insights, such as the impact of weather and day of the week on bike usage patterns.

4. Dashboard Features
- Main Factors Influencing Bike Usage
Visualize how temperature, humidity, and other factors affect bike usage across different hours.
- Weekday vs Weekend Usage
Analyze and compare bike usage on weekdays versus weekends with bar charts that highlight the average usage differences.
- Additional Weather Analysis
See how weather conditions impact the total number of bike rentals.

5. Screenshots
a. Main Factors Influencing Bike Usage at Different Times
![image](https://github.com/user-attachments/assets/fa8db8b8-4fe1-46de-b79c-6e1406225ec0)

b. Variation in Bike Usage Patterns Between Weekdays and Weekends
![image](https://github.com/user-attachments/assets/ed8598f1-2b00-4d15-85b8-ca568632bd2f)

c.Additional Analysis: Usage by Weather Conditions
![image](https://github.com/user-attachments/assets/46a99a95-d7ae-4d2f-b666-d3a9230174d1)
