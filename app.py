import streamlit as st
import plotly.express as px
from utils.data_processing import load_bleaching_data, filter_bleaching_data

st.title("🐠 Coral Reef Bleaching and Recovery Visualization")

# Load and filter data
bleaching_df = load_bleaching_data()
bleaching_filtered = filter_bleaching_data(bleaching_df)

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