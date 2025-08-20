import streamlit as st

# Color Palette
palette = {
    "salmon": "#F6A58D",
    "deep_blue": "#003f5c",
    "coral_red": "#ff6f61",
    "turquoise": "#2f9e99",
    "off_white": "#fdfdfd"
}

# Color Palette Application
def apply_styling():
    st.markdown(f"""
    <style>
    /* 1. Gradient salmon background */
    .stApp {{
        background: linear-gradient(160deg, {palette['salmon']} 0%, #ff8566 100%);
    }}

    /* 2. Body text */
    .stMarkdown p, .stMarkdown li {{
        color: {palette['deep_blue']} !important;
    }}

    /* 2. Header hierarchy */
    h1, h2 {{
        color: {palette['deep_blue']} !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.25);
        letter-spacing: 0.5px;
    }}
    h3, h4 {{
        color: {palette['off_white']} !important;
        font-weight: 600;
    }}
    h5, h6 {{
        color: {palette['coral_red']} !important;
        font-weight: 500;
    }}

    /* 3. Links & buttons */
    a, .stButton button {{
        background-color: {palette['deep_blue']} !important;
        color: {palette['off_white']} !important;
        border-radius: 8px;
        padding: 6px 12px;
        border: none;
    }}
    a:hover, .stButton button:hover {{
        background-color: {palette['turquoise']} !important;
        color: #ffffff !important;
    }}

    /* 4. Rounded image corners */
    .stImage img {{
        border-radius: 15px;
    }}
    
    /* 5. Rounded chart corners */
    .js-plotly-plot .plotly .modebar {{
        display: none !important;
    }}
    .js-plotly-plot .plotly {{
        border-radius: 12px;
        overflow: hidden;
    }}
    .stPlotlyChart > div {{
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }}
    .matplotlib-container {{
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }}
    </style>
    """, unsafe_allow_html=True)