import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# --- 1. SETUP & STYLE OVERRIDE ---
st.set_page_config(page_title="Executive Dashboard", page_icon="📈", layout="wide")

# This CSS hides the default Streamlit bars and creates the "Card" look
st.markdown("""
    <style>
        /* Background Color */
        .stApp {background-color: #0E1117;}
        
        /* The "Expensive" Card Style */
        .metric-card {
            background-color: #1A1C24;
            border: 1px solid #2D2F3B;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
            margin-bottom: 20px;
        }
        .metric-title {color: #9CA3AF; font-size: 14px; font-weight: 500;}
        .metric-value {color: #FFFFFF; font-size: 32px; font-weight: 700; margin: 4px 0;}
        .metric-delta {font-size: 12px; font-weight: 600;}
        .positive {color: #10B981;}
        .negative {color: #EF4444;}
        
        /* Remove Default Streamlit Padding */
        .block-container {padding-top: 2rem; padding-bottom: 2rem;}
    </style>
""", unsafe_allow_html=True)

# --- 2. SIDEBAR (The Control Center) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=40)
    st.markdown("### **AgencyControl™**")
    agency_name = st.text_input("Agency Name", "Tallahassee Digital")
    client_name = st.selectbox("Client Portfolio", ["Luxury Estates LLC", "Downtown Dental", "TechStart Inc"])
    st.divider()
    st.caption(f"Logged in as: **{agency_name} Admin**")

# --- 3. HELPER FUNCTION FOR CARDS ---
def display_card(title, value, delta, is_positive=True):
    color_class = "positive" if is_positive else "negative"
    arrow = "↑" if is_positive else "↓"
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">{title}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-delta {color
