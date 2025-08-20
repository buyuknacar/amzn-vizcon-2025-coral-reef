import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

@st.cache_data
def load_bleaching_data():
    return pd.read_csv("data/coral_bleaching_cleaned.csv", low_memory=False)

@st.cache_data
def load_recovery_data():
    return pd.read_csv("data/coral_recovery_cleaned.csv", low_memory=False)

@st.cache_data
def load_clustered_data():
    return pd.read_csv("data/clustered_data.csv", low_memory=False)

@st.cache_data
def load_correlation_matrix():
    return pd.read_csv("data/correlation_matrix.csv", index_col=0, low_memory=False)

@st.cache_data
def load_elbow_results():
    return pd.read_csv("data/elbow_results.csv", low_memory=False)



# Visualization 1 - Coral Bleaching Over The Years
def create_bleaching_heatmap():
    """Create coral bleaching intensity heatmap visualization"""
    bleaching_df = load_bleaching_data()
    bleaching_filtered = bleaching_df[
        (bleaching_df['date_year'].notnull()) & (bleaching_df['date_year'] >= 2000) & 
        (bleaching_df['date_year'] <= 2019) & (bleaching_df['latitude_degrees'].notnull()) & 
        (bleaching_df['longitude_degrees'].notnull()) & (bleaching_df['country_name'].notnull()) &
        (bleaching_df['percent_bleaching'].notnull())
    ].copy()
    
    bleaching_filtered['date_year'] = bleaching_filtered['date_year'].astype(int)
    bleaching_filtered = bleaching_filtered.sort_values(by='date_year')
    
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
    return fig

# Visualization 2 - Coral Recovery Over the Years
def create_recovery_heatmap():
    """Create coral recovery intensity heatmap visualization"""
    recovery_df = load_recovery_data()
    recovery_filtered = recovery_df[
        (recovery_df['date_year'].notnull()) & (recovery_df['date_year'] >= 2000) & 
        (recovery_df['date_year'] <= 2019) & (recovery_df['latitude_degrees'].notnull()) & 
        (recovery_df['longitude_degrees'].notnull()) & (recovery_df['country_name'].notnull()) &
        (recovery_df['percent_hard_coral_cover'].notnull())
    ].copy()
    
    recovery_filtered['date_year'] = recovery_filtered['date_year'].astype(int)
    recovery_filtered = recovery_filtered.sort_values(by='date_year')
    
    fig = px.density_mapbox(
        recovery_filtered,
        lat='latitude_degrees',
        lon='longitude_degrees',
        z='percent_hard_coral_cover',
        radius=20,
        animation_frame='date_year',
        color_continuous_scale='Greens',
        range_color=[0, recovery_filtered['percent_hard_coral_cover'].max()],
        mapbox_style='open-street-map',
        center=dict(lat=0, lon=0),
        zoom=0.4,
        height=700,
        title='Coral Recovery Intensity Heatmap',
        hover_name='country_name',
        hover_data={'percent_hard_coral_cover': True, 'date_year': True}
    )
    
    fig.update_layout(coloraxis_colorbar=dict(title="Percent Hard Coral Cover"))
    return fig

def create_kmeans_analysis():
    """Create K-means analysis visualizations"""
    dfC = load_clustered_data()
    correlation_matrix = load_correlation_matrix()
    elbow_df = load_elbow_results()
    
    # Geographic distribution of clusters
    fig1 = px.scatter(
        dfC,
        x="Longitude_Degrees",
        y="Latitude_Degrees",
        color="Cluster",
        color_continuous_scale="viridis",
        title="Geographic Distribution of Clusters",
        labels={"Longitude_Degrees": "Longitude", "Latitude_Degrees": "Latitude"},
        height=500
    )
    
    # Correlation matrix heatmap
    fig2 = px.imshow(
        correlation_matrix,
        text_auto=True,
        color_continuous_scale="RdBu_r",
        title="Correlation Matrix of Coral Features",
        height=600
    )
    
    # Elbow method plot
    fig3 = px.line(
        elbow_df,
        x="k",
        y="inertia",
        markers=True,
        title="Elbow Method For Optimal k",
        labels={"k": "Number of Clusters (k)", "inertia": "Inertia"},
        height=400
    )
    
    # Donut chart for factor influence
    features = ['Geographic Location', 'Macroalgal Competition', 'Temperature Factors', 
               'Depth', 'Other Environmental Factors']
    sizes = [27.5, 27, 20, 17, 7]
    colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF99CC']
    
    fig4 = go.Figure(data=[go.Pie(
        labels=features,
        values=sizes,
        hole=0.7,
        marker_colors=colors,
        textinfo='label+percent',
        textposition='outside'
    )])
    
    fig4.update_layout(
        title="Influence of Different Factors on Coral Recovery",
        height=500,
        showlegend=True
    )
    
    return fig1, fig2, fig3, fig4


