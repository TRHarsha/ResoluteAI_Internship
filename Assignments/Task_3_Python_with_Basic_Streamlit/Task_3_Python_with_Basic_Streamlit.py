import pandas as pd
import streamlit as st
from datetime import datetime

# Load the data
uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    
    # Convert date and time columns to string before combining
    df['date'] = df['date'].astype(str)
    df['time'] = df['time'].astype(str)
    
    # Create a datetime column
    df['datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'])

    st.write("## Raw Data")
    st.write(df)

    # Task 1: Datewise total duration for each inside and outside
    df['activity_duration'] = df.groupby('activity')['datetime'].diff().dt.total_seconds()
    datewise_duration = df.groupby(['date', 'position'])['activity_duration'].sum().unstack().fillna(0)

    st.write("## Datewise Total Duration for Each Inside and Outside")
    st.write(datewise_duration)

    # Task 2: Datewise number of picking and placing activity done
    datewise_activity_count = df.groupby(['date', 'activity']).size().unstack().fillna(0)

    st.write("## Datewise Number of Picking and Placing Activity Done")
    st.write(datewise_activity_count)
