# Library Imports
import streamlit as st
import plotly.express as p
from utils.styling import apply_styling
from utils.data_processing import create_bleaching_heatmap, create_kmeans_analysis, create_bleaching_dashboard, create_management_analysis, create_gbr_forecast, create_climate_timeline

# Configure page layout
st.set_page_config(layout="wide")

# Apply styling
apply_styling()


# TITLE
st.title("Coral Reefs Under Threat and Hope for Recovery")

st.markdown("\n")

st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
st.image("utils/salmon-teal-coral-reef.png")
st.markdown('</div>', unsafe_allow_html=True)
st.markdown("\n")

# Intro
st.markdown("""
## The Crisis Beneath the Waves

When trying to understand the topic of sustainability, the impact that humans have on the environment is an extremely broad and significant area of discussion. But, there is **no better example** of human impact on the environment than the negative impacts humans have had on coral reefs around the world.

Coral reefs are some of the most biologically diverse and productive ecosystems—home to a wide array of symbiotic species that create some of the most beautiful living architecture on Earth.
""")

st.info("An estimated **25% of all marine life**, including over 4,000 species of fish, are dependent on coral reefs at some point in their life cycle. **- *U.S. Environmental Protection Agency***")

st.markdown("""
### The Bleaching Crisis

However, coral reefs around the world have been significantly affected by the rise of global temperatures, changes in the climate, and general pollution of the environment and our oceans—undergoing a transformation known as **coral bleaching**.

Coral bleaching occurs when corals become stressed by changes in their environment, most commonly:
-  **Elevated sea temperatures**
-  **Increased UV radiation**
-  **Poor water quality and pollution**

During bleaching, corals become transparent—revealing their white skeletons. While bleached corals are still alive, they are significantly weakened and more vulnerable to starvation, disease, and even death.
""")

st.warning(" **The Ripple Effect**: When reefs die, fish populations decline, marine food webs collapse, coastal communities lose tourism income, and natural storm protection weakens.")

st.markdown("""
### Global Climate Events Timeline""")
    
with st.spinner("Loading climate timeline..."):
    fig = create_climate_timeline()
    st.plotly_chart(fig)

st.markdown("""
This timeline highlights major global climate events that have significantly impacted coral reef ecosystems worldwide. Each event represents a critical moment in the ongoing coral bleaching crisis.
""")

st.info("💡 **Insight**: Notice the increasing frequency and severity of bleaching events, particularly the unprecedented back-to-back events in recent years.")


st.divider()


# Datasets
st.header("Dataset Introduction")

st.image("utils/coral reef.jpg", 
         caption="Coral reefs are among Earth's most diverse ecosystems, supporting 25% of all marine life")

st.markdown("""
To understand the global coral crisis, we analyze two comprehensive datasets that capture both the **destruction** and **recovery** of coral reefs worldwide.
""")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Coral Bleaching Dataset")
    st.markdown("""
    **Focus**: Bleaching events and environmental stressors
    
    This dataset tracks coral bleaching presence/absence across global reef sites, enabling comparative analyses and determination of geographical bleaching thresholds.
    
    **Key Variables**:
    - Site exposure and distance to land
    - Mean turbidity and cyclone frequency  
    - Sea-surface temperature metrics
    - Bleaching severity indicators
    """)
    
with col2:
    st.subheader("Coral Recovery Dataset")
    st.markdown("""
    **Focus**: Recovery patterns following disturbances
    
    The Heatwaves and Coral-Recovery Database (HeatCRD) - the most comprehensive reference on coral recovery following marine heatwaves and other disturbances.
    
    **Key Variables**:
    - Coral cover percentages over time
    - MPA descriptions and protection status
    - Temperature and thermal stress indicators
    - Recovery rates and timelines
    """)

st.success("📈 **Combined Power**: 29,205+ data records spanning 44 years from 12,266 sites across 83 countries")

st.markdown("""
**Data Sources**: 
- [Coral Recovery Database](https://www.bco-dmo.org/dataset/933334)
            
- [Coral Bleaching Database](https://www.bco-dmo.org/dataset/773466)
""")

st.divider()

# Viz 1
st.markdown("## Coral Bleaching Over The Years")

with st.spinner("Loading bleaching visualization..."):
    fig = create_bleaching_heatmap()
    st.plotly_chart(fig)

st.markdown("""
This interactive heatmap reveals the global distribution and intensity of coral bleaching events from 2000-2019. 
The animation shows how bleaching patterns evolved over time, with warmer colors indicating higher bleaching percentages.
""")

st.info("💡 **Insight**: Use the play button to see temporal patterns, or drag the slider to explore specific years.")

# Viz 2
st.markdown("## K Means Analysis")

with st.spinner("Loading K-means analysis..."):
    fig = create_kmeans_analysis()
    st.plotly_chart(fig)

st.markdown("""
This analysis shows the relative influence of different environmental factors on coral recovery:
- **Geographic Location** and **Macroalgal Competition** are the dominant factors
- **Temperature Factors** and **Depth** have moderate influence
- **Other Environmental Factors** have minimal impact
""")

st.info("💡 **Insight**: Different colored clusters represent coral sites with similar environmental characteristics and bleaching patterns.")

# Viz 3
st.markdown("## Coral Bleaching and Environmental Correlation")

with st.spinner("Loading environmental correlation dashboard..."):
    fig = create_bleaching_dashboard()
    st.plotly_chart(fig)

st.markdown("""
This comprehensive dashboard analyzes the relationship between coral bleaching and environmental factors:
- **Bleaching trends** over time globally and by country
- **Exposure levels** impact on bleaching severity
- **Top 15 countries** most affected by bleaching
- **Environmental correlations** with temperature, turbidity, and wind speed
""")

st.info("💡 **Insight**: Use the dropdown to switch between global view and individual country analysis to identify regional patterns.")

# Viz 4
st.markdown("## Management Authority Effectiveness")

with st.spinner("Loading management analysis..."):
    fig = create_management_analysis()
    st.plotly_chart(fig)

st.markdown("""
This analysis evaluates the effectiveness of different management authorities in coral recovery:
- **Horizontal bar chart** shows mean coral recovery percentages by management authority
- **Color gradient** indicates recovery performance (darker green = better recovery)
- **Sample counts** displayed on bars show data reliability
""")

st.info("💡 **Insight**: Compare management approaches to identify which authorities achieve the highest coral recovery rates.")

# Viz 5
st.markdown("## Great Barrier Reef Forecast")

with st.spinner("Loading GBR forecast..."):
    fig = create_gbr_forecast()
    st.plotly_chart(fig)

st.markdown("""
This time series analysis shows the Great Barrier Reef's coral cover trajectory:
- **Historical data** (blue) shows observed coral cover percentages over time
- **Forecast data** (red) projects future coral cover for the next 10 years
- **Confidence interval** (shaded area) indicates forecast uncertainty range
""")

st.info("💡 **Insight**: The forecast helps predict future coral health trends and informs conservation planning decisions.")

