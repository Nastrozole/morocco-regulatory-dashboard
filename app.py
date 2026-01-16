"""
Dashboard d'Intelligence Réglementaire Maroc-MiCA
Analyse comparative complète des cadres réglementaires crypto
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Configuration de la page
st.set_page_config(
    page_title="Intelligence Réglementaire Crypto Maroc-MiCA",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Style AMMC - Couleurs Or et Bleu
st.markdown("""
<style>
    /* Couleurs officielles AMMC */
    :root {
        --ammc-or: #D4AF37;
        --ammc-or-light: #FFD700;
        --ammc-blue: #003366;
        --ammc-blue-light: #0055a4;
        --ammc-green: #006233;
    }
    
    .main-title {
        font-size: 2.8rem;
        font-weight: 700;
        background: linear-gradient(90deg, var(--ammc-or) 0%, var(--ammc-or-light) 50%, var(--ammc-blue) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .section-header {
        background: linear-gradient(90deg, var(--ammc-blue) 0%, var(--ammc-blue-light) 100%);
        color: white;
        padding: 15px 25px;
        border-radius: 10px;
        margin: 2rem 0 1rem 0;
        font-size: 1.4rem;
        font-weight: 600;
    }
    
    .mica-box {
        background: linear-gradient(135deg, var(--ammc-blue) 0%, var(--ammc-blue-light) 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid var(--ammc-or);
        margin: 10px 0;
    }
    
    .morocco-box {
        background: linear-gradient(135deg, var(--ammc-green) 0%, #00a859 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid var(--ammc-or);
        margin: 10px 0;
    }
    
    .comparison-box {
        background: white;
        border: 2px solid var(--ammc-blue);
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 4px 12px rgba(0, 51, 102, 0.1);
    }
    
    .highlight-box {
        background: linear-gradient(135deg, rgba(212, 175, 55, 0.1) 0%, rgba(255, 215, 0, 0.1) 100%);
        border-left: 4px solid var(--ammc-or);
        padding: 15px;
        border-radius: 0 8px 8px 0;
        margin: 15px 0;
    }
    
    .risk-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin: 2px;
    }
    
    .critical { background-color: #dc3545; color: white; }
    .high { background-color: #fd7e14; color: white; }
    .medium { background-color: #ffc107; color: #212529; }
    .low { background-color: #28a745; color: white; }
    .minimal { background-color: #17a2b8; color: white; }
    
    /* Navigation */
    .stButton > button {
        background: linear-gradient(90deg, var(--ammc-or) 0%, var(--ammc-or-light) 100%);
        color: var(--ammc-blue);
        font-weight: 600;
        border: none;
        border-radius: 8px;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #f8f9fa;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: 600;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(90deg, var(--ammc-or) 0%, var(--ammc-or-light) 100%);
        color: var(--ammc-blue);
    }
</style>
""", unsafe_allow_html=True)

class DashboardReglementaireMarocMICA:
    def __init__(self):
        self.charger_donnees()
        self.initialiser_session()
        
    def charger_donnees(self):
        """Charger toutes les données réglementaires"""
        
        # Sources documentaires
        self.sources = {
            'MiCA': 'Règlement (UE) 2023/1114 - Markets in Crypto-Assets',
            'Loi_42_25': 'Projet de Loi 42-25 relative aux actifs numériques',
            'Livre_Blanc': 'Livre Blanc AMMC sur la transformation digitale (2022)',
            'BAM': 'Avis de la Banque Al-Maghrib (Novembre 2021)'
        }
        
        # Cadres réglementaires détaillés
        self.cadres = {
            'MiCA': {
                'nom': 'Règlement MiCA (UE)',
                'statut': 'Actif - Entrée en vigueur 30/12/2024',
                'portee': 'Union Européenne (27 pays)',
                'classification': {
                    'ART': 'Asset-Referenced Tokens - Référencés à des actifs',
                    'EMT': 'E-Money Tokens - Monnaie électronique',
                    'Utility': 'Utility Tokens - Accès à des services'
                },
                'exigences': {
                    'capital_min': '€50,000 - €350,000 selon activité',
                    'agrement': 'Autorisation obligatoire pour CASP',
                    'white_paper': 'Obligatoire pour offres publiques',
                    'surveillance': 'ESMA + autorités nationales'
                }
            },
            'Maroc': {
                'nom': 'Cadre Marocain (Loi 42-25)',
                'statut': 'En développement - Projet de loi',
                'portee': 'Royaume du Maroc',
                'classification': {
                    'actifs_numeriques': 'Définition générale en cours',
                    'tokens': 'Catégories à préciser',
                    'stablecoins': 'Non spécifiquement traités'
                },
                'exigences': {
                    'capital_min': 'À déterminer',
                    'agrement': 'PSAN - Prévision dans loi 42-25',
                    'white_paper': 'Principe de transparence',
                    'surveillance': 'AMMC + BAM coordination'
                }
            }
        }
        
        # Analyse comparative MiCA vs Maroc
        self.comparaison = pd.DataFrame({
            'Aspect': [
                'Base juridique',
                'Classification tokens',
                'Licensing prestataires',
                'Exigences capital',
                'Gouvernance',
                'Protection investisseurs',
                'Surveillance marché',
                'Règles AML/CFT',
                'Traitement stablecoins',
                'Coordination autorités'
            ],
            'MiCA': [9, 10, 9, 8, 9, 9, 8, 10, 10, 9],
            'Maroc': [6, 5, 4, 3, 6, 5, 2, 7, 2, 7],
            'Écart': [3, 5, 5, 5, 3, 4, 6, 3, 8, 2],
            'Priorité': ['Haute', 'Critique', 'Critique', 'Haute', 'Moyenne', 'Haute', 'Critique', 'Moyenne', 'Critique', 'Basse']
        })
        
        # Analyse des crypto-actifs
        self.actifs = {
            'BTC': {
                'nom': 'Bitcoin',
                'type': 'Token de paiement',
                'cap_marché': '$850B',
                'analyse_mica': 'Utility token probable - Exempt si offre privée',
                'analyse_maroc': 'Non régulé - Utilisation courante malgré interdiction BAM',
                'risque_mica': 15,
                'risque_maroc': 70,
                'recommandation': 'Classer comme actif numérique, encadrer les exchanges'
            },
            'ETH': {
                'nom': 'Ethereum',
                'type': 'Token utilitaire',
                'cap_marché': '$350B',
                'analyse_mica': 'Utility token complexe - Gouvernance à analyser',
                'analyse_maroc': 'Non régulé - Risques techniques et de smart contracts',
                'risque_mica': 25,
                'risque_maroc': 65,
                'recommandation': 'Établir règles pour tokens utilitaires complexes'
            },
            'USDT': {
                'nom': 'Tether',
                'type': 'Stablecoin (ART)',
                'cap_marché': '$95B',
                'analyse_mica': 'ART - Licence requise, réserves, white paper approuvé',
                'analyse_maroc': 'Interdit par BAM - Utilisation souterraine détectée',
                'risque_mica': 78,
                'risque_maroc': 95,
                'recommandation': 'Développer cadre stablecoin au lieu d\'interdiction'
            },
            'USDC': {
                'nom': 'USD Coin',
                'type': 'Stablecoin (EMT)',
                'cap_marché': '$32B',
                'analyse_mica': 'EMT - Licence EMI, garantie des fonds',
                'analyse_maroc': 'Interdit par BAM - Pas d\'alternative régulée',
                'risque_mica': 40,
                'risque_maroc': 95,
                'recommandation': 'Autoriser sous licence stricte avec réserves vérifiées'
            }
        }
        
        # Feuille de route pour le Maroc
        self.feuille_route = {
            'Phase 1: Fondations (0-6 mois)': [
                'Adopter la Loi 42-25',
                'Définir les catégories de tokens',
                'Établir exigences PSAN',
                'Former régulateurs sur MiCA',
                'Créer registre des entités'
            ],
            'Phase 2: Implémentation (6-18 mois)': [
                'Mettre en place agrément PSAN',
                'Développer cadre stablecoins',
                'Instaurer surveillance marché',
                'Créer mécanismes protection',
                'Établir règles gouvernance'
            ],
            'Phase 3: Maturation (18-36 mois)': [
                'Instaurer passeport régional',
                'Développer cadre DeFi',
                'Mettre en place fonds garantie',
                'Établir accords coopération',
                'Réviser cadre réglementaire'
            ]
        }
        
        # Calcul des scores
        self.calculer_scores()
    
    def calculer_scores(self):
        """Calculer les scores de maturité"""
        self.score_mica = np.mean(self.comparaison['MiCA']) * 10
        self.score_maroc = np.mean(self.comparaison['Maroc']) * 10
        self.ecart_total = self.score_mica - self.score_maroc
        
        # Scores par catégorie
        self.scores_categories = {
            'Cadre juridique': {'MiCA': 85, 'Maroc': 45},
            'Classification': {'MiCA': 95, 'Maroc': 35},
            'Licensing': {'MiCA': 90, 'Maroc': 40},
            'Protection': {'MiCA': 85, 'Maroc': 35},
            'Conformité': {'MiCA': 92, 'Maroc': 50}
        }
    
    def initialiser_session(self):
        """Initialiser l'état de la session"""
        if 'page' not in st.session_state:
            st.session_state.page = 'accueil'
        if 'onglet' not in st.session_state:
            st.session_state.onglet = 'tableau_bord'
    
    def creer_en_tete(self):
        """Créer l'en-tête du dashboard"""
        col1, col2, col3 = st.columns([3, 1, 1])
        
        with col1:
            st.markdown('<h1 class="main-title">🇲🇦 Intelligence Réglementaire Maroc-MiCA</h1>', unsafe_allow_html=True)
            st.markdown('**Analyse comparative MiCA (UE) vs Cadre Marocain (Loi 42-25)**')
        
        with col2:
            aujourdhui = datetime.now().strftime("%d/%m/%Y")
            st.metric("Date", aujourdhui)
        
        with col3:
            jours_mica = (datetime(2024, 12, 30) - datetime.now()).days
            st.metric("Jours avant MiCA", jours_mica)
        
        st.markdown("---")
    
    def creer_sidebar(self):
        """Créer la barre latérale"""
        with st.sidebar:
            # Logo AMMC
            st.markdown("""
            <div style="text-align: center; padding: 20px 0;">
                <div style="font-size: 2.5rem; color: #D4AF37;">🇲🇦</div>
                <h3 style="color: #D4AF37; margin: 5px 0;">AMMC</h3>
                <p style="color: #666; font-size: 0.9rem;">
                    Intelligence Réglementaire
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Navigation
            st.markdown("### 📚 Navigation")
            
            pages = [
                ('accueil', '🏠 Tableau de Bord'),
                ('comparaison', '⚖️ Analyse Comparative'),
                ('actifs', '💰 Actifs Crypto'),
                ('details_mica', '🇪🇺 Détails MiCA'),
                ('details_maroc', '🇲🇦 Cadre Marocain'),
                ('roadmap', '🗺️ Feuille de Route')
            ]
            
            for page_id, page_label in pages:
                if st.button(page_label, key=f"nav_{page_id}", use_container_width=True):
                    st.session_state.page = page_id
            
            st.markdown("---")
            
            # Filtres
            st.markdown("### 🔍 Filtres")
            filtre_priorite = st.multiselect(
                "Priorité",
                ['Critique', 'Haute', 'Moyenne', 'Basse'],
                default=['Critique', 'Haute']
            )
            
            st.markdown("---")
            
            # Métriques
            st.markdown("### 📊 Métriques")
            st.metric("Maturité MiCA", f"{self.score_mica:.1f}%")
            st.metric("Maturité Maroc", f"{self.score_maroc:.1f}%")
            st.metric("Écart total", f"{self.ecart_total:.1f} points")
            
            st.markdown("---")
            
            if st.button("🔄 Actualiser", use_container_width=True):
                st.rerun()
    
    def page_accueil(self):
        """Page d'accueil"""
        st.markdown('<div class="section-header">📊 TABLEAU DE BORD SYNTHÉTIQUE</div>', unsafe_allow_html=True)
        
        # Métriques principales
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Maturité MiCA", f"{self.score_mica:.1f}%", "Niveau maximal")
        
        with col2:
            st.metric("Maturité Maroc", f"{self.score_maroc:.1f}%", f"+{self.ecart_total:.1f}% nécessaire")
        
        with col3:
            actifs_critiques = sum(1 for a in self.actifs.values() if a['risque_maroc'] >= 80)
            st.metric("Actifs critiques", f"{actifs_critiques}/{len(self.actifs)}")
        
        with col4:
            jours_mica = (datetime(2024, 12, 30) - datetime.now()).days
            st.metric("Jours avant MiCA", jours_mica, delta="-30", delta_color="off")
        
        # Présentation cadres
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.markdown("""
            <div class="mica-box">
                <h4>🇪🇺 Règlement MiCA (UE)</h4>
                <p><strong>Date:</strong> 30/12/2024</p>
                <p><strong>Statut:</strong> Actif</p>
                <p><strong>Portée:</strong> 27 pays UE</p>
                <p><strong>Objectif:</strong> Cadre harmonisé complet</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col_b:
            st.markdown("""
            <div class="morocco-box">
                <h4>🇲🇦 Cadre Marocain</h4>
                <p><strong>Documents:</strong> Loi 42-25, Livre Blanc</p>
                <p><strong>Statut:</strong> En développement</p>
                <p><strong>Autorités:</strong> AMMC, BAM, Finances</p>
                <p><strong>Approche:</strong> Progressive</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Graphique maturité
        st.markdown('<div class="section-header">📈 MATURITÉ PAR CATÉGORIE</div>', unsafe_allow_html=True)
        
        df_categories = pd.DataFrame([
            {'Catégorie': cat, 'MiCA': scores['MiCA'], 'Maroc': scores['Maroc']}
            for cat, scores in self.scores_categories.items()
        ])
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=df_categories['Catégorie'],
            y=df_categories['MiCA'],
            name='MiCA',
            marker_color='#003366',
            text=df_categories['MiCA'].round(1),
            textposition='auto'
        ))
        
        fig.add_trace(go.Bar(
            x=df_categories['Catégorie'],
            y=df_categories['Maroc'],
            name='Maroc',
            marker_color='#D4AF37',
            text=df_categories['Maroc'].round(1),
            textposition='auto'
        ))
        
        fig.update_layout(
            barmode='group',
            height=400,
            showlegend=True,
            yaxis_title="Score de maturité (%)",
            yaxis_range=[0, 100]
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Alertes prioritaires
        st.markdown('<div class="section-header">⚠️ ALERTES PRIORITAIRES</div>', unsafe_allow_html=True)
        
        alertes = [
            ("Stablecoins interdits sans cadre alternatif", "Critique", "127B$ de marché, utilisation souterraine"),
            ("Pas de surveillance marché", "Critique", "Risque manipulation et fraude"),
            ("Exigences capital non définies", "Haute", "Impossible d'agréer PSAN"),
            ("Classification imprécise", "Haute", "Tokens non classables")
        ]
        
        for alerte, niveau, description in alertes:
            couleur = {'Critique': '#dc3545', 'Haute': '#fd7e14', 'Moyenne': '#ffc107'}.get(niveau, '#6c757d')
            
            st.markdown(f"""
            <div style="border-left: 4px solid {couleur}; padding: 10px 15px; margin: 10px 0; background: #f8f9fa;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <strong>{alerte}</strong>
                    <span style="background-color: {couleur}; color: white; padding: 2px 8px; border-radius: 12px; font-size: 0.8rem;">
                        {niveau}
                    </span>
                </div>
                <div style="color: #666; font-size: 0.9rem;">{description}</div>
            </div>
            """, unsafe_allow_html=True)
    
    def page_comparaison(self):
        """Page d'analyse comparative"""
        st.markdown('<div class="section-header">⚖️ ANALYSE COMPARATIVE DÉTAILLÉE</div>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="highlight-box">
            <strong>🎯 Objectif:</strong> Comparer 10 aspects réglementaires clés entre MiCA et le cadre marocain.
            Scores de 1 à 10, écarts calculés, priorités identifiées.
        </div>
        """, unsafe_allow_html=True)
        
        # Tableau comparatif
        st.markdown("#### 📊 Tableau Comparatif MiCA vs Maroc")
        
        st.dataframe(
            self.comparaison,
            use_container_width=True,
            column_config={
                "Aspect": "Aspect réglementaire",
                "MiCA": st.column_config.NumberColumn("Score MiCA (1-10)"),
                "Maroc": st.column_config.NumberColumn("Score Maroc (1-10)"),
                "Écart": st.column_config.NumberColumn("Écart"),
                "Priorité": "Priorité action"
            }
        )
        
        # Graphique radar
        st.markdown("#### 📈 Analyse Radar des Performances")
        
        aspects = self.comparaison['Aspect'].tolist()
        scores_mica = self.comparaison['MiCA'].tolist()
        scores_maroc = self.comparaison['Maroc'].tolist()
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=scores_mica + [scores_mica[0]],
            theta=aspects + [aspects[0]],
            fill='toself',
            name='MiCA',
            line_color='#003366',
            fillcolor='rgba(0, 51, 102, 0.3)'
        ))
        
        fig.add_trace(go.Scatterpolar(
            r=scores_maroc + [scores_maroc[0]],
            theta=aspects + [aspects[0]],
            fill='toself',
            name='Maroc',
            line_color='#D4AF37',
            fillcolor='rgba(212, 175, 55, 0.3)'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 10]
                )),
            showlegend=True,
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Analyse par aspect
        st.markdown("#### 🎯 Analyse des Écarts Clés")
        
        aspects_critiques = self.comparaison[self.comparaison['Priorité'].isin(['Critique', 'Haute'])]
        
        for _, row in aspects_critiques.iterrows():
            with st.expander(f"🔴 {row['Aspect']} - Écart: {row['Écart']} (Priorité: {row['Priorité']})"):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("**MiCA:**")
                    if row['Aspect'] == 'Classification tokens':
                        st.markdown("- ART: Asset-Referenced Tokens")
                        st.markdown("- EMT: E-Money Tokens")
                        st.markdown("- Utility Tokens")
                
                with col2:
                    st.markdown("**Maroc:**")
                    if row['Aspect'] == 'Classification tokens':
                        st.markdown("- Catégories à définir")
                        st.markdown("- Définitions générales")
                
                st.markdown("**Recommandation:**")
                if row['Aspect'] == 'Classification tokens':
                    st.markdown("Adopter la classification MiCA avec adaptations locales")
    
    def page_actifs(self):
        """Page d'analyse des actifs"""
        st.markdown('<div class="section-header">💰 ANALYSE DES ACTIFS CRYPTO</div>', unsafe_allow_html=True)
        
        # Sélection d'actif
        actif_selectionne = st.selectbox(
            "Sélectionner un actif",
            options=list(self.actifs.keys()),
            format_func=lambda x: f"{self.actifs[x]['nom']} ({x})",
            key="select_asset"
        )
        
        if actif_selectionne:
            actif = self.actifs[actif_selectionne]
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### 🇪🇺 Analyse sous MiCA")
                st.markdown(f"**Type:** {actif['type']}")
                st.markdown(f"**Capitalisation:** {actif['cap_marché']}")
                st.markdown(f"**Analyse:** {actif['analyse_mica']}")
                st.markdown(f"**Risque réglementaire:** {actif['risque_mica']}/100")
                st.progress(actif['risque_mica']/100)
            
            with col2:
                st.markdown("#### 🇲🇦 Analyse au Maroc")
                st.markdown(f"**Statut actuel:** {actif['analyse_maroc'].split(' - ')[0]}")
                st.markdown(f"**Situation:** {actif['analyse_maroc'].split(' - ')[1] if ' - ' in actif['analyse_maroc'] else actif['analyse_maroc']}")
                st.markdown(f"**Risque réglementaire:** {actif['risque_maroc']}/100")
                
                categorie = self.categoriser_risque(actif['risque_maroc'])
                couleur = self.couleur_risque(actif['risque_maroc'])
                
                st.markdown(f"""
                <div style="background-color: {couleur}; color: white; padding: 8px 12px; border-radius: 8px; text-align: center;">
                    <strong>Catégorie: {categorie}</strong>
                </div>
                """, unsafe_allow_html=True)
            
            # Recommandation
            st.markdown("#### 🎯 Recommandation")
            st.info(actif['recommandation'])
            
            # Comparaison risques
            st.markdown("#### 📊 Comparaison des Risques par Actif")
            
            risques = pd.DataFrame({
                'Actif': [self.actifs[a]['nom'] for a in self.actifs],
                'Risque MiCA': [self.actifs[a]['risque_mica'] for a in self.actifs],
                'Risque Maroc': [self.actifs[a]['risque_maroc'] for a in self.actifs]
            })
            
            fig = go.Figure()
            
            fig.add_trace(go.Bar(
                x=risques['Actif'],
                y=risques['Risque MiCA'],
                name='Risque MiCA',
                marker_color='#003366'
            ))
            
            fig.add_trace(go.Bar(
                x=risques['Actif'],
                y=risques['Risque Maroc'],
                name='Risque Maroc',
                marker_color='#D4AF37'
            ))
            
            fig.update_layout(
                barmode='group',
                height=400,
                yaxis_title="Score de risque (0-100)",
                yaxis_range=[0, 100]
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    def page_details_mica(self):
        """Page détails MiCA"""
        st.markdown('<div class="section-header">🇪🇺 RÈGLEMENT MiCA DÉTAILLÉ</div>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="mica-box">
            <h4>📜 Règlement (UE) 2023/1114 - Markets in Crypto-Assets</h4>
            <p><strong>Date d'adoption:</strong> 31 mai 2023</p>
            <p><strong>Entrée en vigueur:</strong> 30 décembre 2024</p>
            <p><strong>Portée:</strong> 27 États membres UE</p>
            <p><strong>Autorités:</strong> ESMA, EBA, autorités nationales</p>
        </div>
        """, unsafe_allow_html=True)
        
        tabs = st.tabs(["Classification", "CASPs", "Protection", "Surveillance"])
        
        with tabs[0]:
            st.markdown("#### 🏷️ Classification des Tokens")
            
            classification = pd.DataFrame([
                {'Type': 'ART', 'Description': 'Asset-Referenced Tokens', 'Exigences': 'Agrément, capital €350k, réserves'},
                {'Type': 'EMT', 'Description': 'E-Money Tokens', 'Exigences': 'Agrément EMI, garantie fonds'},
                {'Type': 'Utility', 'Description': 'Utility Tokens', 'Exigences': 'White paper notifié'}
            ])
            
            st.dataframe(classification, use_container_width=True)
        
        with tabs[1]:
            st.markdown("#### 🏢 CASPs (Crypto Asset Service Providers)")
            
            casps = pd.DataFrame([
                {'Activité': 'Custodie', 'Capital': '€125,000', 'Exigences': '12 critères'},
                {'Activité': 'Exchange', 'Capital': '€125,000', 'Exigences': '14 critères'},
                {'Activité': 'Placement', 'Capital': '€150,000', 'Exigences': '15 critères'},
                {'Activité': 'Conseil', 'Capital': '€50,000', 'Exigences': '8 critères'}
            ])
            
            st.dataframe(casps, use_container_width=True)
        
        with tabs[2]:
            st.markdown("#### 🛡️ Protection des Investisseurs")
            
            st.markdown("""
            - **White paper obligatoire** pour offres publiques
            - **Droit de rétractation** 14 jours pour particuliers
            - **Informations précontractuelles** standardisées
            - **Règles de publicité** strictes
            - **Obligation de conseil** adapté
            """)
        
        with tabs[3]:
            st.markdown("#### 👁️ Surveillance du Marché")
            
            st.markdown("""
            - **Obligations de reporting** pour CASPs
            - **Pouvoirs d'enquête** étendus
            - **Coopération ESMA-EBA**
            - **Mécanismes contre manipulation**
            - **Transparence transactions**
            """)
    
    def page_details_maroc(self):
        """Page détails cadre marocain"""
        st.markdown('<div class="section-header">🇲🇦 CADRE RÉGLEMENTAIRE MAROCAIN</div>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="morocco-box">
            <h4>📚 Cadre Réglementaire Émergent</h4>
            <p><strong>Loi 42-25:</strong> Projet de loi sur les actifs numériques</p>
            <p><strong>Livre Blanc:</strong> Stratégie transformation digitale AMMC</p>
            <p><strong>Avis BAM:</strong> Position de la Banque Al-Maghrib</p>
            <p><strong>Autorités:</strong> AMMC, BAM, Ministère des Finances</p>
        </div>
        """, unsafe_allow_html=True)
        
        tabs = st.tabs(["Loi 42-25", "Livre Blanc", "BAM", "Coordination"])
        
        with tabs[0]:
            st.markdown("#### 📜 Projet de Loi 42-25")
            
            st.markdown("""
            **Statut:** En examen parlementaire
            
            **Objectifs principaux:**
            1. Définir statut juridique actifs numériques
            2. Établir régime agrément PSAN
            3. Protéger utilisateurs et investisseurs
            4. Prévenir risques systémiques
            
            **Structure prévue:**
            - Titre I: Définitions et champ
            - Titre II: Agrément PSAN
            - Titre III: Règles de conduite
            - Titre IV: Surveillance et sanctions
            """)
        
        with tabs[1]:
            st.markdown("#### 📘 Livre Blanc AMMC (2022)")
            
            st.markdown("""
            **Recommandations pour crypto-actifs:**
            
            1. **Cadre réglementaire adapté**
            2. **Classification des actifs**
            3. **Agrément des intermédiaires**
            4. **Surveillance du marché**
            5. **Éducation des investisseurs**
            
            **Approche:** Progressive et évolutive
            """)
        
        with tabs[2]:
            st.markdown("#### ⚠️ Avis BAM (Novembre 2021)")
            
            st.markdown("""
            **Position actuelle:** Interdiction transactions crypto
            
            **Justifications:**
            1. Risques élevés (volatilité)
            2. Absence cadre réglementaire
            3. Risques blanchiment
            4. Contrôle changes
            
            **Évolution:** Vers un cadre réglementé
            """)
        
        with tabs[3]:
            st.markdown("#### 🤝 Coordination des Autorités")
            
            st.markdown("""
            **AMMC (Autorité Marocaine du Marché des Capitaux):**
            - Supervision marchés capitaux
            - Protection investisseurs
            - Agrément PSAN
            
            **BAM (Banque Al-Maghrib):**
            - Stabilité monétaire
            - Régulation paiements
            - AML/CFT
            
            **Ministère des Finances:**
            - Politique économique
            - Législation fiscale
            - Coordination
            """)
    
    def page_roadmap(self):
        """Page feuille de route"""
        st.markdown('<div class="section-header">🗺️ FEUILLE DE ROUTE POUR LE MAROC</div>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="highlight-box">
            <strong>🏗️ Vision:</strong> Alignement progressif sur standards internationaux
            en tirant parti des enseignements MiCA, adapté aux réalités marocaines.
        </div>
        """, unsafe_allow_html=True)
        
        # Phases de la feuille de route
        phases = list(self.feuille_route.keys())
        
        for phase in phases:
            with st.expander(f"📅 {phase}"):
                for tache in self.feuille_route[phase]:
                    st.markdown(f"• {tache}")
        
        # Timeline Gantt
        st.markdown("#### 📈 Timeline d'Implémentation")
        
        gantt_data = []
        start_date = datetime.now()
        
        phases_duration = {
            'Phase 1: Fondations (0-6 mois)': 180,
            'Phase 2: Implémentation (6-18 mois)': 365,
            'Phase 3: Maturation (18-36 mois)': 545
        }
        
        for phase, duration in phases_duration.items():
            gantt_data.append({
                'Phase': phase,
                'Début': start_date.strftime('%Y-%m-%d'),
                'Fin': (start_date + timedelta(days=duration)).strftime('%Y-%m-%d')
            })
            start_date += timedelta(days=duration)
        
        df_gantt = pd.DataFrame(gantt_data)
        
        fig = px.timeline(
            df_gantt,
            x_start="Début",
            x_end="Fin",
            y="Phase",
            color="Phase",
            color_discrete_map={
                'Phase 1: Fondations (0-6 mois)': '#D4AF37',
                'Phase 2: Implémentation (6-18 mois)': '#003366',
                'Phase 3: Maturation (18-36 mois)': '#006233'
            }
        )
        
        fig.update_layout(
            height=300,
            showlegend=True,
            xaxis_title="Timeline"
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Priorités d'action
        st.markdown("#### 🎯 Priorités d'Action Immédiates")
        
        priorites = [
            ('Finaliser Loi 42-25', 'Critique', 'Parlement, AMMC'),
            ('Développer cadre stablecoins', 'Critique', 'BAM, AMMC'),
            ('Former équipes réglementaires', 'Haute', 'AMMC Academy'),
            ('Établir registre PSAN', 'Haute', 'AMMC IT'),
            ('Lancer consultations', 'Moyenne', 'Communication')
        ]
        
        for priorite, niveau, responsable in priorites:
            col_a, col_b, col_c = st.columns([3, 1, 2])
            with col_a:
                st.markdown(f"**{priorite}**")
            with col_b:
                couleur = {'Critique': '#dc3545', 'Haute': '#fd7e14', 'Moyenne': '#ffc107'}.get(niveau, '#6c757d')
                st.markdown(f"<span style='color: {couleur}; font-weight: bold;'>{niveau}</span>", unsafe_allow_html=True)
            with col_c:
                st.markdown(f"*{responsable}*")
            
            st.markdown("---")
    
    def categoriser_risque(self, score):
        """Catégoriser un score de risque"""
        if score >= 80:
            return 'Critique'
        elif score >= 60:
            return 'Élevé'
        elif score >= 40:
            return 'Moyen'
        elif score >= 20:
            return 'Faible'
        else:
            return 'Minimal'
    
    def couleur_risque(self, score):
        """Retourner la couleur pour un score de risque"""
        if score >= 80:
            return '#dc3545'
        elif score >= 60:
            return '#fd7e14'
        elif score >= 40:
            return '#ffc107'
        elif score >= 20:
            return '#28a745'
        else:
            return '#17a2b8'
    
    def run(self):
        """Exécuter le dashboard"""
        if 'page' not in st.session_state:
            st.session_state.page = 'accueil'
        
        self.creer_en_tete()
        self.creer_sidebar()
        
        pages = {
            'accueil': self.page_accueil,
            'comparaison': self.page_comparaison,
            'actifs': self.page_actifs,
            'details_mica': self.page_details_mica,
            'details_maroc': self.page_details_maroc,
            'roadmap': self.page_roadmap
        }
        
        if st.session_state.page in pages:
            pages[st.session_state.page]()
        
        # Footer
        st.markdown("---")
        st.markdown("""
        <div style="text-align: center; color: #666; font-size: 0.9rem; padding: 20px 0;">
            <p><strong>Dashboard d'Intelligence Réglementaire Maroc-MiCA v3.0</strong></p>
            <p>Sources: MiCA (Règlement UE 2023/1114), Loi 42-25, Livre Blanc AMMC, Directives BAM</p>
        </div>
        """, unsafe_allow_html=True)

# Exécution principale
if __name__ == "__main__":
    dashboard = DashboardReglementaireMarocMICA()
    dashboard.run()
