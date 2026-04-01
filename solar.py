import streamlit as st

st.set_page_config(layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
body {
    background-color: #f5f7fb;
}

.main-title {
    font-size: 48px;
    font-weight: 700;
    color: #0b1f3a;
}

.blue-text {
    color: #2E6CF6;
}

.desc {
    color: #5f6b7a;
    font-size: 16px;
    line-height: 1.6;
}

.metric-card {
    background-color: #f9fafc;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.08);
}

.small-title {
    font-size: 12px;
    color: #8a94a6;
    text-transform: uppercase;
}

.metric {
    font-size: 26px;
    font-weight: 700;
}

.green {
    color: green;
}

.btn {
    padding: 15px;
    border-radius: 10px;
    background-color: #ffffff;
    border: 1px solid #e5e7eb;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
col1, col2 = st.columns([6,2])

with col1:
    st.markdown("## ☀️ SPICE Solar Energy Dashboard")
    st.caption("DEVELOPED USING SPICE DATA")

with col2:
    st.button("Overview & Pipeline")
    st.button("Dashboard")

# ---------- MAIN SECTION ----------
left, right = st.columns([2,1])

with left:
    st.markdown('<div class="small-title">PROJECT OVERVIEW</div>', unsafe_allow_html=True)

    st.markdown('<div class="main-title">Solar Production Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-title blue-text">and Prediction</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="desc">
    This project analyzes solar energy production using multiple datasets.
    Visser and Bissell production data were provided by SPICE.
    Additional datasets including weather data, NASA solar radiation data,
    and electricity pool price data were used.
    </div>
    """, unsafe_allow_html=True)

    colA, colB = st.columns(2)

    with colA:
        st.markdown('<div class="btn">• Understand environmental impact on solar production</div>', unsafe_allow_html=True)
        st.markdown('<div class="btn">• Estimate revenue</div>', unsafe_allow_html=True)

    with colB:
        st.markdown('<div class="btn">• Compare solar sites</div>', unsafe_allow_html=True)
        st.markdown('<div class="btn">• Build a machine learning model</div>', unsafe_allow_html=True)

# ---------- RIGHT CARD ----------
with right:
    st.markdown("""
    <div class="metric-card">
        <div class="small-title">PEAK MONTH</div>
        <div class="metric">May</div><br>

        <div class="small-title">MAIN DRIVER</div>
        <div class="metric blue-text">Radiation</div><br>

        <div class="small-title">REVENUE PEAK</div>
        <div class="metric green">Summer</div><br>

        <div class="small-title">MODEL R²</div>
        <div class="metric">0.67</div>
    </div>
    """, unsafe_allow_html=True)
