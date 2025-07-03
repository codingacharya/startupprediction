import streamlit as st
import pandas as pd

st.set_page_config(page_title="Startup Input Form", layout="centered")

st.title("🚀 Startup Feature Input Form")

with st.form("startup_form"):
    st.subheader("Founders & Team")
    founded_year = st.number_input("Founded Year", 2000, 2025, 2022)
    num_founders = st.slider("Number of Founders", 1, 5, 2)
    has_technical_founder = st.selectbox("Has Technical Founder?", ["Yes", "No"])
    prev_startup_exits = st.number_input("Previous Startup Exits", 0, 10, 0)
    team_experience_yrs = st.number_input("Total Team Experience (Years)", 1, 50, 5)

    st.subheader("Funding & Investors")
    total_funding = st.number_input("Total Funding ($USD)", 0, 100_000_000, 1_000_000, step=50000)
    num_rounds = st.slider("Number of Funding Rounds", 0, 10, 1)
    investor_score = st.slider("Lead Investor Reputation (1-10)", 1, 10, 5)

    st.subheader("Product & Traction")
    industry = st.selectbox("Industry", ["FinTech", "EdTech", "HealthTech", "AgriTech", "AI"])
    product_stage = st.selectbox("Product Stage", ["Idea", "MVP", "Launched", "Scaling"])
    mvp_ready = st.selectbox("MVP Ready?", ["Yes", "No"])
    monthly_revenue = st.number_input("Monthly Revenue ($)", 0, 1_000_000, 1000)
    monthly_users = st.number_input("Monthly Active Users", 0, 1_000_000, 500)
    retention_rate = st.slider("User Retention Rate", 0.0, 1.0, 0.5)
    cac = st.number_input("Customer Acquisition Cost ($)", 0, 5000, 100)
    ltv = st.number_input("Lifetime Value ($)", 0, 50000, 1000)

    st.subheader("Market & Competitive Landscape")
    market_size = st.number_input("Market Size ($)", 1000000, 1_000_000_000, 100_000_000)
    num_competitors = st.slider("Number of Competitors", 0, 50, 5)
    has_patents = st.selectbox("Has Patents?", ["Yes", "No"])
    website_traffic = st.number_input("Monthly Website Traffic", 0, 1_000_000, 10000)

    submitted = st.form_submit_button("Submit & Predict")

    if submitted:
        input_df = pd.DataFrame([{
            "founded_year": founded_year,
            "industry": industry,
            "num_founders": num_founders,
            "has_technical_founder": 1 if has_technical_founder == "Yes" else 0,
            "prev_startup_exits": prev_startup_exits,
            "team_experience_yrs": team_experience_yrs,
            "total_funding_usd": total_funding,
            "num_funding_rounds": num_rounds,
            "lead_investor_reputation": investor_score,
            "mvp_ready": 1 if mvp_ready == "Yes" else 0,
            "monthly_revenue_usd": monthly_revenue,
            "monthly_active_users": monthly_users,
            "retention_rate": retention_rate,
            "cac": cac,
            "ltv": ltv,
            "market_size_usd": market_size,
            "num_competitors": num_competitors,
            "has_patents": 1 if has_patents == "Yes" else 0,
            "product_stage": product_stage,
            "website_traffic": website_traffic
        }])
        st.session_state["input_data"] = input_df
        st.success("✅ Input saved! Go to '2_Prediction_Result' to see results.")
