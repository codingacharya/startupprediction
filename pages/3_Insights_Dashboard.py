import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Insights Dashboard", layout="wide")
st.title("📈 Startup Insights Dashboard")

input_data = st.session_state.get("input_data")

if input_data is None:
    st.warning("Please fill the startup form first.")
    st.stop()

st.subheader("📊 Feature Distribution Radar Chart")

# Normalize features for radar chart
features_to_plot = [
    "team_experience_yrs", "total_funding_usd", "monthly_revenue_usd",
    "monthly_active_users", "retention_rate", "ltv", "website_traffic"
]
normalized = input_data[features_to_plot].copy()
normalized = (normalized - normalized.min()) / (normalized.max() - normalized.min())

import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=normalized.values.flatten(),
    theta=features_to_plot,
    fill='toself',
    name='Startup'
))
fig.update_layout(polar=dict(radialaxis=dict(visible=True)), showlegend=False)
st.plotly_chart(fig, use_container_width=True)

st.subheader("📌 Category Highlights")
st.markdown("""
- Strong **team experience** and **funding** support early growth.
- **Revenue** and **retention** metrics indicate product-market fit.
- Compare with your industry benchmarks for deeper insights.
""")
