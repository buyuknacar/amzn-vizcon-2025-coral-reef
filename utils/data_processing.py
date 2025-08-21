import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st
import matplotlib.pyplot as plt

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

@st.cache_data
def load_gbr_historical():
    return pd.read_csv("data/gbr_historical.csv", low_memory=False)

@st.cache_data
def load_gbr_forecast():
    return pd.read_csv("data/gbr_forecast.csv", low_memory=False)



# Visualization 1 - Coral Bleaching Over The Years
def create_bleaching_heatmap():
    """Create coral bleaching intensity heatmap visualization"""
    bleaching_df = load_bleaching_data()
    bleaching_filtered = bleaching_df[
        (bleaching_df['date_year'].notnull()) & 
        (bleaching_df['date_year'] >= 2000) & 
        (bleaching_df['date_year'] <= 2019) &
        (bleaching_df['latitude_degrees'].notnull()) & 
        (bleaching_df['longitude_degrees'].notnull()) & 
        (bleaching_df['country_name'].notnull())
    ].copy()
    
    bleaching_filtered['date_year'] = bleaching_filtered['date_year'].astype(int)
    bleaching_filtered['country_name'] = bleaching_filtered['country_name'].replace('France', 'France (Overseas Territory)')
    
    # Make sure intensity column exists and clean
    bleaching_filtered = bleaching_filtered[bleaching_filtered['percent_bleaching'].notnull()]
    
    # Create custom hover text
    bleaching_filtered['hover_text'] = bleaching_filtered['country_name'] + ' (' + bleaching_filtered['date_year'].astype(str) + ')'
    
    # Sort by date_year ascending
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
        hover_name='hover_text',
        hover_data={
            'hover_text': False,
            'country_name': False,
            'date_year': False,
            'percent_bleaching': False,
            'latitude_degrees': False,
            'longitude_degrees': False
        }
    )
    
    fig.update_layout(coloraxis_colorbar=dict(title="Percent Bleaching"))
    return fig

# Visualization 2 - KMeans Analysis
def create_kmeans_analysis():
    """Create K-means analysis visualization"""
    # Donut chart for factor influence
    features = ['Geographic Location', 'Macroalgal Competition', 'Temperature Factors', 
               'Depth', 'Other Environmental Factors']
    sizes = [27.5, 27, 20, 17, 7]
    colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF99CC']
    
    fig = go.Figure(data=[go.Pie(
        labels=features,
        values=sizes,
        hole=0.7,
        marker_colors=colors,
        textinfo='label+percent',
        textposition='outside'
    )])
    
    fig.update_layout(
        height=500,
        showlegend=True
    )
    
    return fig

