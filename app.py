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
# st.title("Coral Reefs Under Threat and Hope for Recovery")

# st.title("From Bleaching to Balance: Coral Sustainability Matters")

st.title("FROM BRIGHT TO WHITE")
st.subheader("A Bleaching and Recovery Analysis")



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

st.info(" **The Ripple Effect**: When reefs die, fish populations decline, marine food webs collapse, coastal communities lose tourism income, and natural storm protection weakens.")

st.markdown("""
### Global Climate Events Timeline""")
    
with st.spinner("Loading climate timeline..."):
    fig = create_climate_timeline()
    st.plotly_chart(fig)

st.markdown("""
📊 **What it shows:**
An annotated timeline of global climate events that affected coral bleaching

🔎 **Meaning:**
By overlaying real-world events, this chart connects the data to human and ecological consequences
""")


st.divider()


# Datasets
st.header("Dataset Introduction")


st.markdown("""
To understand the global coral crisis, we analyze two comprehensive datasets that capture both the **destruction** and **recovery** of coral reefs worldwide.
""")

col1, col2 = st.columns(2)

with col1:
    st.subheader("[Coral Bleaching Dataset](https://www.bco-dmo.org/dataset/773466)")
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
    st.subheader("[Coral Recovery Dataset](https://www.bco-dmo.org/dataset/933334)")
    st.markdown("""
    **Focus**: Recovery patterns following disturbances
    
    The Heatwaves and Coral-Recovery Database (HeatCRD) - the most comprehensive reference on coral recovery following marine heatwaves and other disturbances.
    
    **Key Variables**:
    - Coral cover percentages over time
    - MPA descriptions and protection status
    - Temperature and thermal stress indicators
    - Recovery rates and timelines
    """)

st.info("📈 **Combined Power**: 29,205+ data records spanning 44 years from 12,266 sites across 83 countries")



st.divider()

# Viz 1
st.markdown("## Coral Bleaching Over The Years")

with st.spinner("Loading bleaching visualization..."):
    fig = create_bleaching_heatmap()
    st.plotly_chart(fig)

st.markdown("""
Chart 1 – Global Heatmap of Coral Bleaching Over Time

📊 **What it shows:**
A timeline of bleaching events across global reef locations since 2000, highlighting peaks in mass bleaching years.

🔎 **Meaning:**
This visualization communicates the alarming trend — bleaching is no longer rare. It's happening more frequently and with greater intensity, linked to global temperature rise. This chart also highlights the geographic hotspots, such as the Caribbean, Great Barrier Reef, and Indo-Pacific. It underlines that bleaching is not an isolated issue — it's a global climate crisis.
""")

# Viz 2
st.markdown("## K Means Analysis")

with st.spinner("Loading K-means analysis..."):
    fig = create_kmeans_analysis()
    st.plotly_chart(fig)

st.markdown("""
📊 **What it shows:**
Four key factors driving coral recovery: geographic location, temperature patterns, macroalgal competition, and depth

🔎 **Meaning:**
Geographic location dominates recovery patterns, explaining why some reefs are more resilient. Depth offers refuge in deeper waters, while algal competition threatens weakened corals post-bleaching. These insights guide targeted conservation — protecting deeper areas, controlling algal growth, and maintaining water quality can significantly improve recovery success for the 25% of marine life dependent on reefs.
""")

# Viz 3
st.markdown("## Coral Bleaching and Environmental Correlation")

with st.spinner("Loading environmental correlation dashboard..."):
    fig = create_bleaching_dashboard()
    st.plotly_chart(fig)

st.markdown("""
📊 **What it shows:**
Correlation of bleaching with exposure levels, sea temperature, turbidity, and windspeed

🔎 **Meaning:**
Temperature rise is the strongest driver, but local conditions like water clarity and wind patterns amplify vulnerability — proving the need for both global and local action.
""")

# Viz 4
st.markdown("## Management Authority Effectiveness")

with st.spinner("Loading management analysis..."):
    fig = create_management_analysis()
    st.plotly_chart(fig)

st.markdown("""
📊 **What it shows:** Recovery rates across different management approaches, with local/regional authorities achieving highest success (40%) and fisheries management close behind (35-40%).

🔎 **Meaning:** Localized management outperforms broad strategies because it addresses specific reef needs—controlling macroalgae, managing local stressors, and empowering communities. While global climate action remains crucial, these findings suggest that successful coral conservation depends on tailored, community-driven approaches that complement geographic and environmental factors.
""")

# Viz 5
st.markdown("## Great Barrier Reef Forecast")

with st.spinner("Loading GBR forecast..."):
    fig = create_gbr_forecast()
    st.plotly_chart(fig)

st.markdown("""
📊 **What it shows:** Historical coral cover (1990-2020) peaked at 35% in the mid-1990s, declined to 20-25% after 2010, with projections showing further decline to 15% by 2030.

🔎 **Meaning:** The widening confidence interval reflects increasing uncertainty as cumulative bleaching events reduce recovery windows. While the downward trend appears inevitable under current climate trajectories, varying management success rates suggest targeted interventions could moderate this decline, making every conservation effort critical for the reef's survival.
""")

st.divider()

st.markdown("""
## Conclusion

As we analyze the patterns of recovery and decline in places like the Great Barrier Reef, we learn so much about the resilience of nature and our role in protecting it. Coral bleaching can't be stopped entirely, but we can reduce its impact by cutting emissions, limiting local stressors like pollution, and supporting reef restoration efforts. Protecting coral reefs also means reducing coastal runoff, establishing marine protected areas, and investing in research that helps corals adapt to rising temperatures. 

While reefs have shown the ability to recover in the past, the combination of rising temperatures, pollution in the oceans, and more frequent extreme weather events is testing their ability to survive. Analyzing this data isn't just about documenting decline, it's about finding ways to protect and preserve these ecosystems for future generations.

            
### A reef without color is a warning, not an ending.
            
""")

st.divider()

st.markdown("## Tools and Tech Used")

st.markdown("\n")
st.markdown("\n")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.image("utils/streamlit.png", width=100)
    
with col2:
    st.image("utils/Q.jpeg", width=100)
    
with col3:
    st.image("utils/chatgpt.png", width=100)
    
with col4:
    st.image("utils/deepnote.png", width=100)
    
with col5:
    st.image("utils/python.png", width=100)