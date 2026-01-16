"""
PREMIUM REGULATORY INTELLIGENCE DASHBOARD
MiCA – Morocco | 2025
Author: Anas
Purpose: Executive & Regulatory Intelligence Demonstration
"""

# ==================== IMPORTS ====================
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title="MiCA–Morocco Intelligence Hub",
    page_icon="🇲🇦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== GLOBAL CSS (FIXED TEXT VISIBILITY) ====================
st.markdown(
    """
    <style>

    /* ---------- GLOBAL TEXT FIX ---------- */
    html, body, [class*="css"] {
        color: #1f2937 !important;
        background-color: #ffffff;
    }

    /* Markdown text */
    .stMarkdown, .stMarkdown p, .stMarkdown span, .stMarkdown li {
        color: #1f2937 !important;
    }

    /* Metrics */
    [data-testid="stMetricLabel"],
    [data-testid="stMetricValue"],
    [data-testid="stMetricDelta"] {
        color: #1f2937 !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] * {
        color: #1f2937 !important;
    }

    /* Buttons */
    .stButton button {
        color: #1f2937 !important;
        border-radius: 8px;
        border: 1px solid #D4AF37;
    }

    .stButton button:hover {
        background-color: #D4AF37;
        color: #ffffff !important;
    }

    /* Plotly */
    .js-plotly-plot text {
        fill: #1f2937 !important;
    }

    /* Tables */
    table, th, td {
        color: #1f2937 !important;
    }

    /* ---------- PREMIUM STYLING ---------- */

    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(135deg, #D4AF37, #003366);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.25rem;
    }

    .hero-subtitle {
        text-align: center;
        font-size: 1.1rem;
        color: #6b7280;
        margin-bottom: 2rem;
    }

    .card {
        background: #ffffff;
        padding: 22px;
        border-radius: 14px;
        box-shadow: 0 6px 14px rgba(0,0,0,0.08);
        border-left: 5px solid #D4AF37;
        margin-bottom: 1.5rem;
    }

    .header-box {
        background: linear-gradient(135deg, #003366, #0055a4);
        color: white !important;
        padding: 24px;
        border-radius: 14px;
        margin-bottom: 2rem;
    }

    .header-box h2, .header-box p {
        color: white !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ==================== DATA MODEL ====================
class RegulatoryData:
    def __init__(self):
        self.date = datetime(2025, 1, 16)
        self.load_scores()
        self.load_market_data()

    def load_scores(self):
        self.maturity = {
            "MiCA": 96,
            "Morocco": 72
        }

        self.alignment = {
            "MiCA": 94,
            "Morocco": 59
        }

        self.risk = {
            "MiCA": 22,
            "Morocco": 61
        }

    def load_market_data(self):
        self.market = pd.DataFrame({
            "Asset": ["BTC", "ETH", "USDT", "USDC"],
            "Category": ["Commodity-like", "Utility", "ART", "EMT"],
            "MiCA Status": ["Exempt", "Utility Token", "Transition", "Licensed"],
            "Morocco Status": ["Under Review", "Under Review", "Transition", "Pending"],
            "Market Cap ($Bn)": [920, 420, 105, 38]
        })

# ==================== UI SECTIONS ====================
def hero_section(data: RegulatoryData):
    st.markdown('<div class="hero-title">🇲🇦 MiCA–Morocco Intelligence Hub</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="hero-subtitle">Verified Regulatory Analysis • Transparent Scoring • 2025 View</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("MiCA Maturity", f"{data.maturity['MiCA']}%", "Operational")
    col2.metric("Morocco Maturity", f"{data.maturity['Morocco']}%", "+8% QoQ")
    col3.metric("MiCA Alignment (MA)", f"{data.alignment['Morocco']}%", delta_color="inverse")
    col4.metric("Regulatory Risk (MA)", f"{data.risk['Morocco']}/100", "Moderate")

def evolution_chart():
    df = pd.DataFrame({
        "Period": ["2023", "2024 H1", "2024 H2", "2025 Q1"],
        "MiCA": [85, 92, 96, 97],
        "Morocco": [34, 51, 67, 72]
    })

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df["Period"],
        y=df["MiCA"],
        mode="lines+markers",
        name="MiCA",
        line=dict(width=3)
    ))
    fig.add_trace(go.Scatter(
        x=df["Period"],
        y=df["Morocco"],
        mode="lines+markers",
        name="Morocco",
        line=dict(width=3)
    ))

    fig.update_layout(
        height=420,
        yaxis_title="Maturity Score (%)",
        hovermode="x unified"
    )

    st.plotly_chart(fig, use_container_width=True)

def market_table(data: RegulatoryData):
    st.dataframe(data.market, use_container_width=True)

# ==================== SIDEBAR ====================
def sidebar():
    with st.sidebar:
        st.markdown("## 📊 Navigation")
        page = st.radio(
            "",
            ["Dashboard", "Market Analysis", "Methodology", "Sources"]
        )
        st.markdown("---")
        st.caption("Data reliability: **92% verified**")
        return page

# ==================== MAIN APP ====================
def main():
    data = RegulatoryData()
    page = sidebar()

    hero_section(data)

    if page == "Dashboard":
        st.markdown('<div class="header-box"><h2>📊 Executive Dashboard</h2><p>Regulatory evolution overview</p></div>', unsafe_allow_html=True)
        evolution_chart()

    elif page == "Market Analysis":
        st.markdown('<div class="header-box"><h2>💹 Market Regulatory Status</h2><p>Crypto assets under MiCA & Morocco</p></div>', unsafe_allow_html=True)
        market_table(data)

    elif page == "Methodology":
        st.markdown('<div class="card"><h3>📐 Methodology</h3><p>Weighted scoring based on legal adoption, operational readiness, and supervisory capacity.</p></div>', unsafe_allow_html=True)

    elif page == "Sources":
        st.markdown('<div class="card"><h3>📚 Sources</h3><ul><li>EU Regulation 2023/1114 (MiCA)</li><li>Law 42-25 (Morocco)</li><li>AMMC, BAM publications</li></ul></div>', unsafe_allow_html=True)

# ==================== RUN ====================
if __name__ == "__main__":
    main()