# Visualization 3 - Coral Bleaching and Environmental Correlation
def create_bleaching_dashboard():
    """Create comprehensive coral bleaching analysis dashboard"""
    df = load_bleaching_data()
    
    # Clean data
    df['date_year'] = pd.to_datetime(df['date']).dt.year
    numeric_cols = ['percent_bleaching', 'temperature_maximum', 'windspeed', 'turbidity']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    df = df.dropna(subset=['percent_bleaching'])
    
    countries = sorted(df['country_name'].unique())
    
    fig = make_subplots(
        rows=5, cols=1,
        subplot_titles=(
            'Bleaching by Exposure Level',
            'Top 15 Countries by Bleaching Severity',
            'Mean Sea Temperature Over Years',
            'Mean Water Turbidity Over Years',
            'Mean Wind Speed Over Years'
        ),
        specs=[
            [{"type": "bar"}],
            [{"type": "bar"}],
            [{"type": "scatter"}],
            [{"type": "scatter"}],
            [{"type": "scatter"}]
        ],
        vertical_spacing=0.06
    )
    
    # Global data traces
    global_exposure = df.groupby('exposure')['percent_bleaching'].mean().reset_index()
    fig.add_trace(
        go.Bar(
            x=global_exposure['exposure'],
            y=global_exposure['percent_bleaching'],
            name='Global Exposure',
            marker_color='#2E5077',
            visible=True,
            hovertemplate='<b>Exposure Level:</b> %{x}<br><b>Bleaching Percentage:</b> %{y:.2f}%<extra></extra>'
        ),
        row=1, col=1
    )
    
    # Top 15 countries
    country_bleaching = (df.groupby('country_name')['percent_bleaching']
                        .agg(['mean', 'count'])
                        .reset_index()
                        .sort_values('mean', ascending=False))
    top_15 = country_bleaching[country_bleaching['count'] >= 100].head(15)
    
    fig.add_trace(
        go.Bar(
            x=top_15['country_name'],
            y=top_15['mean'],
            name='Top 15 Countries',
            marker_color='#2F4F4F',
            visible=True,
            hovertemplate='<b>Country:</b> %{x}<br><b>Mean Bleaching:</b> %{y:.2f}%<extra></extra>'
        ),
        row=2, col=1
    )
    
    # Global environmental factors
    global_temp = df.groupby('date_year')['temperature_maximum'].mean().reset_index()
    fig.add_trace(
        go.Scatter(
            x=global_temp['date_year'],
            y=global_temp['temperature_maximum'],
            name='Global Temperature',
            line=dict(color='#8B0000'),
            visible=True,
            hovertemplate='<b>Year:</b> %{x}<br><b>Temperature:</b> %{y:.2f}K<extra></extra>'
        ),
        row=3, col=1
    )
    
    global_turb = df.groupby('date_year')['turbidity'].mean().reset_index()
    fig.add_trace(
        go.Scatter(
            x=global_turb['date_year'],
            y=global_turb['turbidity'],
            name='Global Turbidity',
            line=dict(color='#00008B'),
            visible=True,
            hovertemplate='<b>Year:</b> %{x}<br><b>Turbidity:</b> %{y:.2f}<extra></extra>'
        ),
        row=4, col=1
    )
    
    global_wind = df.groupby('date_year')['windspeed'].mean().reset_index()
    fig.add_trace(
        go.Scatter(
            x=global_wind['date_year'],
            y=global_wind['windspeed'],
            name='Global Wind Speed',
            line=dict(color='#006400'),
            visible=True,
            hovertemplate='<b>Year:</b> %{x}<br><b>Wind Speed:</b> %{y:.2f} m/s<extra></extra>'
        ),
        row=5, col=1
    )
    
    # Country-specific traces (initially hidden)
    for country in countries[:20]:  # Limit to first 20 countries for performance
        country_data = df[df['country_name'] == country]
        
        exposure_data = country_data.groupby('exposure')['percent_bleaching'].mean().reset_index()
        fig.add_trace(
            go.Bar(
                x=exposure_data['exposure'],
                y=exposure_data['percent_bleaching'],
                name=f'{country} Exposure',
                marker_color='#2E5077',
                visible=False,
                hovertemplate=f'<b>Country:</b> {country}<br><b>Exposure Level:</b> %{{x}}<br><b>Bleaching Percentage:</b> %{{y:.2f}}%<extra></extra>'
            ),
            row=1, col=1
        )
    
    # Create dropdown for country selection
    buttons = [dict(
        args=[{"visible": [True] * 5 + [False] * (len(fig.data) - 5)}],
        label="All Countries",
        method="update"
    )]
    
    for i, country in enumerate(countries[:20]):
        visibility = [True] * 5 + [False] * (len(fig.data) - 5)
        visibility[5 + i] = True  # Show country exposure
        
        buttons.append(dict(
            args=[{"visible": visibility}],
            label=country,
            method="update"
        ))
    
    fig.update_layout(
        height=2400,

        showlegend=True,
        updatemenus=[dict(
            buttons=buttons,
            direction="down",
            showactive=True,
            x=0.5,
            y=1.02,
            xanchor="center",
            yanchor="top",
            bgcolor="#2E5077",
            bordercolor="#ffffff",
            borderwidth=2,
            font=dict(color="white", size=14)
        )],
        annotations=[dict(
            text="<b>All Countries</b>",
            x=0.5,
            y=1.05,
            xref="paper",
            yref="paper",
            showarrow=False,
            font=dict(size=16, color="#2E5077", family="Arial Black")
        )]
    )
    
    # Update axes labels
    fig.update_xaxes(title_text="Exposure Level", row=1, col=1)
    fig.update_yaxes(title_text="Bleaching %", row=1, col=1)
    fig.update_xaxes(title_text="Country", row=2, col=1, tickangle=45)
    fig.update_yaxes(title_text="Bleaching %", row=2, col=1)
    fig.update_xaxes(title_text="Year", row=3, col=1)
    fig.update_yaxes(title_text="Temperature (K)", row=3, col=1)
    fig.update_xaxes(title_text="Year", row=4, col=1)
    fig.update_yaxes(title_text="Turbidity", row=4, col=1)
    fig.update_xaxes(title_text="Year", row=5, col=1)
    fig.update_yaxes(title_text="Wind Speed (m/s)", row=5, col=1)
    
    return fig


