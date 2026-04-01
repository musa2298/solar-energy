# dashboard.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Spice Solar Energy Dashboard", layout="wide")

# --- Sidebar ---
st.sidebar.title("Filters")
region = st.sidebar.selectbox("Select Region", ["All", "North", "South", "East", "West"])
year = st.sidebar.slider("Select Year", 2018, 2026, 2023)

# --- Dummy Data ---
np.random.seed(42)
data = pd.DataFrame({
    "Month": pd.date_range(start=f"{year}-01-01", periods=12, freq="M"),
    "Energy Produced (kWh)": np.random.randint(2000, 5000, 12),
    "Energy Consumed (kWh)": np.random.randint(1500, 4500, 12),
    "Revenue ($)": np.random.randint(1000, 5000, 12),
    "Region": np.random.choice(["North", "South", "East", "West"], 12)
})

# Apply region filter
if region != "All":
    data = data[data["Region"] == region]

# --- KPIs ---
total_energy = data["Energy Produced (kWh)"].sum()
total_revenue = data["Revenue ($)"].sum()
avg_energy = data["Energy Produced (kWh)"].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Total Energy Produced", f"{total_energy:,} kWh")
col2.metric("Average Energy Produced", f"{avg_energy:.2f} kWh")
col3.metric("Total Revenue", f"${total_revenue:,}")

# --- Line Chart ---
fig_energy = px.line(
    data,
    x="Month",
    y=["Energy Produced (kWh)", "Energy Consumed (kWh)"],
    title="Monthly Energy Produced vs Consumed",
    markers=True
)
st.plotly_chart(fig_energy, use_container_width=True)

# --- Bar Chart ---
fig_revenue = px.bar(
    data,
    x="Month",
    y="Revenue ($)",
    title="Monthly Revenue",
    color="Revenue ($)",
    color_continuous_scale="Viridis"
)
st.plotly_chart(fig_revenue, use_container_width=True)

# --- Data Table ---
st.subheader("Detailed Data")
st.dataframe(data)

# --- Footer ---
st.markdown("""
---
Dashboard created with **Streamlit** | Demo Version
""")
