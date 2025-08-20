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

# Visualization 3 - KMeans Analysis
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

# Visualization 4 - Coral Bleaching and Environmental Correlation
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
        rows=6, cols=1,
        subplot_titles=(
            'Mean Bleaching Percentage Over Years',
            'Bleaching by Exposure Level',
            'Top 15 Countries by Bleaching Severity',
            'Mean Sea Temperature Over Years',
            'Mean Water Turbidity Over Years',
            'Mean Wind Speed Over Years'
        ),
        specs=[
            [{"type": "scatter"}],
            [{"type": "bar"}],
            [{"type": "bar"}],
            [{"type": "scatter"}],
            [{"type": "scatter"}],
            [{"type": "scatter"}]
        ],
        vertical_spacing=0.06
    )
    
    # Global data traces
    global_bleaching = df.groupby('date_year')['percent_bleaching'].mean().reset_index()
    fig.add_trace(
        go.Scatter(
            x=global_bleaching['date_year'],
            y=global_bleaching['percent_bleaching'],
            mode='lines+markers',
            name='Global Average',
            line=dict(color='#2E5077'),
            visible=True
        ),
        row=1, col=1
    )
    
    global_exposure = df.groupby('exposure')['percent_bleaching'].mean().reset_index()
    fig.add_trace(
        go.Bar(
            x=global_exposure['exposure'],
            y=global_exposure['percent_bleaching'],
            name='Global Exposure',
            marker_color='#2E5077',
            visible=True
        ),
        row=2, col=1
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
            visible=True
        ),
        row=3, col=1
    )
    
    # Global environmental factors
    global_temp = df.groupby('date_year')['temperature_maximum'].mean().reset_index()
    fig.add_trace(
        go.Scatter(
            x=global_temp['date_year'],
            y=global_temp['temperature_maximum'],
            name='Global Temperature',
            line=dict(color='#8B0000'),
            visible=True
        ),
        row=4, col=1
    )
    
    global_turb = df.groupby('date_year')['turbidity'].mean().reset_index()
    fig.add_trace(
        go.Scatter(
            x=global_turb['date_year'],
            y=global_turb['turbidity'],
            name='Global Turbidity',
            line=dict(color='#00008B'),
            visible=True
        ),
        row=5, col=1
    )
    
    global_wind = df.groupby('date_year')['windspeed'].mean().reset_index()
    fig.add_trace(
        go.Scatter(
            x=global_wind['date_year'],
            y=global_wind['windspeed'],
            name='Global Wind Speed',
            line=dict(color='#006400'),
            visible=True
        ),
        row=6, col=1
    )
    
    # Country-specific traces (initially hidden)
    for country in countries[:20]:  # Limit to first 20 countries for performance
        country_data = df[df['country_name'] == country]
        
        yearly_bleaching = country_data.groupby('date_year')['percent_bleaching'].mean().reset_index()
        fig.add_trace(
            go.Scatter(
                x=yearly_bleaching['date_year'],
                y=yearly_bleaching['percent_bleaching'],
                mode='lines+markers',
                name=f'{country} Bleaching',
                line=dict(color='#2E5077'),
                visible=False
            ),
            row=1, col=1
        )
        
        exposure_data = country_data.groupby('exposure')['percent_bleaching'].mean().reset_index()
        fig.add_trace(
            go.Bar(
                x=exposure_data['exposure'],
                y=exposure_data['percent_bleaching'],
                name=f'{country} Exposure',
                marker_color='#2E5077',
                visible=False
            ),
            row=2, col=1
        )
    
    # Create dropdown for country selection
    buttons = [dict(
        args=[{"visible": [True] * 6 + [False] * (len(fig.data) - 6)}],
        label="Global View",
        method="update"
    )]
    
    for i, country in enumerate(countries[:20]):
        visibility = [True] * 6 + [False] * (len(fig.data) - 6)
        visibility[6 + i * 2] = True  # Show country bleaching
        visibility[6 + i * 2 + 1] = True  # Show country exposure
        
        buttons.append(dict(
            args=[{"visible": visibility}],
            label=country,
            method="update"
        ))
    
    fig.update_layout(
        height=2800,
        title_text="Coral Bleaching Analysis Dashboard",
        showlegend=True,
        updatemenus=[dict(
            buttons=buttons,
            direction="down",
            showactive=True,
            x=0.1,
            y=1.1
        )]
    )
    
    # Update axes labels
    fig.update_xaxes(title_text="Year", row=1, col=1)
    fig.update_yaxes(title_text="Bleaching %", row=1, col=1)
    fig.update_xaxes(title_text="Exposure Level", row=2, col=1)
    fig.update_yaxes(title_text="Bleaching %", row=2, col=1)
    fig.update_xaxes(title_text="Country", row=3, col=1, tickangle=45)
    fig.update_yaxes(title_text="Bleaching %", row=3, col=1)
    fig.update_xaxes(title_text="Year", row=4, col=1)
    fig.update_yaxes(title_text="Temperature (K)", row=4, col=1)
    fig.update_xaxes(title_text="Year", row=5, col=1)
    fig.update_yaxes(title_text="Turbidity", row=5, col=1)
    fig.update_xaxes(title_text="Year", row=6, col=1)
    fig.update_yaxes(title_text="Wind Speed (m/s)", row=6, col=1)
    
    return fig