# Visualization 4 - Management Authorities
def create_management_analysis():
    """Create management authorities coral recovery analysis"""
    recovery_df = load_recovery_data()
    
    # Management categories dictionary
    management_categories = {
        'National Park Service': 'National Government Agencies',
        'Federal or national ministry or agency': 'National Government Agencies',
        'Ministry of Environment': 'National Government Agencies',
        'Ministry of Agriculture': 'National Government Agencies',
        'U.S. Fish and Wildlife Service': 'National Government Agencies',
        'Department of Environment': 'National Government Agencies',
        'Environmental Protection Agency': 'National Government Agencies',
        'National Oceanic and Atmospheric Administration': 'National Government Agencies',
        'AU-QLD_DES': 'State/Provincial Authorities',
        'AU-WA_DBCA': 'State/Provincial Authorities',
        'AU-NSW_OEH': 'State/Provincial Authorities',
        'State Department of Conservation': 'State/Provincial Authorities',
        'State Fish and Wildlife': 'State/Provincial Authorities',
        'Mili Atoll Local Government': 'Local/Regional Management',
        'Jaluit Atoll Local Government': 'Local/Regional Management',
        'Rongelap Atoll Local Government': 'Local/Regional Management',
        'LGU': 'Local/Regional Management',
        'Village Chiefs': 'Traditional/Community Management',
        'Qoliqoli Committee': 'Traditional/Community Management',
        'Traditional Fisherman': 'Traditional/Community Management',
        'Fish Wardens': 'Traditional/Community Management',
        'Community': 'Traditional/Community Management',
        'Protected Area Management Board': 'Protected Area Management',
        'Marine Parks and Reserves Unit': 'Protected Area Management',
        'National Parks Trust': 'Protected Area Management',
        'Sabah Parks': 'Protected Area Management',
        'Fisheries Department': 'Fisheries Management',
        'Fisheries Division': 'Fisheries Management',
        'Seychelles Fishing Authority': 'Fisheries Management',
        'Ministry of Fisheries': 'Fisheries Management',
        'Nature Seychelles': 'Conservation Organizations',
        'Chumbe Island Coral Park': 'Conservation Organizations',
        'Bahamas National Trust': 'Conservation Organizations',
        'Bermuda Audubon Society': 'Conservation Organizations'
    }
    
    def assign_category(authority):
        if pd.isna(authority):
            return 'Unspecified'
        if authority in management_categories:
            return management_categories[authority]
        if any(keyword in str(authority).lower() for keyword in ['ministry', 'national', 'federal']):
            return 'National Government Agencies'
        elif any(keyword in str(authority).lower() for keyword in ['park', 'protected area']):
            return 'Protected Area Management'
        elif any(keyword in str(authority).lower() for keyword in ['fish']):
            return 'Fisheries Management'
        elif any(keyword in str(authority).lower() for keyword in ['community', 'village', 'traditional']):
            return 'Traditional/Community Management'
        elif any(keyword in str(authority).lower() for keyword in ['conservation', 'nature']):
            return 'Conservation Organizations'
        else:
            return 'Other'
    
    # Filter and prepare data
    recovery_mgmt = recovery_df[
        (recovery_df['management_authority'].notnull()) &
        (recovery_df['management_authority'] != 'nd') &
        (recovery_df['management_authority'] != 'Not Reported') &
        (recovery_df['percent_hard_coral_cover'].notnull())
    ].copy()
    
    # Apply categorization
    recovery_mgmt['management_category'] = recovery_mgmt['management_authority'].apply(assign_category)
    
    # Calculate mean recovery by category
    agg_by_category = recovery_mgmt.groupby('management_category')['percent_hard_coral_cover'].mean().reset_index()
    agg_by_category = agg_by_category.sort_values('percent_hard_coral_cover', ascending=True)
    
    fig = go.Figure(go.Bar(
        y=agg_by_category['management_category'],
        x=agg_by_category['percent_hard_coral_cover'],
        orientation='h',
        marker=dict(
            color=agg_by_category['percent_hard_coral_cover'],
            colorscale=[[0, '#E1F5FE'], [0.5, '#4FC3F7'], [1, '#01579B']],
            showscale=True,
            colorbar=dict(title="Mean Recovery %")
        ),
        hovertemplate='<b>%{y}</b><br>Mean Recovery: %{x:.2f}%<extra></extra>'
    ))
    
    fig.update_layout(
        xaxis_title='Mean Percent Hard Coral Cover',
        yaxis_title='Management Category',
        height=600,
        margin=dict(l=200)
    )
    
    return fig

