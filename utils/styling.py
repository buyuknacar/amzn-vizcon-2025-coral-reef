import streamlit as st

# Color Palette
palette = {
    "salmon": "#F6A58D",
    "deep_blue": "#003f5c",
    "coral_red": "#ff6f61",
    "turquoise": "#2f9e99",
    "off_white": "#fdfdfd",
    "powder_blue": "#B0E0E6",    # A soft, light blue that pairs well with salmon
    "steel_blue": "#4682B4",     # A medium blue that bridges deep_blue and turquoise
    "cerulean": "#007BA7",       # A bright middle blue that complements coral_red
    "dusty_blue": "#6699CC",     # A muted blue that works with the overall scheme
    "sky_blue": "#87CEEB"        # A light, airy blue that contrasts with deep_blue
}


# Color Palette Application
def apply_styling():
    st.markdown(f"""
    <style>
    /* 1. Gradient powder blue background */
    .stApp {{
        background: linear-gradient(160deg, {palette['powder_blue']} 0%, #87CEEB 100%);
    }}

    /* 2. Body text */
    .stMarkdown p, .stMarkdown li {{
        color: {palette['deep_blue']} !important;
        font-size: 18px !important;
    }}

    /* 2. Header hierarchy */
    h1, h2 {{
        color: {palette['deep_blue']} !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.25);
        letter-spacing: 0.5px;
    }}
    h3, h4 {{
        color: {palette['deep_blue']} !important;
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
    
    /* 6. Container styling */
    .stApp > div:first-child > div:first-child > div:first-child > div:nth-child(4) {{
        background-color: {palette['deep_blue']} !important;
        padding: 20px;
        border-radius: 12px;
        margin: 10px 0;
    }}
    .stApp > div:first-child > div:first-child > div:first-child > div:nth-child(4) .stMarkdown p {{
        color: {palette['off_white']} !important;
    }}
    .stApp > div:first-child > div:first-child > div:first-child > div:nth-child(4) h2, 
    .stApp > div:first-child > div:first-child > div:first-child > div:nth-child(4) h3 {{
        color: {palette['off_white']} !important;
    }}
    </style>
    """, unsafe_allow_html=True)