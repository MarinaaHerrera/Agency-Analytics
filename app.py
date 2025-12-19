import streamlit as st
import pandas as pd

# --- PAGE CONFIGURATION (The Tab Title & Icon) ---
st.set_page_config(
    page_title="Agency Analytics Pro",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS (The "Expensive" Look) ---
# This removes the top padding and styles the metric cards
st.markdown("""
    <style>
        /* Main Background */
        .stApp {
            background-color: #0E1117;
            color: #FAFAFA;
        }
        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #262730;
        }
        /* Metric Cards */
        div[data-testid="stMetricValue"] {
            font-size: 28px;
            color: #4CAF50; /* Money Green */
        }
        /* Card Container Styling */
        .css-1r6slb0 {
            background-color: #1E1E1E;
            border: 1px solid #333;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR (White Label Settings) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=50) # Generic Admin Icon
    st.title("Admin Console")
    st.divider()
    
    # Agency Branding Input
    agency_name = st.text_input("Agency Name", "Tallahassee Digital")
    
    # Client Selector (Simulated)
    client = st.selectbox("Select Client Account", 
                          ["Real Estate - Luxury Homes", "Downtown Dental", "Law Firm Specialist"])

# --- MAIN DASHBOARD ---
# Dynamic Title based on input
st.subheader(f"🔒 {agency_name} Client Portal")
st.title(f"Performance Report: {client}")
st.divider()

# --- METRICS ROW 1 ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Total Ad Spend", value="$4,250", delta="-12% (Efficiency)")
with col2:
    st.metric(label="Leads Generated", value="85", delta="+24%")
with col3:
    st.metric(label="Cost Per Lead (CPL)", value="$50.00", delta="-8%")
with col4:
    # ROI Calculation Visualization
    st.metric(label="Estimated Revenue", value="$68,000", delta="+15%")

# --- CHARTS ROW ---
st.markdown("### Campaign Efficiency Breakdown")

# Dummy Data for Charts
chart_data = pd.DataFrame({
    'Day': range(1, 31),
    'Google Ads': [x * 1.2 + 10 for x in range(30)],
    'Meta Ads': [x * 0.8 + 50 for x in range(30)],
    'Organic': [x * 2 + 5 for x in range(30)]
})

c1, c2 = st.columns([2, 1])

with c1:
    st.line_chart(chart_data)

with c2:
    st.write("#### Channel Attribution")
    st.dataframe(pd.DataFrame({
        "Source": ["Google", "Meta", "SEO"],
        "Conv. Rate": ["4.2%", "3.1%", "1.8%"],
        "ROI": ["450%", "320%", "N/A"]
    }), hide_index=True)

# --- FOOTER ---
st.markdown("---")
st.caption(f"Powered by {agency_name} Intelligence Engine • Updated: Just Now")