# Visualization 5 - GBR Forecast Analysis
def create_gbr_forecast():
    """Create Great Barrier Reef forecast visualization"""
    hist_df = load_gbr_historical()
    forecast_df = load_gbr_forecast()
    
    # Process historical data
    hist_df["date_year"] = pd.to_datetime(hist_df["date_year"])
    x_hist = hist_df["date_year"].dt.year.values
    y_hist = hist_df["percent_hard_coral_cover"].values
    
    # Process forecast data
    x_fore = forecast_df["year"].values
    y_fore = forecast_df["forecast_percent_hard_coral_cover"].values
    y_lo = forecast_df["lower_95"].values
    y_hi = forecast_df["upper_95"].values
    
    fig = go.Figure()
    
    # Add historical data
    fig.add_trace(go.Scatter(
        x=x_hist,
        y=y_hist,
        mode='lines+markers',
        name='Observed',
        line=dict(color='#4FC3F7', width=3),
        marker=dict(size=8, color='#4FC3F7')
    ))
    
    # Add forecast data
    fig.add_trace(go.Scatter(
        x=x_fore,
        y=y_fore,
        mode='lines+markers',
        name='Forecast',
        line=dict(color='#01579B', width=3),
        marker=dict(size=8, color='#01579B')
    ))
    
    # Add confidence interval upper bound
    fig.add_trace(go.Scatter(
        x=x_fore,
        y=y_hi,
        mode='lines',
        line=dict(width=0),
        showlegend=False
    ))
    
    # Add confidence interval lower bound with fill
    fig.add_trace(go.Scatter(
        x=x_fore,
        y=y_lo,
        mode='lines',
        line=dict(width=0),
        fillcolor='rgba(79, 195, 247, 0.2)',
        fill='tonexty',
        name='95% Confidence Interval'
    ))
    
    fig.update_layout(
        xaxis_title='Year',
        yaxis_title='Hard Coral Cover Percentage',
        height=600,
        showlegend=True,
        hovermode='x unified',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.06,
            xanchor="center",
            x=0.5
        )
    )
    
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(211, 211, 211, 0.5)')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(211, 211, 211, 0.5)')
    
    return fig


