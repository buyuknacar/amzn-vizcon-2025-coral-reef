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
    
    fig.update_layout(
        coloraxis_colorbar=dict(
            title=dict(text="Percent Bleaching", font=dict(color='black', size=16), side="top"),
            tickfont=dict(color='black', size=14),
            orientation="h",
            x=0.5,
            xanchor="center",
            y=1.02,
            yanchor="bottom"
        ),
        sliders=[dict(
            currentvalue=dict(prefix="Year: ", font=dict(size=18)),
            font=dict(size=16),
            steps=[dict(label=str(year), method="animate", args=[[str(year)]]) for year in sorted(bleaching_filtered['date_year'].unique())]
        )],
        plot_bgcolor='#F5FBFF',
        paper_bgcolor='#F5FBFF',
        font=dict(color='black', size=16),
        hoverlabel=dict(font_size=16),
        mapbox=dict(
            bounds=dict(west=-180, east=180, south=-90, north=90)
        )
    )
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
        textposition='outside',
        textfont=dict(size=16)
    )])
    
    fig.update_layout(
        height=500,
        showlegend=False,
        plot_bgcolor='#F5FBFF',
        paper_bgcolor='#F5FBFF',
        font=dict(color='black', size=14),
        hoverlabel=dict(font_size=16)
    )
    
    return fig

