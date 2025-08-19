import pandas as pd
import streamlit as st

@st.cache_data
def load_bleaching_data():
    """Load and clean bleaching data"""
    bleaching_df = pd.read_csv("data/coral_bleaching.csv", low_memory=False)
    bleaching_df.columns = bleaching_df.columns.str.strip().str.lower().str.replace(" ", "_")
    
    # Convert to numeric
    bleaching_df['date_year'] = pd.to_numeric(bleaching_df['date_year'], errors='coerce')
    bleaching_df['percent_bleaching'] = pd.to_numeric(bleaching_df['percent_bleaching'], errors='coerce')
    
    return bleaching_df
