import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# --- 1. SETUP & STYLE ---
st.set_page_config(page_title="Executive Dashboard", page_icon="📈", layout="wide")

st.markdown("""
    <style>
        .stApp {background-color: #0E1117; color: #FFFFFF;}
        section[data-testid="stSidebar"] {background-color: #111111; border-right: 1px solid #333;}
        section[data-testid="stSidebar"] h1, section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] span, section[data-testid="stSidebar"] div, section[data-testid="stSidebar"] label {color: #FFFFFF !important;}
        .metric-card {background-color: #1A1C24; border: 1px solid #2D2F3B; padding: 20px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.5); margin-bottom: 20px;}
        .metric-title {color: #A0A0A0; font-size: 14px; font-weight: 500;}
        .metric-value {color: #FFFFFF; font-size: 32px; font-weight: 700; margin: 4px 0;}
        .metric-delta {font-size: 12px; font-weight: 600;}
        .positive {color: #00FF99;}
        .negative {color: #FF4444;}
        h3 {color: #FFFFFF !important;}
        .block-container {padding-top: 2rem; padding-bottom: 2rem;}
    </style>
""", unsafe_allow_html=True)

# --- 2. LIVE DATA CONNECTION ---
# 🚨 PASTE YOUR NEW LINK ENDING IN 'output=csv' BELOW 🚨
sheet_url = "https://docs.google.com/spreadsheets/d/1mAyKWlq7KyPw6b3wRKz__LEFddlDz-xVSuWl9mdn6sw/edit?usp=sharing"

try:
    df = pd.read_csv(sheet_url)
    agency_name_data = str(df['Agency_Name'].iloc[0])
    ad_spend_data = float(df['Ad_Spend'].iloc[0])
    leads_data = float(df['Leads'].iloc[0])
    revenue_data = float(df['Revenue'].iloc[0])
except Exception as e:
    # This prevents the app from crashing if the link is wrong
    agency_name_data = "Error Loading Data"
    ad_spend_data = 1000 # Default value so we don't divide by zero
    leads_data = 0
    revenue_data = 0
    st.error(f"⚠️ Connection Issue: {e}")

# --- 3. SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=40)
    st.markdown("### **AgencyControl™**")
    st.info(f"Connected to: **{agency_name_data}**")
    client_name = st.selectbox("Client Portfolio", ["Luxury Estates LLC", "Downtown Dental"])
    st.divider()

# --- 4. DASHBOARD ---
st.title(f"{client_name} Performance")

# --- SAFE ROI CALCULATION ---
if ad_spend_data > 0:
    roi_val = revenue_data / ad_spend_data
else:
    roi_val = 0

# HELPER FUNCTION
def display_card(title, value, delta, is_positive=True):
    color_class = "positive" if is_positive else "negative"
    arrow = "↑" if is_positive else "↓"
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">{title}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-delta {color_class}">
                {arrow} {delta} vs last month
            </div>
        </div>
    """, unsafe_allow_html=True)

# METRICS ROW
c1, c2, c3, c4 = st.columns(4)
with c1: display_card("Total Revenue", f"${revenue_data:,.0f}", "12.5%", True)
with c2: display_card("Ad Spend (YTD)", f"${ad_spend_data:,.0f}", "3.2%", False)
with c3: display_card("Qualified Leads", f"{leads_data:,.0f}", "18.4%", True)
with c4: display_card("ROI Multiplier", f"{roi_val:.1f}x", "5.1%", True)

# CHARTS
st.markdown("###")
col_chart, col_table = st.columns([2, 1])

with col_chart:
    st.markdown("### Revenue Trend")
    chart_df = pd.DataFrame({'Month': ['Jan','Feb','Mar','Apr','May','Jun'], 'Revenue': [45, 52, 48, 61, 58, 72]})
    fig = px.area(chart_df, x='Month', y='Revenue', template='plotly_dark')
    fig.update_traces(line_color='#00B4D8', fillcolor='rgba(0, 180, 216, 0.3)')
    fig.update_layout(height=350, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="white"))
    st.plotly_chart(fig, use_container_width=True)

with col_table:
    st.markdown("### Campaign Efficiency")
    st.dataframe(pd.DataFrame({
        "Channel": ["Google", "Meta", "SEO"],
        "Spend": ["$5.2k", "$3.1k", "$0.0k"],
        "ROAS": ["4.5x", "3.2x", "∞"]
    }), hide_index=True, use_container_width=True)
