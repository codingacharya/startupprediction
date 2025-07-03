import streamlit as st
import pandas as pd
from fpdf import FPDF
import os

st.set_page_config(page_title="History & Export", layout="centered")
st.title("🗃️ Prediction History & Report Export")

if "input_data" not in st.session_state:
    st.warning("No startup prediction history found.")
    st.stop()

data = st.session_state["input_data"]

st.subheader("🧾 Most Recent Input")
st.dataframe(data)

# === PDF Export ===
if st.button("📤 Export to PDF"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Startup Success Report", ln=True, align="C")
    
    for col, val in data.iloc[0].items():
        pdf.cell(200, 10, txt=f"{col}: {val}", ln=True)

    os.makedirs("exports", exist_ok=True)
    pdf.output("exports/startup_report.pdf")
    st.success("✅ PDF exported to /exports/startup_report.pdf")
