import streamlit as st
from PIL import Image
import os

# Page config
st.set_page_config(
    page_title="Startup Success Predictor",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# App Header
st.markdown("""
    <style>
        .main-header {
            font-size: 40px;
            font-weight: 700;
            color: #4B8BBE;
        }
        .sub-header {
            font-size: 18px;
            color: #555;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🚀 Startup Success Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Predict startup growth potential using AI/ML techniques based on key business indicators</div>', unsafe_allow_html=True)

# Optional: Show a logo
logo_path = "assets/logo.png"
if os.path.exists(logo_path):
    st.image(logo_path, width=100)

# Sidebar navigation
st.sidebar.title("📂 Navigation")
st.sidebar.info("Use the sidebar to navigate between pages")

st.sidebar.markdown("---")
st.sidebar.markdown("📌 Built with Streamlit")

st.markdown("### 👈 Please select a page from the sidebar to get started.")

# Optional: Welcome animation or feature cards
st.markdown("---")
st.markdown("#### 🔍 What You Can Do:")
st.markdown("""
- **Enter startup details** like team, funding, product stage, and traction.
- **Predict success probability** using a trained ML model.
- **Visualize key insights** like radar charts, IPO/acquisition probabilities, and score explanations.
- **Export reports** and track history of predictions.
""")

# Optional Footer
st.markdown("---")
st.markdown("Made with ❤️ by [Your Name] | [GitHub](https://github.com/your-repo)")

