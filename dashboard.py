import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Apply minimalist design with a light blue theme using Streamlit's config and CSS
st.set_page_config(page_title="Bike Usage Analysis Dashboard", layout="wide")

# Custom CSS for a light blue minimalist design
st.markdown("""
    <style>
    /* Center and minimize the width of the dashboard */
    .block-container {
        max-width: 800px;
        margin: auto;
        padding-top: 20px;
    }
    /* Light blue theme for headers and text */
    h1, h2, h3, h4, h5, h6, p {
        color: #87CEFA; /* Light blue color */
    }
    /* Adjust table and charts to have a minimalist look */
    .stDataFrame, .stChart {
        background-color: #E0F7FA;
        border-radius: 8px;
    }
    /* Light blue buttons */
    .stButton button {
        background-color: #87CEFA;
        color: white;
        border-radius: 5px;
    }
    /* Minimal padding for checkboxes */
    .stCheckbox {
        margin-bottom: 15px;
    }
    /* Set all text alignment to horizontal */
    h1, h2, h3, h4, h5, h6, p {
        text-align: left;
    }
    </style>
    """, unsafe_allow_html=True)

# Load the datasets (replace with actual paths if needed)
df_day = pd.read_csv('df_day_analisis.csv')
df_hour = pd.read_csv('df_hour_analisis.csv')

# Set the title for the dashboard
st.title("🚴‍♂️ Bike Usage Analysis Dashboard")

# Section 1: Main Factors Influencing Bike Usage at Different Times
st.header("1. Main Factors Influencing Bike Usage at Different Times")

# Introduction to this section
st.write("""
In this section, we explore how factors like temperature, humidity, and time of day affect bike usage.
The data is presented on an hourly basis to understand how these factors impact the number of casual and registered users.
""")

# Select features for analysis
selected_factors = st.multiselect(
    "Select factors to analyze (e.g., Temperature, Humidity, etc.):",
    ['temp', 'humidity', 'windspeed', 'total'],
    default=['temp', 'humidity', 'total']
)

# Group hourly data by the selected factors and plot
st.subheader("Hourly Bike Usage by Selected Factors")
if selected_factors:
    # Group data by hour and calculate the mean for selected factors
    grouped_hourly = df_hour[['hour'] + selected_factors].groupby('hour').mean()

    # Plot the data
    st.line_chart(grouped_hourly)

    # Provide an interpretation of the results
    st.write("""
    The line chart above shows the variation in bike usage across different hours of the day, along with the selected factors.
    Higher bike usage may correspond to specific temperatures or humidity levels, showing clear patterns throughout the day.
    """)

# Optional: Display raw data
if st.checkbox("Show raw hourly data"):
    st.write(df_hour)

# Section 2: Variation in Bike Usage Patterns Between Weekdays and Weekends
st.header("2. Variation in Bike Usage Patterns Between Weekdays and Weekends")

# Introduction to this section
st.write("""
This section analyzes how bike usage patterns vary between weekdays and weekends. By comparing the total usage on workdays vs weekends,
we can see if people tend to use bikes more during leisure time or commuting periods.
""")

# Create a new column to differentiate weekdays from weekends
df_day['is_weekend'] = df_day['weekday'].apply(lambda x: 1 if x in ['Sat', 'Sun'] else 0)

# Group data by weekdays (is_weekend) and calculate average total bike usage
usage_by_day_type = df_day.groupby('is_weekend')['total'].mean()

# Plot weekday vs weekend usage
st.subheader("Average Bike Usage: Weekdays vs Weekends")
st.bar_chart(usage_by_day_type)

# Add insights based on the analysis
st.write("""
From the bar chart, we can observe the difference in bike usage between weekdays and weekends. 
Generally, weekends may see higher casual usage due to leisure activities, while weekdays may show increased usage due to commuting.
""")

# Optional: Display raw data for daily analysis
if st.checkbox("Show raw daily data"):
    st.write(df_day)

# Section 3: Additional Analysis - Usage by Weather Conditions
st.header("3. Additional Analysis: Usage by Weather Conditions")

# Group data by weather situation to see how different weather conditions affect bike usage
st.write("""
Bike usage can also be affected by weather conditions. Below is an analysis of bike usage based on different weather situations (e.g., clear, misty, cloudy).
""")

# Group by weather condition
weather_usage = df_day.groupby('weather_situation')['total'].mean()

# Plot usage by weather conditions
st.bar_chart(weather_usage)

# Conclusion section
st.header("Conclusion")
st.write("""
From this dashboard, we can conclude that both environmental factors like temperature, humidity, and time of day, 
as well as situational factors like the type of day (weekday vs weekend) and weather, significantly influence bike usage patterns.
Understanding these trends can help in optimizing bike-sharing services or urban planning for better cycling infrastructure.
""")