# Visualization 3 - Coral Bleaching and Environmental Correlation
def create_bleaching_dashboard():
    """Create comprehensive coral bleaching analysis dashboard"""
    df = load_bleaching_data()
    
    # Color scheme
    CHART_COLORS = {
        'default': '#2E5077',
        'temperature': '#8B0000',
        'windspeed': '#006400',
        'turbidity': '#00008B',
        'top15_default': '#2F4F4F',
        'top15_highlight': '#4169E1',
        'grid': '#E8E8E8'
    }
    
    # Clean data
    df['date_year'] = pd.to_datetime(df['date']).dt.year
    numeric_cols = ['percent_bleaching', 'temperature_maximum', 'windspeed', 'turbidity']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    df = df.dropna(subset=['percent_bleaching'])
    
    countries = sorted(df['country_name'].unique())
    
    fig = make_subplots(
        rows=3, cols=2,
        subplot_titles=(
            '<b>Mean Bleaching Percentage Over Years</b>',
            '<b>Bleaching by Exposure Level</b>',
            '<b>Top 15 Countries by Bleaching Severity</b>',
            '<b>Mean Sea Temperature Over Years</b>',
            '<b>Mean Water Turbidity Over Years</b>',
            '<b>Mean Wind Speed Over Years</b>'
        ),
        specs=[[{"type": "scatter"}, {"type": "bar"}],
               [{"type": "bar"}, {"type": "scatter"}],
               [{"type": "scatter"}, {"type": "scatter"}]],
        vertical_spacing=0.22,
        horizontal_spacing=0.15
    )
    
    # Make subplot titles black
    for annotation in fig['layout']['annotations']:
        annotation['font'] = dict(color='black', size=14)
    
    # Top 15 countries
    country_bleaching = (df.groupby('country_name')['percent_bleaching']
                        .agg(['mean', 'count'])
                        .reset_index()
                        .sort_values('mean', ascending=False))
    top_15_countries = set(country_bleaching[country_bleaching['count'] >= 100].head(15)['country_name'])
    
    # Create traces per country
    for country in countries:
        country_data = df[df['country_name'] == country]
        
        # Bleaching trends
        yearly_bleaching = country_data.groupby('date_year')['percent_bleaching'].mean().reset_index()
        fig.add_trace(go.Scatter(
            x=yearly_bleaching['date_year'], y=yearly_bleaching['percent_bleaching'],
            mode='lines+markers', name=country, line=dict(color=CHART_COLORS['default']),
            visible=False
        ), row=1, col=1)
        
        # Exposure distribution
        exposure_data = country_data.groupby('exposure')['percent_bleaching'].mean().reset_index()
        fig.add_trace(go.Bar(
            x=exposure_data['exposure'], y=exposure_data['percent_bleaching'],
            name=country, marker_color=CHART_COLORS['default'], visible=False
        ), row=1, col=2)
        
        # Temperature trends
        temp_data = country_data.groupby('date_year')['temperature_maximum'].mean().reset_index()
        fig.add_trace(go.Scatter(
            x=temp_data['date_year'], y=temp_data['temperature_maximum'],
            name=country, line=dict(color=CHART_COLORS['temperature']), visible=False
        ), row=2, col=2)
        
        # Turbidity trends
        turb_data = country_data.groupby('date_year')['turbidity'].mean().reset_index()
        fig.add_trace(go.Scatter(
            x=turb_data['date_year'], y=turb_data['turbidity'],
            name=country, line=dict(color=CHART_COLORS['turbidity']), visible=False
        ), row=3, col=1)
        
        # Wind speed trends
        wind_data = country_data.groupby('date_year')['windspeed'].mean().reset_index()
        fig.add_trace(go.Scatter(
            x=wind_data['date_year'], y=wind_data['windspeed'],
            name=country, line=dict(color=CHART_COLORS['windspeed']), visible=False
        ), row=3, col=2)
    
    # Add global traces
    global_bleaching = df.groupby('date_year')['percent_bleaching'].mean().reset_index()
    fig.add_trace(go.Scatter(
        x=global_bleaching['date_year'], y=global_bleaching['percent_bleaching'],
        mode='lines+markers', name='Global Average', line=dict(color=CHART_COLORS['default']),
        visible=True
    ), row=1, col=1)
    
    global_exposure = df.groupby('exposure')['percent_bleaching'].mean().reset_index()
    fig.add_trace(go.Bar(
        x=global_exposure['exposure'], y=global_exposure['percent_bleaching'],
        name='Global Exposure', marker_color=CHART_COLORS['default'], visible=True
    ), row=1, col=2)
    
    global_temp = df.groupby('date_year')['temperature_maximum'].mean().reset_index()
    fig.add_trace(go.Scatter(
        x=global_temp['date_year'], y=global_temp['temperature_maximum'],
        name='Global Temperature', line=dict(color=CHART_COLORS['temperature']), visible=True
    ), row=2, col=2)
    
    global_turb = df.groupby('date_year')['turbidity'].mean().reset_index()
    fig.add_trace(go.Scatter(
        x=global_turb['date_year'], y=global_turb['turbidity'],
        name='Global Turbidity', line=dict(color=CHART_COLORS['turbidity']), visible=True
    ), row=3, col=1)
    
    global_wind = df.groupby('date_year')['windspeed'].mean().reset_index()
    fig.add_trace(go.Scatter(
        x=global_wind['date_year'], y=global_wind['windspeed'],
        name='Global Wind Speed', line=dict(color=CHART_COLORS['windspeed']), visible=True
    ), row=3, col=2)
    
    # Top 15 Countries Chart
    top_15 = country_bleaching[country_bleaching['count'] >= 100].head(15)
    fig.add_trace(go.Bar(
        x=top_15['country_name'], y=top_15['mean'],
        name='Top 15 Countries', marker_color=[CHART_COLORS['top15_default']] * len(top_15),
        visible=True
    ), row=2, col=1)
    
    # Create dropdown menu
    buttons = []
    n_traces_per_country = 5
    total_country_traces = len(countries) * n_traces_per_country
    
    buttons.append(dict(
        args=[{"visible": [False] * total_country_traces + [True] * 6}],
        label="All Countries", method="update"
    ))
    
    for i, country in enumerate(countries):
        visibility = [False] * len(fig.data)
        country_trace_indices = range(i * n_traces_per_country, (i + 1) * n_traces_per_country)
        for idx in country_trace_indices:
            visibility[idx] = True
        visibility[-1] = True
        
        buttons.append(dict(
            args=[{"visible": visibility}],
            label=country, method="update"
        ))
    
    fig.update_layout(
        height=1300, width=1200,
        showlegend=False,
        plot_bgcolor='white', paper_bgcolor='white',
        hoverlabel=dict(font_size=16),
        updatemenus=[dict(
            buttons=buttons, direction="down", showactive=True,
            x=0.5, xanchor="center", y=1.05, yanchor="middle",
            bgcolor='#01579B', font=dict(size=12, color='black'),
            bordercolor='#01579B'
        )]
    )
    
    # Update axes with black labels
    fig.update_yaxes(title_text="<b>Bleaching Percentage (%)</b>", title_font=dict(color='black'), tickfont=dict(color='black'), row=1, col=1)
    fig.update_xaxes(title_text="<b>Year</b>", title_font=dict(color='black'), tickfont=dict(color='black'), row=1, col=1)
    fig.update_xaxes(title_text="<b>Exposure Level</b>", title_font=dict(color='black'), tickfont=dict(color='black'), row=1, col=2)
    fig.update_yaxes(title_text="<b>Average Bleaching (%)</b>", title_font=dict(color='black'), tickfont=dict(color='black'), row=1, col=2)
    fig.update_xaxes(title_text="<b>Country</b>", title_font=dict(color='black'), tickfont=dict(color='black'), tickangle=45, row=2, col=1)
    fig.update_yaxes(title_text="<b>Average Bleaching (%)</b>", title_font=dict(color='black'), tickfont=dict(color='black'), row=2, col=1)
    fig.update_xaxes(title_text="<b>Year</b>", title_font=dict(color='black'), tickfont=dict(color='black'), row=2, col=2)
    fig.update_yaxes(title_text="<b>Temperature (K)</b>", title_font=dict(color='black'), tickfont=dict(color='black'), row=2, col=2)
    fig.update_xaxes(title_text="<b>Year</b>", title_font=dict(color='black'), tickfont=dict(color='black'), row=3, col=1)
    fig.update_yaxes(title_text="<b>Turbidity Level</b>", title_font=dict(color='black'), tickfont=dict(color='black'), row=3, col=1)
    fig.update_xaxes(title_text="<b>Year</b>", title_font=dict(color='black'), tickfont=dict(color='black'), row=3, col=2)
    fig.update_yaxes(title_text="<b>Wind Speed (m/s)</b>", title_font=dict(color='black'), tickfont=dict(color='black'), row=3, col=2)
    
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
        margin=dict(l=200),
        plot_bgcolor='#F5FBFF',
        paper_bgcolor='#F5FBFF',
        font=dict(color='black'),
        hoverlabel=dict(font_size=16)
    )
    
    fig.update_xaxes(title_font=dict(size=16, color='black'), tickfont=dict(size=14, color='black'))
    fig.update_yaxes(title_font=dict(size=16, color='black'), tickfont=dict(size=14, color='black'))
    
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
        showlegend=False,
        hovertemplate='<b>Upper 95% CI:</b> %{y:.2f}%<extra></extra>'
    ))
    
    # Add confidence interval lower bound with fill
    fig.add_trace(go.Scatter(
        x=x_fore,
        y=y_lo,
        mode='lines',
        line=dict(width=0),
        fillcolor='rgba(79, 195, 247, 0.2)',
        fill='tonexty',
        name='95% Confidence Interval',
        hovertemplate='<b>Lower 95% CI:</b> %{y:.2f}%<extra></extra>'
    ))
    
    fig.update_layout(
        xaxis_title='Year',
        yaxis_title='Hard Coral Cover Percentage',
        height=600,
        showlegend=True,
        hovermode='x unified',
        plot_bgcolor='#F5FBFF',
        paper_bgcolor='#F5FBFF',
        font=dict(color='black'),
        hoverlabel=dict(font_size=16),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5,
            font=dict(size=18)
        )
    )
    
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(211, 211, 211, 0.5)', title_font=dict(size=16, color='black'), tickfont=dict(size=14, color='black'))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(211, 211, 211, 0.5)', title_font=dict(size=16, color='black'), tickfont=dict(size=14, color='black'))
    
    return fig

