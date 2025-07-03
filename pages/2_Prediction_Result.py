import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(page_title="📊 Startup Success Prediction")

st.title("📊 Prediction Result")
st.write("This page predicts your startup's growth and success potential based on your input.")

# === Load model, scaler, encoders ===
try:
    model = joblib.load("models/model.pkl")
    scaler = joblib.load("models/scaler.pkl")
    label_encoders = joblib.load("models/label_encoders.pkl")
except FileNotFoundError as e:
    st.error(f"❌ Required file missing: {e}")
    st.stop()

# === Load user input from CSV or form submission ===
input_path = "data/sample_input.csv"
if not os.path.exists(input_path):
    st.warning("⚠️ No input data found. Please submit a form first.")
    st.stop()

input_data = pd.read_csv(input_path)

st.subheader("📥 Your Input")
st.write(input_data)

# === Label Encoding (safe) ===
categorical_cols = ['industry', 'location', 'stage']
for col in categorical_cols:
    if col in input_data.columns:
        if col in label_encoders:
            try:
                input_data[col] = label_encoders[col].transform(input_data[col])
            except Exception as e:
                st.warning(f"⚠️ Encoding issue in column `{col}`: {e}")
        else:
            st.warning(f"⚠️ No encoder found for column: {col}")
    else:
        st.warning(f"⚠️ Column `{col}` not in input data")

# === Scale ===
try:
    input_scaled = scaler.transform(input_data)
except Exception as e:
    st.error(f"❌ Scaling failed: {e}")
    st.stop()

# === Predict ===
try:
    prediction = model.predict(input_scaled)
    prediction_proba = model.predict_proba(input_scaled)
except Exception as e:
    st.error(f"❌ Prediction failed: {e}")
    st.stop()

st.subheader("🔮 Prediction Result")
st.success(f"🧠 **Prediction:** {prediction[0]}")

st.subheader("📈 Confidence Score")
proba_df = pd.DataFrame(prediction_proba, columns=model.classes_)
st.bar_chart(proba_df.T)

