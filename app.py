import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# --- 1. SETUP & STYLE OVERRIDE ---
st.set_page_config(page_title="Executive Dashboard", page_icon="📈", layout="wide")

# This CSS fixes the Sidebar Background + The White Text Issue
st.markdown("""
    <style>
        /* Main Background */
        .stApp {
            background-color: #0E1117;
            color: #FFFFFF;
        }
        
        /* SIDEBAR BACKGROUND - THE FIX */
        section[data-testid="stSidebar"] {
            background-color: #111111; /* Pitch Black Sidebar */
            border-right: 1px solid #333;
        }
        
        /* FORCE SIDEBAR TEXT WHITE */
        section[data-testid="stSidebar"] h1, 
        section[data-testid="stSidebar"] h2, 
        section[data-testid="stSidebar"] span, 
        section[data-testid="stSidebar"] div,
        section[data-testid="stSidebar"] label {
            color: #FFFFFF !important;
        }
        
        /* METRIC CARDS */
        .metric-card {
            background-color: #1A1C24;
            border: 1px solid #2D2F3B;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.5);
            margin-bottom: 20px;
        }
        .metric-title {color: #A0A0A0; font-size: 14px; font-weight: 500;}
        .metric-value {color: #FFFFFF; font-size: 32px; font-weight: 700; margin: 4px 0;}
        .metric-delta {font-size: 12px; font-weight: 600;}
        .positive {color: #00FF99;} /* Neon Green */
        .negative {color: #FF4444;}
        
        /* Charts */
        h3 {color: #FFFFFF !important;}
        
        /* Remove Default Padding */
        .block-container {padding-top: 2rem; padding-bottom: 2rem;}
    </style>
""", unsafe_allow_html=True)

# --- 2. SIDEBAR (The Control Center) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=40)
    st.markdown("### **AgencyControl™**")
    
    # These inputs will now be visible against the dark background
    agency_name = st.text_input("Agency Name", "Tallahassee Digital")
    client_name = st.selectbox("Client Portfolio", ["Luxury Estates LLC", "Downtown Dental", "TechStart Inc"])
    
    st.divider()
    st.info(f"Logged in as: **{agency_name} Admin**")

# --- 3. HELPER FUNCTION FOR CARDS ---
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

# --- 4. MAIN DASHBOARD ---
st.title(f"{client_name} Performance")
st.markdown("Real-time cross-channel attribution data.")

# TOP ROW METRICS (Custom HTML Cards)
c1, c2, c3, c4 = st.columns(4)
with c1: display_card("Total Revenue", "$124,500", "12.5%", True)
with c2: display_card("Ad Spend (YTD)", "$14,200", "3.2%", False) # Red means spend went up
with c3: display_card("Qualified Leads", "342", "18.4%", True)
with c4: display_card("ROI Multiplier", "8.4x", "5.1%", True)

# CHART ROW (Using Plotly)
st.markdown("###") # Spacer
col_chart, col_table = st.columns([2, 1])

with col_chart:
    st.markdown("### Revenue Trend (6 Months)")
    # Fancy Gradient Area Chart
    df = pd.DataFrame({'Month': ['Jan','Feb','Mar','Apr','May','Jun'], 'Revenue': [45, 52, 48, 61, 58, 72]})
    fig = px.area(df, x='Month', y='Revenue', template='plotly_dark')
    fig.update_traces(line_color='#00B4D8', fillcolor='rgba(0, 180, 216, 0.3)')
    fig.update_layout(
        height=350, 
        margin=dict(l=20, r=20, t=20, b=20), 
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color="white")
    )
    st.plotly_chart(fig, use_container_width=True)

with col_table:
    st.markdown("### Campaign Efficiency")
    # Clean Data Table
    table_data = pd.DataFrame({
        "Channel": ["Google Ads", "Meta (FB/IG)", "Email", "SEO"],
        "Spend": ["$5.2k", "$3.1k", "$0.4k", "$0.0k"],
        "ROAS": ["4.5x", "3.2x", "12.1x", "∞"]
    })
    st.dataframe(table_data, hide_index=True, use_container_width=True)


#############################################################################


# --- 3. LIVE DATA CONNECTION ---
# Paste your Google Sheet CSV Link below (keep the quotes!)
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSpttGz_PaylwRX_TBmFJNz7ggao9ydhIj9U5VROWDyCXPkYItbo_0K2AcwXlrai1pStc8jY4oI3i4n/pubhtml"

# This loads the data automatically
try:
    df = pd.read_csv(sheet_url)
    agency_name = str(df['Agency_Name'].iloc[0])
    ad_spend = float(df['Ad_Spend'].iloc[0])
    leads = float(df['Leads'].iloc[0])
    revenue = float(df['Revenue'].iloc[0])
except Exception as e:
    st.error(f"❌ Connection Error: {e}")
    st.stop()
