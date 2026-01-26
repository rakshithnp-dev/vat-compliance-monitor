import streamlit as st
import pandas as pd
import altair as alt
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Global VAT Monitor | Enterprise",
    page_icon="🌍",
    layout="wide"
)

# --- SIDEBAR CONFIGURATION (The "What-If" Engine) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1055/1055644.png", width=50)
    st.title("⚙️ Compliance Config")
    
    # Dynamic Threshold (What-If Scenario)
    st.markdown("### 🛠️ Scenario Planning")
    threshold_limit = st.slider(
        "Distance Selling Threshold (€)", 
        min_value=0, 
        max_value=50000, 
        value=10000, 
        step=1000,
        help="Adjust this to simulate different regulatory environments."
    )
    
    st.divider()
    
    # Simulated API Status
    st.caption("Status: 🟢 System Online")
    st.caption("Policy Engine: v2.4.1 (EU-OSS)")

# --- MAIN HEADER ---
col1, col2 = st.columns([3, 1])
with col1:
    st.title("🌍 Global VAT Monitor")
    st.markdown("**Enterprise Distance Selling & Nexus Threshold Analytics**")
with col2:
    if st.button("🔄 Refresh Data Source"):
        st.toast("Data successfully refreshed from ERP.", icon="✅")

st.divider()

# --- MOCK DATA ENGINE ---
def get_mock_data():
    return pd.DataFrame({
        "Country": ["Germany", "France", "Austria", "Spain", "Italy", "Poland", "Netherlands", "Belgium"],
        "Sales_EUR": [12500, 8200, 15000, 9500, 26000, 4000, 11000, 300],
        "Transactions": [150, 90, 200, 110, 320, 45, 130, 5],
        "Last_Audit": ["2024-01-15", "2024-01-12", "2024-01-18", "2024-01-10", "2024-01-20", "2024-01-22", "2024-01-19", "2024-01-05"]
    })

# --- DATA LOADING ---
uploaded_file = st.file_uploader("📂 Upload Monthly Sales CSV", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
    except:
        df = get_mock_data()
else:
    st.info("ℹ️ Running in **Demo Mode**. Upload a CSV to analyze real data.")
    df = get_mock_data()

# --- LOGIC ENGINE ---
# Ensure necessary columns exist (Simulating validation)
if 'Country' not in df.columns or 'Sales_EUR' not in df.columns:
    st.error("Invalid CSV Format. Required columns: 'Country', 'Sales_EUR'")
    st.stop()

summary = df.groupby("Country")["Sales_EUR"].sum().reset_index()

# Calculate Metrics
total_sales = summary["Sales_EUR"].sum()
markets_at_risk = summary[summary["Sales_EUR"] >= threshold_limit].shape[0]
approaching_limit = summary[(summary["Sales_EUR"] < threshold_limit) & (summary["Sales_EUR"] >= threshold_limit * 0.8)].shape[0]

# --- TABBED LAYOUT (Professional UX) ---
tab1, tab2, tab3 = st.tabs(["📊 Executive Dashboard", "📋 Detailed Compliance Report", "💾 Data Export"])

with tab1:
    # 1. KPI Cards
    st.subheader("High-Level Overview")
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric("Total EU Revenue", f"€{total_sales:,.2f}", delta="4% vs last month")
    kpi2.metric("Breached Markets", markets_at_risk, delta="CRITICAL", delta_color="inverse")
    kpi3.metric("At-Risk Markets", approaching_limit, delta="Warning", delta_color="off")
    kpi4.metric("Active Threshold", f"€{threshold_limit:,.0f}")

    # 2. Advanced Visuals (Split View)
    st.markdown("---")
    c1, c2 = st.columns([2, 1])
    
    with c1:
        st.subheader("Revenue vs Threshold Analysis")
        # Altair Chart with Dynamic Threshold Line
        base = alt.Chart(summary).encode(x=alt.X('Country', sort='-y'), y='Sales_EUR', tooltip=['Country', 'Sales_EUR'])
        bars = base.mark_bar().encode(
            color=alt.condition(
                alt.datum.Sales_EUR >= threshold_limit,
                alt.value('#FF4B4B'),  # Red
                alt.value('#00C853')   # Green
            )
        )
        rule = alt.Chart(pd.DataFrame({'y': [threshold_limit]})).mark_rule(color='white', strokeDash=[5, 5]).encode(y='y')
        st.altair_chart((bars + rule).interactive(), use_container_width=True)
    
    with c2:
        st.subheader("Risk Distribution")
        # Donut Chart Logic
        risk_counts = pd.DataFrame({
            'Status': ['Breached', 'Safe'],
            'Count': [markets_at_risk, len(summary) - markets_at_risk]
        })
        donut = alt.Chart(risk_counts).mark_arc(innerRadius=50).encode(
            theta='Count',
            color=alt.Color('Status', scale=alt.Scale(domain=['Breached', 'Safe'], range=['#FF4B4B', '#00C853']))
        )
        st.altair_chart(donut, use_container_width=True)

with tab2:
    st.subheader("🚨 Action Required")
    # Intelligent Filtering
    risky_df = summary[summary["Sales_EUR"] >= threshold_limit * 0.8].sort_values("Sales_EUR", ascending=False)
    
    if not risky_df.empty:
        for index, row in risky_df.iterrows():
            country = row['Country']
            amount = row['Sales_EUR']
            pct = (amount / threshold_limit) * 100
            
            if amount >= threshold_limit:
                st.error(f"🔴 **{country}** (€{amount:,.2f}) - {pct:.1f}% of limit. **MANDATORY REGISTRATION**")
            else:
                st.warning(f"🟡 **{country}** (€{amount:,.2f}) - {pct:.1f}% of limit. Monitor closely.")
    else:
        st.success("All markets are currently compliant.")

with tab3:
    st.subheader("💾 Export for Taxually")
    st.write("Generate a standardized CSV report for your tax filing team.")
    
    csv_data = summary.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="⬇️ Download Compliance Report (CSV)",
        data=csv_data,
        file_name="vat_compliance_report.csv",
        mime="text/csv",
        type="primary"
    )