# Visualization 6 - Global Climate Events Timeline
def create_climate_timeline():
    """Create global climate events timeline visualization"""
    # Define timeline events with improved formatting
    events = [
        {
            "year": "2005",
            "event": "Caribbean Heatwave Crisis",
            "detail": "80% bleaching in some reefs",
            "color": "#FFA500",
            "position": -1
        },
        {
            "year": "2010",
            "event": "SE Asia & Indian Ocean Event",
            "detail": "Moderate El Niño bleaching",
            "color": "#FF4500",
            "position": 1
        },
        {
            "year": "2014–2017",
            "event": "Longest Global Bleaching",
            "detail": "Severe damage on Great Barrier Reef",
            "color": "#FF0000",
            "position": -1
        },
        {
            "year": "2019–2020",
            "event": "Pacific & GBR Crisis",
            "detail": "High ocean heat stress",
            "color": "#8B0000",
            "position": 1
        }
    ]

    # Create figure
    fig = go.Figure()

    # Add markers and text for each event
    for i, e in enumerate(events):
        y_pos = 0 if e["position"] > 0 else 0
        text_pos = "top center" if e["position"] > 0 else "bottom center"
        
        # Add event markers
        fig.add_trace(go.Scatter(
            x=[i],
            y=[y_pos],
            mode="markers+text",
            marker=dict(
                size=25,
                color=e["color"],
                line=dict(color="white", width=2)
            ),
            text=[f"<b>{e['year']}</b><br>{e['event']}<br><i>{e['detail']}</i>"],
            textposition=text_pos,
            textfont=dict(size=18),
            hoverinfo="text",
            hovertext=f"<b>Year:</b> {e['year']}<br><b>Event:</b> {e['event']}<br><b>Impact:</b> {e['detail']}",
            showlegend=False
        ))

    # Add connecting line
    fig.add_trace(go.Scatter(
        x=list(range(len(events))),
        y=[0]*len(events),
        mode="lines",
        line=dict(color="gray", width=3),
        hoverinfo="none",
        showlegend=False
    ))

    # Update layout
    fig.update_layout(
        showlegend=False,
        xaxis=dict(
            showticklabels=False,
            showgrid=False,
            zeroline=False,
            range=[-0.5, len(events)-0.5]
        ),
        yaxis=dict(
            showticklabels=False,
            showgrid=False,
            zeroline=False,
            range=[-0.5, 0.5]
        ),
        height=400,
        margin=dict(l=50, r=50, t=20, b=20),
        plot_bgcolor='#F5FBFF',
        paper_bgcolor='#F5FBFF',
        font=dict(color='black'),
        hoverlabel=dict(font_size=16),
        shapes=[
            dict(
                type="line",
                x0=-0.5,
                y0=-0.01,
                x1=len(events)-0.5,
                y1=-0.01,
                line=dict(color="rgba(0,0,0,0.1)", width=5)
            )
        ]
    )
    
    return fig


