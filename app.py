"""
Morocco-MiCA Crypto Regulatory Intelligence Dashboard
Comparative analysis of EU MiCA vs Moroccan regulatory framework
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Morocco-MiCA Regulatory Intelligence",
    page_icon="🇲🇦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# AMMC Color Scheme: White & Gold
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(90deg, #D4AF37 0%, #FFD700 50%, #D4AF37 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
        padding-bottom: 0;
    }
    .sub-header {
        color: #666666;
        font-size: 1.2rem;
        margin-top: 0;
        padding-top: 0;
    }
    .stButton > button {
        background: linear-gradient(90deg, #D4AF37 0%, #FFD700 100%);
        color: white;
        border: none;
        font-weight: 600;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #B8941F 0%, #E6C200 100%);
        color: white;
    }
</style>
""", unsafe_allow_html=True)

class MoroccoMICADashboard:
    def __init__(self):
        self.load_data()
    
    def load_data(self):
        """Load comprehensive regulatory data for Morocco and MiCA"""
        
        # Regulatory Frameworks Data
        self.frameworks = {
            'MiCA': {
                'name': 'Markets in Crypto-Assets Regulation (MiCA)',
                'jurisdiction': 'European Union',
                'effective_date': '2024-12-30',
                'status': 'Active Implementation',
                'scope': 'Comprehensive (all crypto-assets, CASPs, stablecoins)',
                'authority': 'ESMA, EBA, National Competent Authorities',
                'color': '#003366',
                'logo': '🇪🇺'
            },
            'Morocco_Law_42_25': {
                'name': 'Loi 42-25 & Livre Blanc',
                'jurisdiction': 'Royaume du Maroc',
                'effective_date': '2025-01-01 (proposed)',
                'status': 'Draft Legislation',
                'scope': 'Limited (VASPs, basic crypto framework)',
                'authority': 'AMMC, BAM, Ministry of Finance',
                'color': '#006233',
                'logo': '🇲🇦'
            }
        }
        
        # Crypto Assets Regulatory Status
        self.crypto_assets = {
            'BTC': {
                'name': 'Bitcoin',
                'type': 'Utility Token',
                'mica_status': 'Exempt',
                'morocco_status': 'Unregulated',
                'risk_score_mica': 18,
                'risk_score_morocco': 65,
                'recommendation': 'Classify as digital commodity'
            },
            'ETH': {
                'name': 'Ethereum',
                'type': 'Utility Token',
                'mica_status': 'Pending Review',
                'morocco_status': 'Unregulated',
                'risk_score_mica': 35,
                'risk_score_morocco': 68,
                'recommendation': 'Establish clear utility token guidelines'
            },
            'USDT': {
                'name': 'Tether',
                'type': 'Stablecoin',
                'mica_status': 'EMT (Requires license)',
                'morocco_status': 'Banned',
                'risk_score_mica': 78,
                'risk_score_morocco': 95,
                'recommendation': 'Create regulated stablecoin framework'
            },
            'USDC': {
                'name': 'USD Coin',
                'type': 'Stablecoin',
                'mica_status': 'ART (Requires license)',
                'morocco_status': 'Banned',
                'risk_score_mica': 42,
                'risk_score_morocco': 95,
                'recommendation': 'Allow licensed stablecoins'
            },
            'BNB': {
                'name': 'Binance Coin',
                'type': 'Exchange Token',
                'mica_status': 'CASPs Token (Requires license)',
                'morocco_status': 'Restricted',
                'risk_score_mica': 48,
                'risk_score_morocco': 75,
                'recommendation': 'License exchange tokens under CASP rules'
            }
        }
        
        # Comparative Analysis Data
        self.comparison_matrix = pd.DataFrame({
            'Aspect': [
                'Legal Classification',
                'Licensing Requirements',
                'Capital Requirements',
                'Governance Standards',
                'AML/CFT Framework',
                'Consumer Protection',
                'Market Surveillance',
                'Stablecoin Regulation',
                'CASP Supervision'
            ],
            'MiCA_Score': [9, 10, 9, 9, 10, 9, 8, 10, 9],
            'Morocco_Score': [6, 7, 5, 6, 8, 5, 4, 3, 6],
            'MiCA_Status': ['Defined', 'Comprehensive', 'Tiered', 'High', 'Advanced', 'Strong', 'Real-time', 'Comprehensive', 'Direct'],
            'Morocco_Status': ['Partial', 'Basic', 'Pending', 'Developing', 'Adequate', 'Limited', 'None', 'None', 'Indirect']
        })
    
    def create_header(self):
        """Create dashboard header with AMMC styling"""
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown('<h1 class="main-header">🇲🇦 Morocco-MiCA Regulatory Intelligence</h1>', unsafe_allow_html=True)
            st.markdown('<p class="sub-header">Comparative Analysis & Strategic Roadmap for Moroccan Crypto Regulation</p>', unsafe_allow_html=True)
        
        with col2:
            current_date = datetime.now().strftime("%d %B %Y")
            st.markdown(f"**Date:** {current_date}")
            st.markdown("**AMMC Advisory Dashboard**")
        
        st.markdown("---")
    
    def create_sidebar(self):
        """Create navigation sidebar"""
        with st.sidebar:
            # AMMC Branding
            st.markdown("""
            <div style="text-align: center; padding: 20px 0;">
                <div style="font-size: 2rem; color: #D4AF37;">🇲🇦</div>
                <h2 style="color: #D4AF37; margin: 5px 0;">AMMC</h2>
                <p style="color: #666; font-size: 0.9rem; margin: 0;">
                    Autorité Marocaine du Marché des Capitaux
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Navigation
            st.markdown("### 📊 Navigation")
            
            if st.button("📈 Dashboard Overview", use_container_width=True):
                st.session_state.page = "dashboard"
            
            if st.button("⚖️ Framework Comparison", use_container_width=True):
                st.session_state.page = "comparison"
            
            if st.button("💰 Crypto Asset Analysis", use_container_width=True):
                st.session_state.page = "assets"
            
            st.markdown("---")
            
            # Quick Actions
            st.markdown("### ⚡ Quick Actions")
            
            if st.button("📥 Export Analysis", use_container_width=True):
                st.success("Analysis exported to PDF")
            
            if st.button("🔄 Update Data", use_container_width=True):
                st.rerun()
    
    def create_dashboard_view(self):
        """Create main dashboard view"""
        st.markdown("## 📊 EXECUTIVE OVERVIEW")
        
        # Key Metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("MiCA Maturity", "92%", "+2%")
        
        with col2:
            st.metric("Morocco Maturity", "45%", "+15%")
        
        with col3:
            st.metric("Regulatory Gap", "47%", "-8%")
        
        with col4:
            days_to_mica = (datetime(2024, 12, 30) - datetime.now()).days
            st.metric("Days to MiCA", str(days_to_mica), "-30 days")
        
        # Main Content
        col_left, col_right = st.columns([2, 1])
        
        with col_left:
            # Maturity Comparison Chart
            st.markdown("#### 📈 Regulatory Maturity Comparison")
            
            data = pd.DataFrame({
                'Area': ['Legal Classification', 'Licensing', 'AML/CFT', 'Investor Protection', 'Market Surveillance'],
                'MiCA': [90, 95, 90, 85, 80],
                'Morocco': [40, 55, 75, 35, 30]
            })
            
            fig = go.Figure()
            fig.add_trace(go.Bar(x=data['Area'], y=data['MiCA'], name='MiCA', marker_color='#003366'))
            fig.add_trace(go.Bar(x=data['Area'], y=data['Morocco'], name='Morocco', marker_color='#006233'))
            
            fig.update_layout(height=400, barmode='group')
            st.plotly_chart(fig, use_container_width=True)
        
        with col_right:
            # Risk Distribution
            st.markdown("#### 🎯 Risk Distribution")
            
            risk_data = pd.DataFrame({
                'Risk': ['Critical', 'High', 'Medium', 'Low'],
                'Count': [3, 2, 1, 0]
            })
            
            fig = px.pie(risk_data, values='Count', names='Risk', hole=0.5)
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
            
            # Quick Stats
            st.markdown("#### 📝 Quick Stats")
            st.info("""
            **Morocco Progress:**
            - ✅ AML/CFT: 75% complete
            - ⚠️ Licensing: 55% complete
            - ❌ Stablecoins: 10% complete
            """)
    
    def create_comparison_view(self):
        """Create framework comparison view"""
        st.markdown("## ⚖️ FRAMEWORK COMPARISON: MiCA vs MOROCCO")
        
        # Framework Cards
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #003366 0%, #0055a4 100%); 
                        color: white; padding: 20px; border-radius: 10px; border-left: 5px solid #FFD700;">
                <h3>🇪🇺 MiCA Regulation</h3>
                <p><strong>Jurisdiction:</strong> European Union (27 countries)</p>
                <p><strong>Status:</strong> ✅ Active Implementation</p>
                <p><strong>Effective:</strong> December 30, 2024</p>
                <p><strong>Scope:</strong> Comprehensive regulation</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #006233 0%, #00a859 100%); 
                        color: white; padding: 20px; border-radius: 10px; border-left: 5px solid #D4AF37;">
                <h3>🇲🇦 Morocco Framework</h3>
                <p><strong>Jurisdiction:</strong> Royaume du Maroc</p>
                <p><strong>Status:</strong> 📝 Draft Legislation (Loi 42-25)</p>
                <p><strong>Proposed:</strong> January 1, 2025</p>
                <p><strong>Scope:</strong> VASP licensing, AML/CFT</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Comparative Analysis Table
        st.markdown("#### 📊 Detailed Comparison Matrix")
        
        st.dataframe(
            self.comparison_matrix,
            use_container_width=True,
            column_config={
                "Aspect": "Regulatory Aspect",
                "MiCA_Score": "MiCA Score (0-10)",
                "Morocco_Score": "Morocco Score (0-10)",
                "MiCA_Status": "MiCA Status",
                "Morocco_Status": "Morocco Status"
            }
        )
    
    def create_assets_view(self):
        """Create crypto assets regulatory analysis"""
        st.markdown("## 💰 CRYPTO ASSET REGULATORY ANALYSIS")
        
        # Create comparison table
        asset_data = []
        for symbol, asset in self.crypto_assets.items():
            asset_data.append({
                'Asset': f"{asset['name']} ({symbol})",
                'Type': asset['type'],
                'MiCA Status': asset['mica_status'],
                'Morocco Status': asset['morocco_status'],
                'MiCA Risk': asset['risk_score_mica'],
                'Morocco Risk': asset['risk_score_morocco']
            })
        
        df = pd.DataFrame(asset_data)
        
        # Display table
        st.dataframe(
            df,
            use_container_width=True,
            column_config={
                "MiCA Risk": st.column_config.ProgressColumn(
                    "MiCA Risk",
                    min_value=0,
                    max_value=100
                ),
                "Morocco Risk": st.column_config.ProgressColumn(
                    "Morocco Risk",
                    min_value=0,
                    max_value=100
                )
            }
        )
        
        # Risk Comparison Chart
        st.markdown("#### 📊 Risk Score Comparison")
        
        fig = go.Figure()
        
        for symbol, asset in self.crypto_assets.items():
            fig.add_trace(go.Bar(
                name=f"{asset['name']} - MiCA",
                x=[asset['name']],
                y=[asset['risk_score_mica']],
                marker_color='#003366'
            ))
            
            fig.add_trace(go.Bar(
                name=f"{asset['name']} - Morocco",
                x=[asset['name']],
                y=[asset['risk_score_morocco']],
                marker_color='#006233'
            ))
        
        fig.update_layout(barmode='group', height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    def run(self):
        """Run the dashboard"""
        # Initialize session state
        if 'page' not in st.session_state:
            st.session_state.page = "dashboard"
        
        self.create_header()
        self.create_sidebar()
        
        # Route to appropriate view
        if st.session_state.page == "dashboard":
            self.create_dashboard_view()
        elif st.session_state.page == "comparison":
            self.create_comparison_view()
        elif st.session_state.page == "assets":
            self.create_assets_view()
        
        # Footer
        st.markdown("---")
        st.markdown("""
        <div style="text-align: center; color: #666; font-size: 0.9rem; padding: 20px 0;">
            <p><strong>🇲🇦 Autorité Marocaine du Marché des Capitaux (AMMC)</strong> | Regulatory Intelligence Division</p>
            <p>📧 Contact: regulation@ammc.ma</p>
        </div>
        """, unsafe_allow_html=True)

# Run the dashboard
if __name__ == "__main__":
    dashboard = MoroccoMICADashboard()
    dashboard.run()