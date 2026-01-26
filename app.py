import streamlit as st
import pandas as pd
import altair as alt

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Global VAT Monitor",
    page_icon="🛡️",
    layout="wide"
)

# --- UI HEADER ---
st.title("🛡️ Global VAT Monitor")
st.markdown("**Enterprise Distance Selling & Nexus Threshold Analytics**")
st.divider()

# --- SIDEBAR CONTROLS ---
with st.sidebar:
    st.header("⚙️ Settings")
    region = st.selectbox("Select Region", ["EU (OSS Rules)", "US (Nexus Rules)"])
    st.info("💡 **Note:** Since July 2021, the EU Distance Selling Threshold is unified at **€10,000**.")

# --- MOCK DATA ENGINE ---
def get_mock_data():
    """Generates realistic sales data for testing."""
    return pd.DataFrame({
        "Country": ["Germany", "France", "Austria", "Spain", "Italy", "Poland", "Netherlands", "Belgium"],
        "Sales_EUR": [12500, 8200, 15000, 9500, 26000, 4000, 11000, 300]
    })

# --- MAIN UPLOADER ---
# Checks for file, otherwise loads mock data
uploaded_file = st.file_uploader("Upload Sales CSV (Columns: Country, Sales_EUR)", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Error reading CSV: {e}")
        df = get_mock_data()
else:
    st.warning("⚠️ No file uploaded. Using **Demo Data**.")
    df = get_mock_data()

# --- CORE LOGIC ---
# 1. Group data
if 'Country' in df.columns and 'Sales_EUR' in df.columns:
    summary = df.groupby("Country")["Sales_EUR"].sum().reset_index()
else:
    st.error("CSV must contain 'Country' and 'Sales_EUR' columns.")
    st.stop()

THRESHOLD_LIMIT = 10000

# --- METRICS SECTION ---
total_sales = summary["Sales_EUR"].sum()
risky_markets = summary[summary["Sales_EUR"] >= THRESHOLD_LIMIT].shape[0]

st.subheader("📊 Executive Summary")
m1, m2, m3 = st.columns(3)
m1.metric("Total EU Revenue", f"€{total_sales:,.2f}")
m2.metric("Markets over Threshold", f"{risky_markets}")
m3.metric("EU Threshold Limit", "€10,000")

# --- ALERT SYSTEM ---
st.divider()
st.subheader("🚨 VAT Registration Status")

# Display status alerts
for index, row in summary.iterrows():
    country = row['Country']
    total = row['Sales_EUR']
    
    if total >= THRESHOLD_LIMIT:
        st.error(f"🔴 **{country}**: €{total:,.2f} - LIMIT EXCEEDED! Immediate VAT Registration Required.")
    elif total >= (THRESHOLD_LIMIT * 0.8):
        st.warning(f"🟡 **{country}**: €{total:,.2f} - Approaching Limit (80% used).")
    else:
        st.success(f"🟢 **{country}**: €{total:,.2f} - Safe.")

# --- VISUALIZATION (FIXED) ---
st.divider()
st.subheader("📈 Revenue vs Threshold Analysis")

# 1. The Base Chart (Data)
base = alt.Chart(summary).encode(
    x=alt.X('Country', sort='-y'),
    y=alt.Y('Sales_EUR', title='Total Sales (€)'),
    tooltip=['Country', 'Sales_EUR']
)

# 2. The Bars (with Conditional Color)
bars = base.mark_bar().encode(
    color=alt.condition(
        alt.datum.Sales_EUR >= THRESHOLD_LIMIT,
        alt.value('#FF4B4B'),  # Red for danger
        alt.value('#00C853')   # Green for safe
    )
)

# 3. The Threshold Line (Red Dashed Line)
rule = alt.Chart(pd.DataFrame({'y': [THRESHOLD_LIMIT]})).mark_rule(color='white', strokeDash=[5, 5]).encode(y='y')

# 4. Combine properly using layers
final_chart = (bars + rule).properties(
    height=400,
    title="Sales per Country (Red = Over Limit)"
)

st.altair_chart(final_chart, use_container_width=True)