import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from risk_utils import calculate_risk, estimate_waiting_time

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="Transport Overcrowding AI",
    layout="wide"
)

# --------------------------------------------------
# PREMIUM AI UI – GLASSMORPHISM + GRADIENT
# --------------------------------------------------
st.markdown(
    """
    <style>
    /* -------- GLOBAL BACKGROUND -------- */
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: #ffffff;
        font-family: 'Segoe UI', sans-serif;
    }

    /* -------- HEADERS -------- */
    h1, h2, h3 {
        color: #e6f1ff;
        text-shadow: 0 0 6px rgba(0,212,255,0.6);
    }

    .subtitle {
        color: #cfd8dc;
        font-size: 15px;
        margin-bottom: 6px;
    }

    /* -------- INPUT BOXES -------- */
    input, textarea {
        background: rgba(0,0,0,0.45) !important;
        color: white !important;
        border-radius: 10px !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
    }

    /* -------- GLASS METRIC CARDS -------- */
    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(12px);
        padding: 16px;
        border-radius: 16px;
        border: 1px solid rgba(255,255,255,0.18);
        box-shadow: 0 8px 32px rgba(0,0,0,0.4);
        transition: transform 0.2s ease;
    }

    div[data-testid="stMetric"]:hover {
        transform: scale(1.03);
    }

    /* -------- AI GLOW BUTTON -------- */
    .stButton>button {
        background: linear-gradient(90deg, #00d2ff, #3a7bd5);
        color: black;
        font-weight: bold;
        border-radius: 14px;
        padding: 12px;
        border: none;
        box-shadow: 0 0 14px rgba(0,210,255,0.8);
        transition: all 0.25s ease;
    }

    .stButton>button:hover {
        background: linear-gradient(90deg, #3a7bd5, #00d2ff);
        color: white;
        transform: scale(1.05);
        box-shadow: 0 0 22px rgba(0,210,255,1);
    }

    /* -------- ROAD + BUS -------- */
    .road {
        width: 100%;
        height: 42px;
        background: rgba(255,255,255,0.12);
        border-radius: 22px;
        position: relative;
        overflow: hidden;
        margin-top: 8px;
        margin-bottom: 8px;
        border: 1px solid rgba(255,255,255,0.25);
        backdrop-filter: blur(8px);
    }

    .bus {
        font-size: 30px;
        position: absolute;
        top: 5px;
        animation-name: movebus;
        animation-timing-function: ease-out;
        animation-fill-mode: forwards;
        animation-duration: 1.2s;
    }

    @keyframes movebus {
        from { left: 0%; }
        to { left: var(--bus-position); }
    }

    /* -------- PROGRESS BAR -------- */
    div[data-testid="stProgress"] > div > div {
        background: linear-gradient(90deg, #00ffcc, #00d4ff);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Load trained LSTM model
# --------------------------------------------------
model = load_model("lstm_model.keras")

# --------------------------------------------------
# Header
# --------------------------------------------------
st.markdown("## 🚍 AI-Driven Public Transport Overcrowding Prediction")
st.markdown(
    "<div class='subtitle'>Real-time LSTM-based decision support dashboard</div>",
    unsafe_allow_html=True
)
st.markdown("---")

# --------------------------------------------------
# Layout
# --------------------------------------------------
left, center, right = st.columns([1.3, 1.6, 1.3])

# ================= LEFT: INPUT ====================
with left:
    st.subheader("📥 Recent Passenger Load")

    l1 = st.number_input("15 minutes ago", min_value=0, max_value=200, value=0)
    l2 = st.number_input("10 minutes ago", min_value=0, max_value=200, value=0)
    l3 = st.number_input("5 minutes ago", min_value=0, max_value=200, value=0)

    predict = st.button("🔍 Predict Overcrowding", use_container_width=True)

# ================= CENTER: GRAPH ==================
with center:
    st.subheader("📈 Passenger Trend")

    if predict:
        X = np.array([[l1, l2, l3]]) / 200
        X = X.reshape((1, 3, 1))

        with st.spinner("Running AI prediction…"):
            predicted = model.predict(X, verbose=0)[0][0] * 200
            predicted = int(predicted)

        trend_df = pd.DataFrame({
            "Time": ["-15 min", "-10 min", "-5 min", "+10 min"],
            "Passengers": [l1, l2, l3, predicted]
        })

        fig, ax = plt.subplots(figsize=(5.4, 3), facecolor="#000000")
        ax.set_facecolor("#000000")

        ax.plot(
            trend_df["Time"],
            trend_df["Passengers"],
            marker="o",
            linewidth=2,
            color="#00d4ff"
        )

        ax.set_title("Short-Term Passenger Forecast", color="white", fontsize=12)
        ax.set_xlabel("Time Window", color="white")
        ax.set_ylabel("Passengers", color="white")

        ax.tick_params(axis="x", colors="white")
        ax.tick_params(axis="y", colors="white")
        ax.grid(True, color="#444444", linestyle="--", alpha=0.6)

        for i, value in enumerate(trend_df["Passengers"]):
            ax.text(i, value + 1, str(value),
                    color="white", ha="center",
                    fontsize=10, fontweight="bold")

        st.pyplot(fig)
    else:
        st.info("Enter passenger data and click **Predict**")

# ================= RIGHT: OUTPUT ==================
with right:
    st.subheader("📊 Prediction Output")

    if predict:
        level, risk = calculate_risk(predicted)
        wait = estimate_waiting_time(predicted)

        capacity = 50
        utilization = min(predicted / capacity, 1.0)
        bus_position = int(utilization * 85)

        st.metric("Predicted Load", f"{predicted}")
        st.metric("Risk Score", f"{risk:.2f}")
        st.metric("Waiting Time (mins)", f"{wait}")

        st.markdown("**Capacity Utilization (Visual)**")

        st.markdown(
            f"""
            <div class="road">
                <div class="bus" style="--bus-position: {bus_position}%;">🚌</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.progress(utilization)

        if level == "HIGH":
            st.error("🚨 HIGH RISK\nOvercrowding imminent – dispatch additional bus")
        elif level == "MODERATE":
            st.warning("⚠ MODERATE RISK\nPassenger load increasing")
        else:
            st.success("✅ NORMAL\nOperating within capacity")
    else:
        st.info("Results will appear here")

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.caption(
    "ℹ This dashboard simulates real-time passenger monitoring. "
    "An LSTM model predicts near-future load and converts it into actionable risk indicators."
)
