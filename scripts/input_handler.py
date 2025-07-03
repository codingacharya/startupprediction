import pandas as pd

def clean_input(data: pd.DataFrame) -> pd.DataFrame:
    """Converts Yes/No to 1/0 and ensures correct data types."""
    binary_cols = ["has_technical_founder", "mvp_ready", "has_patents"]

    for col in binary_cols:
        if data[col].iloc[0] in ["Yes", "No"]:
            data[col] = data[col].map({"Yes": 1, "No": 0})

    return data
