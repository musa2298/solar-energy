import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import RandomForestRegressor

# Page config
st.set_page_config(page_title="Solar Dashboard", layout="wide")

# Header
st.title("☀ Solar Energy Monitoring Dashboard")
st.markdown("Real-time solar performance insights & predictions")

# Sidebar
st.sidebar.header("⚙ Controls")
file = st.sidebar.file_uploader("Upload CSV Data")

if file:
    df = pd.read_csv(file)

    # Metrics (top cards)
    col1, col2, col3 = st.columns(3)

    if "AC_POWER" in df.columns:
        col1.metric("⚡ Avg Power", f"{df['AC_POWER'].mean():.2f} kW")
        col2.metric("🔋 Max Power", f"{df['AC_POWER'].max():.2f} kW")
        col3.metric("📉 Min Power", f"{df['AC_POWER'].min():.2f} kW")

    st.divider()

    # Charts row 1
    c1, c2 = st.columns(2)

    if "AC_POWER" in df.columns:
        fig1 = px.line(df, y="AC_POWER", title="⚡ AC Power Trend")
        c1.plotly_chart(fig1, use_container_width=True)

    if "AMBIENT_TEMPERATURE" in df.columns:
        fig2 = px.line(df, y="AMBIENT_TEMPERATURE", title="🌡 Temperature Trend")
        c2.plotly_chart(fig2, use_container_width=True)

    # Charts row 2
    c3, c4 = st.columns(2)

    if "IRRADIATION" in df.columns and "AC_POWER" in df.columns:
        fig3 = px.scatter(df, x="IRRADIATION", y="AC_POWER",
                          title="☀ Irradiation vs Power")
        c3.plotly_chart(fig3, use_container_width=True)

    if "MODULE_TEMPERATURE" in df.columns:
        fig4 = px.histogram(df, x="MODULE_TEMPERATURE",
                            title="🔥 Module Temperature Distribution")
        c4.plotly_chart(fig4, use_container_width=True)

    st.divider()

    # ML Prediction Section
    st.subheader("🤖 Power Prediction (AI Model)")

    if st.button("Train & Predict"):
        X = df.select_dtypes(include='number').drop(columns=["AC_POWER"], errors='ignore')
        y = df["AC_POWER"]

        model = RandomForestRegressor()
        model.fit(X, y)

        preds = model.predict(X[:10])

        st.success("Model Trained Successfully ✅")
        st.write("🔮 Sample Predictions:", preds)

else:
    st.info("👈 Upload your solar dataset to start dashboard")
