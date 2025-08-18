import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
@st.cache_data
def load_data():
    bleaching_df = pd.read_csv("data/coral_bleaching.csv")
    bleaching_df.columns = bleaching_df.columns.str.strip().str.lower().str.replace(" ", "_")
    return bleaching_df

st.title("🐠 Coral Reef Bleaching and Recovery Visualization")

# Load data
bleaching_df = load_data()

# Convert to numeric first
bleaching_df['date_year'] = pd.to_numeric(bleaching_df['date_year'], errors='coerce')
bleaching_df['percent_bleaching'] = pd.to_numeric(bleaching_df['percent_bleaching'], errors='coerce')

# Filter data
bleaching_filtered = bleaching_df[
    (bleaching_df['date_year'].notnull()) & 
    (bleaching_df['date_year'] >= 2000) & 
    (bleaching_df['date_year'] <= 2019) &
    (bleaching_df['latitude_degrees'].notnull()) & 
    (bleaching_df['longitude_degrees'].notnull()) & 
    (bleaching_df['country_name'].notnull()) &
    (bleaching_df['percent_bleaching'].notnull())
].copy()

bleaching_filtered['date_year'] = bleaching_filtered['date_year'].astype(int)
bleaching_filtered = bleaching_filtered.sort_values(by='date_year')

# Create heatmap
fig = px.density_mapbox(
    bleaching_filtered,
    lat='latitude_degrees',
    lon='longitude_degrees',
    z='percent_bleaching',
    radius=20,
    animation_frame='date_year',
    color_continuous_scale='YlOrRd',
    range_color=[0, bleaching_filtered['percent_bleaching'].max()],
    mapbox_style='open-street-map',
    center=dict(lat=0, lon=0),
    zoom=0.4,
    height=700,
    title='Coral Bleaching Intensity Heatmap',
    hover_name='country_name',
    hover_data={'percent_bleaching': True, 'date_year': True}
)

fig.update_layout(coloraxis_colorbar=dict(title="Percent Bleaching"))

st.plotly_chart(fig, use_container_width=True)