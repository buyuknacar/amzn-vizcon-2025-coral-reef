import streamlit as st
import plotly.express as p

# Color Palette
palette = {
    "salmon": "#ffa07a",
    "turquoise": "#2f9e99",
    "deep_blue": "#003f5c",
    "yellow": "#ffd166"
}


# Background Color
st.markdown(f"""
<style>
.stApp {{
    background-color: {palette['salmon']};
}}
</style>
""", unsafe_allow_html=True)

# TITLE
st.title("🐠 Coral Reef History")

# Intro
with st.container():
    st.markdown("""
    ## 🌊 The Crisis Beneath the Waves
    
    When trying to understand the topic of sustainability, the impact that humans have on the environment is an extremely broad and significant area of discussion. But, there is **no better example** of human impact on the environment than the negative impacts humans have had on coral reefs around the world.
    
    Coral reefs are some of the most biologically diverse and productive ecosystems—home to a wide array of symbiotic species that create some of the most beautiful living architecture on Earth.
    """)
    
    st.info("💡 **Did you know?** An estimated 25% of all marine life, including over 4,000 species of fish, are dependent on coral reefs at some point in their life cycle. - *U.S. Environmental Protection Agency*")
    
    st.markdown("""
    ### 🔥 The Bleaching Crisis
    
    However, coral reefs around the world have been significantly affected by the rise of global temperatures, changes in the climate, and general pollution of the environment and our oceans—undergoing a transformation known as **coral bleaching**.
    
    Coral bleaching occurs when corals become stressed by changes in their environment, most commonly:
    - 🌡️ **Elevated sea temperatures**
    - ☀️ **Increased UV radiation**
    - 🏭 **Poor water quality and pollution**
    
    During bleaching, corals become transparent—revealing their white skeletons. While bleached corals are still alive, they are significantly weakened and more vulnerable to starvation, disease, and even death.
    """)
    
    st.warning("⚠️ **The Ripple Effect**: When reefs die, fish populations decline, marine food webs collapse, coastal communities lose tourism income, and natural storm protection weakens.")
    
    st.markdown("""
    ### 🇦🇺 The Great Barrier Reef: A Global Crisis Symbol
    
    The Great Barrier Reef has become the global poster child for this crisis. As the world's largest reef system, its recent history of severe bleaching events has shocked scientists and sparked worldwide concern about the future of coral ecosystems.
    
    **Timeline of Mass Bleaching Events:**
    """)
    
    col1, col2 = st.columns([1, 3])
    with col1:
        st.metric("📅 1998", "First Event", "<5% mortality")
        st.metric("📅 2002", "Widespread", ">50% affected")
        st.metric("📅 2006", "Localized", "98% bleached")
        st.metric("📅 2016-17", "Back-to-back", "2/3 affected")
    
    with col2:
        st.markdown("""
        - **1998**: The first recorded mass bleaching event. Most reefs recovered fully with less than 5% of inshore reefs suffering high coral mortality
        - **2002**: More widespread than 1998, affecting over half of the observed reefs
        - **2006**: A localized event, mainly in the southern parts, with up to 98% of corals bleached on some reefs
        - **2016-2017**: Back-to-back bleaching years, a first for the reef, collectively affecting two-thirds of the Great Barrier Reef
        - **2020**: Widespread bleaching with restricted monitoring during Covid-19
        - **2022**: Unusual bleaching during typically cooler La Niña conditions
        - **2024**: Fifth mass bleaching event, part of the 4th global bleaching event
        - **2025**: Sixth mass bleaching since 2016, first time both Australian World Heritage reefs bleached simultaneously
        """)
    
    st.error("🚨 **Critical Alert**: 6 mass bleaching events in just 8 years (2016-2025) - an unprecedented frequency that gives reefs little time to recover.")

st.divider()


# Datasets
with st.container():
    st.header("Dataset Introduction")
    
    st.image("https://www.ogsociety.org/images/stories/articles/featured/GlobalReefs-04b_AWM1337.jpg", 
             caption="Coral reefs are among Earth's most diverse ecosystems, supporting 25% of all marine life")
    
    st.markdown("""
    To understand the global coral crisis, we analyze two comprehensive datasets that capture both the **destruction** and **recovery** of coral reefs worldwide.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔥 Coral Bleaching Dataset")
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
        st.subheader("🌱 Coral Recovery Dataset")
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
with st.container():
    st.markdown("## Viz 1 - Coral Bleaching Over The Years")
    
    ### Viz Code
    
    ### Visualization Write Up

# Viz 2
with st.container():
    st.markdown("## Viz 2 - Coral Recovery Over The years")
    
    ### Viz Code
    
    ### Visualization Write Up

# Viz 3
with st.container():
    st.markdown("## Viz 3 - K Means Analysis")
    
    ### Viz Code
    
    ### Visualization Write Up

# Viz 4
with st.container():
    st.markdown("## Viz 4 - Coral Exposure and Temperature Comparison")
    
    ### Viz Code
    
    ### Visualization Write Up

# Viz 5
with st.container():
    st.markdown("## Viz 5 - Ryan's Forecast")
    
    ### Viz Code
    
    ### Visualization Write Up



