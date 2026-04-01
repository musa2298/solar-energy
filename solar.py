# pro_dashboard.py
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
regions = st.sidebar.multiselect(
    "Select Region(s)",
    options=["North", "South", "East", "West"],
    default=["North", "South", "East", "West"]
)

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
data = data[data["Region"].isin(regions)]

# --- KPIs ---
total_energy = data["Energy Produced (kWh)"].sum()
avg_energy = data["Energy Produced (kWh)"].mean()
total_revenue = data["Revenue ($)"].sum()

st.markdown("<h2 style='text-align: center;'>Spice Solar Energy Dashboard</h2>", unsafe_allow_html=True)
st.markdown("---")

col1, col2, col3 = st.columns(3)
col1.metric("Total Energy Produced", f"{total_energy:,} kWh", delta=f"{total_energy - 40000:,} kWh")
col2.metric("Average Energy Produced", f"{avg_energy:.2f} kWh", delta=f"{avg_energy - 3000:.2f} kWh")
col3.metric("Total Revenue", f"${total_revenue:,}", delta=f"${total_revenue - 30000:,}")

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
fig_energy.update_layout(
    plot_bgcolor="#f9f9f9",
    paper_bgcolor="#f9f9f9",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
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
fig_revenue.update_layout(
    plot_bgcolor="#f9f9f9",
    paper_bgcolor="#f9f9f9"
)
st.plotly_chart(fig_revenue, use_container_width=True)

# --- Data Table ---
st.subheader("Detailed Data")
st.dataframe(data.reset_index(drop=True))

# --- Footer ---
st.markdown("""
---
Dashboard created with **Streamlit** | Demo Version
""")
