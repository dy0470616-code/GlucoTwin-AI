import streamlit as st
import numpy as np
import pandas as pd
from model import run_experiment

st.set_page_config(page_title="GlucoTwin AI Dashboard", layout="wide")

st.title("🩺 GlucoTwin AI: Digital Twin Healthcare Platform")
st.markdown("### Real-Time Glucose Analytics & Prediction")

# Load model and metrics
@st.cache_resource
def load_engine():
    return run_experiment()

model, metrics = load_engine()

# Sidebar: Patient Telemetry
st.sidebar.header("Patient Digital Twin Input")
r1 = st.sidebar.slider("Reading t-4 (mg/dL)", 60, 200, 110)
r2 = st.sidebar.slider("Reading t-3 (mg/dL)", 60, 200, 115)
r3 = st.sidebar.slider("Reading t-2 (mg/dL)", 60, 200, 112)
r4 = st.sidebar.slider("Reading t-1 (mg/dL)", 60, 200, 118)
r5 = st.sidebar.slider("Current Reading t0 (mg/dL)", 60, 200, 125)

col1, col2 = st.columns(2)

with col1:
    st.subheader("🔮 Digital Twin Forecast")
    recent_readings = np.array([r1, r2, r3, r4, r5]).reshape(1, -1)
    prediction = model.predict(recent_readings)[0]
    
    st.metric(label="Predicted Next Glucose Level", value=f"{prediction:.1f} mg/dL")
    
    if prediction > 140:
        st.error("⚠️ High Risk: Hyperglycemia threshold exceeded!")
    elif prediction < 70:
        st.warning("⚠️ High Risk: Hypoglycemia threshold exceeded!")
    else:
        st.success("✅ Normal Glycemic Range")

with col2:
    st.subheader("📊 Empirical Test Performance")
    res_df = pd.DataFrame({
        "Metric": ["MAE (mg/dL)", "RMSE (mg/dL)"],
        "Baseline Model": [metrics["baseline_mae"], metrics["baseline_rmse"]],
        "GlucoTwin ML Model": [metrics["ml_mae"], metrics["ml_rmse"]]
    })
    st.table(res_df)