# Visualization 5 - Management Authorities
def create_management_analysis():
    """Create management authorities coral recovery analysis"""
    recovery_df = load_recovery_data()
    
    # Filter recovery data excluding null, 'nd', and 'Not Reported'
    recovery_mgmt = recovery_df[
        (recovery_df['management_authority'].notnull()) &
        (recovery_df['management_authority'] != 'nd') &
        (recovery_df['management_authority'] != 'Not Reported') &
        (recovery_df['percent_hard_coral_cover'].notnull())
    ].copy()
    
    # Aggregate mean recovery percent and count per management authority
    agg = recovery_mgmt.groupby('management_authority').agg(
        mean_recovery=('percent_hard_coral_cover', 'mean'),
        count=('percent_hard_coral_cover', 'size')
    ).reset_index()
    
    # Keep only top 15 by count and sort by mean recovery ascending
    agg_top = agg.sort_values('count', ascending=False).head(15)
    agg_top = agg_top.sort_values('mean_recovery', ascending=True)
    
    fig = go.Figure(go.Bar(
        y=agg_top['management_authority'],
        x=agg_top['mean_recovery'],
        orientation='h',
        marker=dict(
            color=agg_top['mean_recovery'],
            colorscale='Greens',
            showscale=True,
            colorbar=dict(title="Mean Recovery %")
        ),
        text=agg_top['count'],
        textposition='auto',
        hovertemplate='<b>%{y}</b><br>Mean Recovery: %{x:.2f}%<br>Samples: %{text}<extra></extra>'
    ))
    
    fig.update_layout(
        title='Top 15 Management Authorities by Mean Coral Recovery %',
        xaxis_title='Mean Percent Hard Coral Cover',
        yaxis_title='Management Authority',
        height=700,
        margin=dict(l=200)
    )
    
    return fig

# Visualization 6 - GBR Forecast Analysis
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
        line=dict(color='#2E5077'),
        marker=dict(size=6)
    ))
    
    # Add forecast data
    fig.add_trace(go.Scatter(
        x=x_fore,
        y=y_fore,
        mode='lines+markers',
        name='Forecast',
        line=dict(color='#FF6B6B'),
        marker=dict(size=6)
    ))
    
    # Add confidence interval
    fig.add_trace(go.Scatter(
        x=np.concatenate([x_fore, x_fore[::-1]]),
        y=np.concatenate([y_hi, y_lo[::-1]]),
        fill='toself',
        fillcolor='rgba(255, 107, 107, 0.2)',
        line=dict(color='rgba(255,255,255,0)'),
        name='95% Confidence Interval',
        showlegend=True
    ))
    
    fig.update_layout(
        title='Average Hard Coral Cover in the Great Barrier Reef<br><sub>Observed & 10-Year Forecast</sub>',
        xaxis_title='Year',
        yaxis_title='Hard Coral Cover Percentage',
        height=600,
        showlegend=True,
        hovermode='x unified'
    )
    
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    
    return fig


