import pandas as pd

def add_derived_features(df: pd.DataFrame) -> pd.DataFrame:
    """Adds custom features to input data."""
    df["ltv_cac_ratio"] = df["ltv"] / (df["cac"] + 1)
    df["revenue_per_user"] = df["monthly_revenue_usd"] / (df["monthly_active_users"] + 1)
    return df
