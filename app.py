import streamlit as st
import pandas as pd

# --- 1. BRANDING ---
st.sidebar.header("Agency Admin Panel")
agency_name = st.sidebar.text_input("Enter Agency Name", "TopTier Marketing")
st.sidebar.write(f"dashboard licensed to: **{agency_name}**")

# --- 2. DASHBOARD ---
st.title(f"🏡 {agency_name}: Real Estate Performance")

# --- 3. INPUTS ---
with st.expander("Update Client Data (Agency Use Only)"):
    ad_spend = st.number_input("Total Ad Spend ($)", value=1500)
    leads = st.number_input("Total Leads Generated", value=45)
    houses_sold = st.number_input("Houses Sold", value=2)
    avg_commission = st.number_input("Avg Commission per House ($)", value=8000)

# --- 4. LOGIC ---
commission_generated = houses_sold * avg_commission
roi = (commission_generated - ad_spend) / ad_spend * 100

# --- 5. OUTPUT ---
st.divider()
st.metric(label="💰 Total Commission Generated", value=f"${commission_generated:,.0f}")

col1, col2, col3 = st.columns(3)
col1.metric("Ad Spend", f"${ad_spend:,.0f}")
col2.metric("Net Profit", f"${commission_generated - ad_spend:,.0f}")
col3.metric("ROI %", f"{roi:.1f}%")

st.info(f"✅ For every \$1 you spent on ads, you made **\${(commission_generated/ad_spend):.2f}** back in commissions.")
