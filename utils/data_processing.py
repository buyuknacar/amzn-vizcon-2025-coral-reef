import pandas as pd
import streamlit as st

@st.cache_data
def load_bleaching_data():
    """Load and clean bleaching data"""
    bleaching_df = pd.read_csv("data/coral_bleaching.csv")
    bleaching_df.columns = bleaching_df.columns.str.strip().str.lower().str.replace(" ", "_")
    
    # Convert to numeric
    bleaching_df['date_year'] = pd.to_numeric(bleaching_df['date_year'], errors='coerce')
    bleaching_df['percent_bleaching'] = pd.to_numeric(bleaching_df['percent_bleaching'], errors='coerce')
    
    return bleaching_df

def filter_bleaching_data(df, start_year=2000, end_year=2019):
    """Filter bleaching data for valid records"""
    filtered = df[
        (df['date_year'].notnull()) & 
        (df['date_year'] >= start_year) & 
        (df['date_year'] <= end_year) &
        (df['latitude_degrees'].notnull()) & 
        (df['longitude_degrees'].notnull()) & 
        (df['country_name'].notnull()) &
        (df['percent_bleaching'].notnull())
    ].copy()
    
    filtered['date_year'] = filtered['date_year'].astype(int)
    return filtered.sort_values(by='date_year')