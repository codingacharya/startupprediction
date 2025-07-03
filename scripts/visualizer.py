import pandas as pd
import plotly.graph_objects as go

def radar_chart(df: pd.DataFrame, features: list):
    """Returns a Plotly radar chart for selected features."""
    normalized = (df[features] - df[features].min()) / (df[features].max() - df[features].min())

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=normalized.values.flatten(),
        theta=features,
        fill='toself',
        name='Startup'
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True)),
        showlegend=False
    )
    return fig
