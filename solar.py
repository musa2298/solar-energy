import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

st.title("☀ Solar Power Dashboard")

file = st.file_uploader("Upload CSV file")

if file:
    df = pd.read_csv(file)

    st.write(df.head())

    if "AC_POWER" in df.columns:
        st.line_chart(df["AC_POWER"])

        X = df.select_dtypes(include=np.number).drop(columns=["AC_POWER"], errors='ignore')
        y = df["AC_POWER"]

        model = RandomForestRegressor()
        model.fit(X, y)

        pred = model.predict(X[:5])
        st.write("Prediction:", pred)