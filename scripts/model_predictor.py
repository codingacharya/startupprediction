import joblib
import pandas as pd

# Load assets once
model = joblib.load("models/model.pkl")
scaler = joblib.load("models/scaler.pkl")
label_encoders = joblib.load("models/label_encoders.pkl")

def preprocess_input(df: pd.DataFrame) -> pd.DataFrame:
    """Applies label encoding and scaling."""
    # Encode categorical features
    for col in ["industry", "product_stage"]:
        df[col] = label_encoders[col].transform(df[col])
    
    # Scale numerical features
    df_scaled = scaler.transform(df)
    return df_scaled

def predict(df: pd.DataFrame) -> dict:
    """Returns class prediction and probability."""
    X_scaled = preprocess_input(df)
    prediction = model.predict(X_scaled)[0]
    proba = model.predict_proba(X_scaled)[0][1]
    return {
        "success_label": int(prediction),
        "probability": float(proba)
    }
