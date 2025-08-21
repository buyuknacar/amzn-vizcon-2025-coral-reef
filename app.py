# Library Imports
import streamlit as st
import plotly.express as p
from utils.styling import apply_styling
from utils.data_processing import create_bleaching_heatmap, create_kmeans_analysis, create_bleaching_dashboard, create_management_analysis, create_gbr_forecast, create_climate_timeline

# Configure page layout
st.set_page_config(layout="wide")

# Apply styling
apply_styling()


col1, col2, col3 = st.columns([1, 4, 1])
with col2:

    # Main container for entire page
    with st.container():
        # TITLE
        # st.title("Coral Reefs Under Threat and Hope for Recovery")

        # st.title("From Bleaching to Balance: Coral Sustainability Matters")

        st.title("GUARDIANS OF THE SEA: CORAL REEFS")


        st.divider()


    st.markdown("\n")

    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        st.image("utils/salmon-teal-coral-reef.png", use_container_width=True)
    st.markdown("\n")

    # Intro
    st.markdown("""
    ## From Bright to White: The Journey of Coral Bleaching

    Coral reefs are often called the rainforests of the ocean. Though they cover less than 1% of the seafloor, they support nearly a quarter of all marine life, providing shelter and breeding grounds for countless species.

    They act as natural barriers, protecting coastlines from storms and erosion, and they sustain fisheries and food security for millions of people worldwide. Reefs also fuel local economies through tourism, diving, and recreation, while inspiring scientific discovery and cultural heritage.

    In short, coral reefs are a foundation of marine biodiversity, coastal protection, and human well-being — making them one of Earth’s most valuable ecosystems.

    """)

    st.info("An estimated **25% of all marine life**, including over 4,000 species of fish, are dependent on coral reefs at some point in their life cycle. **- *U.S. Environmental Protection Agency***")

    st.markdown("""
    ## The Bleaching Crisis

    However, coral reefs around the world have been significantly affected by the rise of global temperatures, changes in the climate, and general pollution of the environment and our oceans—undergoing a transformation known as **coral bleaching**.

    Coral bleaching occurs when corals become stressed by changes in their environment, most commonly:
    -  **Elevated sea temperatures**
    -  **Increased UV radiation**
    -  **Poor water quality and pollution**

    During bleaching, corals become transparent—revealing their white skeletons. While bleached corals are still alive, they are significantly weakened and more vulnerable to starvation, disease, and even death.
    """)

    st.info(" **The Ripple Effect**: When reefs die, fish populations decline, marine food webs collapse, coastal communities lose tourism income, and natural storm protection weakens.")

    st.markdown("""
    ## Global Climate Events Timeline""")

    st.markdown("\n")

    with st.container():
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

    # Fix info box text visibility - black for both themes and increase font size
    st.markdown('<style>.stAlert > div { color: black !important; font-size: 20px !important; } .stAlert .stMarkdown p { font-size: 20px !important; } .stAlert div[data-testid="stMarkdownContainer"] p { font-size: 20px !important; }</style>', unsafe_allow_html=True)

    st.divider()

    # Viz 1
    st.markdown("## Coral Bleaching Over The Years")

    st.markdown("\n")

    with st.container():
        with st.spinner("Loading bleaching visualization..."):
            fig = create_bleaching_heatmap()
            st.plotly_chart(fig)

        st.markdown("""
        📊 **What it shows:**
        A timeline of bleaching events across global reef locations since 2000, highlighting peaks in mass bleaching years.

        🔎 **Meaning:**
        This visualization communicates the alarming trend — bleaching is no longer rare. It's happening more frequently and with greater intensity, linked to global temperature rise. This chart also highlights the geographic hotspots, such as the Caribbean, Great Barrier Reef, and Indo-Pacific. It underlines that bleaching is not an isolated issue — it's a global climate crisis.
        """)

    st.divider()



    # Viz 3
    st.markdown("## Coral Bleaching and Environmental Correlation")

    st.markdown("\n")

    with st.container():
        with st.spinner("Loading environmental correlation dashboard..."):
            fig = create_bleaching_dashboard()
            st.plotly_chart(fig)

        st.markdown("""
        📊 **What it shows:**
        Correlation of bleaching with exposure levels, sea temperature, turbidity, and windspeed

        🔎 **Meaning:**
        Temperature rise is the strongest driver, but local conditions like water clarity and wind patterns amplify vulnerability — proving the need for both global and local action.
        """)

    st.divider()

    st.markdown("## From White to Bright: The Journey of Coral Recovery")

    st.markdown("\n")

    st.markdown("""
    Coral reef recovery after bleaching is critical because it restores the health and stability of the ecosystem. When bleaching occurs, corals expel their symbiotic algae, lose color, and become weak, making them more vulnerable to disease and death. Recovery allows corals to regain these algae, resume energy production, and rebuild their structures. This structural complexity is essential to maintain reef stability and prevent long-term degradation. Without recovery, bleached reefs often collapse into algae-dominated systems that cannot regenerate. Successful recovery also strengthens resilience, as corals that bounce back may develop greater tolerance to rising ocean temperatures. Moreover, natural recovery provides a stronger foundation for restoration projects such as coral gardening and transplantation, making conservation strategies more effective. In this way, recovery after bleaching is not just about survival—it is about rebuilding strength and resilience for the future.
    """)

    st.divider()


    # Viz 2
    st.markdown("## Factors Driving Coral Recovery")

    st.markdown("\n")

    with st.container():
        with st.spinner("Loading K-means analysis..."):
            fig = create_kmeans_analysis()
            st.plotly_chart(fig)

        st.markdown("""
        📊 **What it shows:**
        Four key factors driving coral recovery: geographic location, temperature patterns, macroalgal competition, and depth

        🔎 **Meaning:**
        Geographic location dominates recovery patterns, explaining why some reefs are more resilient. Depth offers refuge in deeper waters, while algal competition threatens weakened corals post-bleaching. These insights guide targeted conservation — protecting deeper areas, controlling algal growth, and maintaining water quality can significantly improve recovery success for the 25% of marine life dependent on reefs.
        """)

    st.divider()

    # Viz 4
    st.markdown("## Management Authority Effectiveness")

    st.markdown("\n")

    with st.container():
        with st.spinner("Loading management analysis..."):
            fig = create_management_analysis()
            st.plotly_chart(fig)

        st.markdown("""
        📊 **What it shows:** Recovery rates across different management approaches, with local/regional authorities achieving highest success (40%) and fisheries management close behind (35-40%).

        🔎 **Meaning:** Localized management outperforms broad strategies because it addresses specific reef needs—controlling macroalgae, managing local stressors, and empowering communities. While global climate action remains crucial, these findings suggest that successful coral conservation depends on tailored, community-driven approaches that complement geographic and environmental factors.
        """)

    st.divider()

    # Viz 5
    st.markdown("## Great Barrier Reef Forecast")

    st.markdown("\n")

    with st.container():
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

    🛡️ **How Can We Protect Coral Reefs?**

    - **Tackle Climate Change** – Reduce carbon emissions to limit ocean warming and acidification.
    - **Marine Protected Areas (MPAs)** – Establish and enforce zones where reefs are safe from overfishing and destructive practices.
    - **Sustainable Fishing** – Use reef-friendly practices that protect breeding grounds and maintain balance in marine life.
    - **Reduce Pollution** – Limit agricultural runoff, plastics, and chemicals that stress coral ecosystems.
    - **Reef Restoration** – Support coral nurseries and transplantation projects that help damaged reefs regrow.
    - **Community & Tourism Practices** – Encourage reef-safe tourism (no touching corals, reef-safe sunscreens, waste management).
    - **Education & Awareness** – Empower local communities and global citizens to understand and protect reef ecosystems.
                
    ### A reef without color is a warning, not an ending!
                
    """)

    st.divider()

    st.markdown("## Tools and Tech Used")

    with st.container():
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