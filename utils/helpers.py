import pandas as pd

def format_currency(value: float) -> str:
    """Formats a number as currency."""
    return f"${value:,.2f}"

def load_sample_input(path: str = "data/sample_input.csv") -> pd.DataFrame:
    """Loads a sample input CSV file."""
    return pd.read_csv(path)

def map_binary(value: str) -> int:
    """Maps 'Yes'/'No' to 1/0."""
    return 1 if value == "Yes" else 0
