# dashboard.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- Page Config ---
st.set_page_config(
    page_title="Spice Solar Energy Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Sidebar ---
st.sidebar.title("Filters")
year = st.sidebar.slider("Select Year", 2018, 2026, 2023)
region = st.sidebar.selectbox("Select Region", ["All", "North", "South", "East", "West"])

# --- Dummy Data ---
np.random.seed(42)
months = pd.date_range(start=f"{year}-01-01", periods=12, freq="M")
data = pd.DataFrame({
    "Month": months,
    "Energy Produced (kWh)": np.random.randint(2000, 5000, size=12),
    "Energy Consumed (kWh)": np.random.randint(1500, 4500, size=12),
    "Revenue ($)": np.random.randint(1000, 5000, size=12),
    "Region": np.random.choice(["North", "South", "East", "West"], size=12)
})

# --- Apply Filters ---
if region != "All":
    data = data[data["Region"] == region]

# --- KPIs ---
total_energy = data["Energy Produced (kWh)"].sum()
avg_energy = data["Energy Produced (kWh)"].mean()
total_revenue = data["Revenue ($)"].sum()

col1, col2, col3 = st.columns(3)
col1.metric("Total Energy Produced", f"{total_energy:,} kWh")
col2.metric("Average Energy Produced", f"{avg_energy:.2f} kWh")
col3.metric("Total Revenue", f"${total_revenue:,}")

st.markdown("---")

# --- Line Chart ---
fig_energy = px.line(
    data,
    x="Month",
    y=["Energy Produced (kWh)", "Energy Consumed (kWh)"],
    markers=True,
    labels={"value": "kWh", "variable": "Energy Type"},
    title="Monthly Energy Produced vs Consumed"
)
st.plotly_chart(fig_energy, use_container_width=True)

# --- Bar Chart ---
fig_revenue = px.bar(
    data,
    x="Month",
    y="Revenue ($)",
    color="Revenue ($)",
    color_continuous_scale="Viridis",
    labels={"Revenue ($)": "Revenue ($)"},
    title="Monthly Revenue"
)
st.plotly_chart(fig_revenue, use_container_width=True)

# --- Data Table ---
st.subheader("Detailed Data")
st.dataframe(data)

# --- Footer ---
st.markdown("""
---
Dashboard created with **Streamlit** | latest Version
""")
