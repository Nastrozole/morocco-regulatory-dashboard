"""
Dashboard Réglementaire Crypto Maroc-MiCA
Analyse comparative complète des cadres réglementaires
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

# Style AMMC
st.markdown("""
<style>
    /* Couleurs AMMC */
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
    
    /* Améliorations visuelles */
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

class DashboardReglementaire:
    def __init__(self):
        self.charger_donnees()
        
    def charger_donnees(self):
        """Charger les données réglementaires"""
        
        # Cadres réglementaires
        self.cadres = {
            'MiCA': {
                'nom': 'Règlement (UE) 2023/1114 - MiCA',
                'date': '30 décembre 2024',
                'statut': 'Actif',
                'autorite': 'ESMA, EBA, autorités nationales',
                'caracteristiques': [
                    'Classification détaillée des tokens (ART, EMT, Utility)',
                    'Agrément harmonisé des CASP',
                    'Exigences de capital proportionnées',
                    'Passeport européen',
                    'Protection renforcée des investisseurs'
                ]
            },
            'Maroc': {
                'nom': 'Cadre réglementaire marocain (Loi 42-25, Livre Blanc)',
                'date': 'En développement',
                'statut': 'Projet',
                'autorite': 'AMMC, BAM, Ministère des Finances',
                'caracteristiques': [
                    'Projet de loi 42-25 en examen',
                    'Livre Blanc sur la transformation digitale',
                    'Directives BAM sur les crypto-actifs',
                    'Approche progressive et pragmatique'
                ]
            }
        }
        
        # Analyse comparative détaillée
        self.analyse_comparative = pd.DataFrame({
            'Aspect': [
                'Base juridique',
                'Classification des tokens',
                'Licensing des prestataires',
                'Exigences de capital',
                'Gouvernance',
                'Protection des investisseurs',
                'Surveillance du marché',
                'Règles AML/CFT',
                'Traitement des stablecoins',
                'Coordination des autorités'
            ],
            'MiCA': [9, 10, 9, 8, 9, 9, 8, 10, 10, 9],
            'Maroc': [6, 5, 4, 3, 6, 5, 2, 7, 2, 7],
            'Gap': [3, 5, 5, 5, 3, 4, 6, 3, 8, 2],
            'Priorité': ['Haute', 'Critique', 'Critique', 'Haute', 'Moyenne', 'Haute', 'Critique', 'Moyenne', 'Critique', 'Basse']
        })
        
        # Données des crypto-actifs
        self.actifs = {
            'BTC': {
                'nom': 'Bitcoin',
                'type': 'Token de paiement',
                'capit_marché': '850B $',
                'mica_status': 'Utility Token probable',
                'maroc_status': 'Non régulé',
                'risque_mica': 15,
                'risque_maroc': 70,
                'recommandation': 'Classer comme actif numérique, réguler les exchanges'
            },
            'ETH': {
                'nom': 'Ethereum',
                'type': 'Token utilitaire',
                'capit_marché': '350B $',
                'mica_status': 'Utility Token complexe',
                'maroc_status': 'Non régulé',
                'risque_mica': 25,
                'risque_maroc': 65,
                'recommandation': 'Établir des règles pour les tokens utilitaires'
            },
            'USDT': {
                'nom': 'Tether',
                'type': 'Stablecoin',
                'capit_marché': '95B $',
                'mica_status': 'ART - Licence requise',
                'maroc_status': 'Interdit',
                'risque_mica': 78,
                'risque_maroc': 95,
                'recommandation': 'Développer un cadre pour les stablecoins régulés'
            },
            'USDC': {
                'nom': 'USD Coin',
                'type': 'Stablecoin',
                'capit_marché': '32B $',
                'mica_status': 'EMT - Licence requise',
                'maroc_status': 'Interdit',
                'risque_mica': 40,
                'risque_maroc': 95,
                'recommandation': 'Autoriser les stablecoins sous licence stricte'
            },
            'BNB': {
                'nom': 'Binance Coin',
                'type': 'Token d\'exchange',
                'capit_marché': '65B $',
                'mica_status': 'Token de CASP',
                'maroc_status': 'Restreint',
                'risque_mica': 45,
                'risque_maroc': 75,
                'recommandation': 'Exiger l\'agrément des exchanges étrangers'
            }
        }
        
        # Feuille de route pour le Maroc
        self.feuille_route = {
            'Phase 1: Fondations (0-6 mois)': [
                'Adopter la loi 42-25',
                'Définir les catégories de tokens',
                'Établir les exigences de base pour les PSAN',
                'Former les régulateurs sur MiCA',
                'Créer un registre des entités régulées'
            ],
            'Phase 2: Implémentation (6-18 mois)': [
                'Mettre en place le système d\'agrément',
                'Développer le cadre des stablecoins',
                'Instaurer la surveillance du marché',
                'Créer des mécanismes de protection',
                'Établir les règles de gouvernance'
            ],
            'Phase 3: Maturation (18-36 mois)': [
                'Instaurer le passeport régional',
                'Développer le cadre DeFi',
                'Mettre en place un fonds de garantie',
                'Établir des accords de coopération',
                'Réviser et adapter le cadre'
            ]
        }
        
        # Sources documentaires
        self.sources = {
            'MiCA': 'Règlement (UE) 2023/1114 du Parlement Européen',
            'Loi 42-25': 'Projet de loi marocain sur les actifs numériques',
            'Livre Blanc': 'Livre Blanc AMMC sur la transformation digitale (2022)',
            'BAM': 'Avis de la Banque Al-Maghrib sur les crypto-actifs (2021)'
        }
        
        # Calculer les scores de maturité
        self.calculer_scores()
    
    def calculer_scores(self):
        """Calculer les scores de maturité réglementaire"""
        self.score_mica = np.mean(self.analyse_comparative['MiCA']) * 10
        self.score_maroc = np.mean(self.analyse_comparative['Maroc']) * 10
        self.ecart_total = self.score_mica - self.score_maroc
        
        # Scores par catégorie
        categories = {
            'Cadre juridique': ['Base juridique', 'Coordination des autorités'],
            'Classification': ['Classification des tokens'],
            'Licensing': ['Licensing des prestataires', 'Exigences de capital'],
            'Protection': ['Protection des investisseurs', 'Surveillance du marché'],
            'Conformité': ['Gouvernance', 'Règles AML/CFT', 'Traitement des stablecoins']
        }
        
        self.scores_categories = {}
        for cat, aspects in categories.items():
            df_cat = self.analyse_comparative[self.analyse_comparative['Aspect'].isin(aspects)]
            self.scores_categories[cat] = {
                'MiCA': np.mean(df_cat['MiCA']) * 10,
                'Maroc': np.mean(df_cat['Maroc']) * 10
            }
    
    def creer_en_tete(self):
        """Créer l'en-tête du dashboard"""
        col1, col2, col3 = st.columns([3, 1, 1])
        
        with col1:
            st.markdown('<h1 class="main-title">🇲🇦 Intelligence Réglementaire Maroc-MiCA</h1>', unsafe_allow_html=True)
            st.markdown('**Analyse comparative complète des cadres réglementaires crypto**')
        
        with col2:
            aujourdhui = datetime.now().strftime("%d/%m/%Y")
            st.metric("Date", aujourdhui)
        
        with col3:
            jours_mica = (datetime(2024, 12, 30) - datetime.now()).days
            st.metric("Jours avant MiCA", jours_mica)
        
        st.markdown("---")
    
    def creer_sidebar(self):
        """Créer la barre latérale de navigation"""
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
                ('roadmap', '🗺️ Feuille de Route'),
                ('recommandations', '🎯 Recommandations')
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
            
            # Actions
            if st.button("🔄 Actualiser", use_container_width=True):
                st.rerun()
    
    def page_accueil(self):
        """Page d'accueil avec vue d'ensemble"""
        st.markdown('<div class="section-header">📊 VUE D\'ENSEMBLE</div>', unsafe_allow_html=True)
        
        # Métriques principales
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "Maturité MiCA",
                f"{self.score_mica:.1f}%",
                delta="Niveau maximal"
            )
        
        with col2:
            st.metric(
                "Maturité Maroc",
                f"{self.score_maroc:.1f}%",
                delta=f"+{(self.score_mica - self.score_maroc):.1f}% nécessaire"
            )
        
        with col3:
            st.metric(
                "Écart réglementaire",
                f"{self.ecart_total:.1f} points",
                delta_color="inverse"
            )
        
        with col4:
            actifs_risque = sum(1 for a in self.actifs.values() if a['risque_maroc'] >= 60)
            st.metric(
                "Actifs à risque",
                f"{actifs_risque}/{len(self.actifs)}",
                delta_color="inverse"
            )
        
        # Présentation des cadres
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.markdown("""
            <div class="mica-box">
                <h3>🇪🇺 Règlement MiCA</h3>
                <p><strong>Date d'effet :</strong> 30 décembre 2024</p>
                <p><strong>Statut :</strong> ✅ Actif</p>
                <p><strong>Portée :</strong> Union Européenne (27 pays)</p>
                <p><strong>Objectif :</strong> Cadre harmonisé complet</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col_b:
            st.markdown("""
            <div class="morocco-box">
                <h3>🇲🇦 Cadre Marocain</h3>
                <p><strong>Documents :</strong> Loi 42-25, Livre Blanc</p>
                <p><strong>Statut :</strong> 📝 En développement</p>
                <p><strong>Autorités :</strong> AMMC, BAM, Finances</p>
                <p><strong>Approche :</strong> Progressive et pragmatique</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Graphique de maturité
        st.markdown('<div class="section-header">📈 MATURITÉ RÉGLEMENTAIRE PAR CATÉGORIE</div>', unsafe_allow_html=True)
        
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
            ("Stablecoins interdits sans alternative", "Critique", "Les stablecoins représentent 127B$ mais sont interdits"),
            ("Pas de surveillance de marché", "Critique", "Risque de manipulation et fraude"),
            ("Exigences de capital non définies", "Haute", "Impossible d'agréer les PSAN"),
            ("Classification imprécise", "Haute", "Les tokens ne peuvent être régulés sans classification claire")
        ]
        
        for alerte, niveau, description in alertes:
            couleur = {'Critique': '#dc3545', 'Haute': '#fd7e14', 'Moyenne': '#ffc107'}.get(niveau, '#6c757d')
            
            st.markdown(f"""
            <div style="border-left: 4px solid {couleur}; padding: 10px 15px; margin: 10px 0; background: #f8f9fa;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <strong>{alerte}</strong>
                    <span style="background-color: {couleur}; color: white; padding: 2px 8px; border-radius: 12px;">
                        {niveau}
                    </span>
                </div>
                <div style="color: #666; font-size: 0.9rem;">{description}</div>
            </div>
            """, unsafe_allow_html=True)
    
    def page_comparaison(self):
        """Page d'analyse comparative"""
        st.markdown('<div class="section-header">⚖️ ANALYSE COMPARATIVE DÉTAILLÉE</div>', unsafe_allow_html=True)
        
        # Introduction
        st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.1) 0%, rgba(255, 215, 0, 0.1) 100%);
                    border-left: 4px solid #D4AF37; padding: 15px; border-radius: 0 8px 8px 0; margin: 20px 0;">
            <strong>🎯 Objectif :</strong> Cette analyse compare 10 aspects réglementaires clés entre MiCA et 
            le cadre marocain émergent. Chaque aspect est noté de 1 à 10, permettant d'identifier 
            les écarts prioritaires à combler.
        </div>
        """, unsafe_allow_html=True)
        
        # Tableau comparatif interactif
        st.markdown("#### 📊 Tableau Comparatif MiCA vs Maroc")
        
        # Filtrage
        col_filtre1, col_filtre2 = st.columns(2)
        
        with col_filtre1:
            filtres_priorite = st.multiselect(
                "Filtrer par priorité",
                options=['Critique', 'Haute', 'Moyenne', 'Basse'],
                default=['Critique', 'Haute']
            )
        
        with col_filtre2:
            filtres_gap = st.multiselect(
                "Filtrer par écart",
                options=['Grand écart (>5)', 'Écart moyen (3-5)', 'Petit écart (<3)'],
                default=['Grand écart (>5)', 'Écart moyen (3-5)']
            )
        
        # Appliquer les filtres
        df_filtre = self.analyse_comparative.copy()
        
        if filtres_priorite:
            df_filtre = df_filtre[df_filtre['Priorité'].isin(filtres_priorite)]
        
        # Convertir les filtres d'écart
        conditions_ecart = []
        if 'Grand écart (>5)' in filtres_gap:
            conditions_ecart.append(df_filtre['Gap'] > 5)
        if 'Écart moyen (3-5)' in filtres_gap:
            conditions_ecart.append((df_filtre['Gap'] >= 3) & (df_filtre['Gap'] <= 5))
        if 'Petit écart (<3)' in filtres_gap:
            conditions_ecart.append(df_filtre['Gap'] < 3)
        
        if conditions_ecart:
            condition_finale = conditions_ecart[0]
            for cond in conditions_ecart[1:]:
                condition_finale = condition_finale | cond
            df_filtre = df_filtre[condition_finale]
        
        # Afficher le tableau
        st.dataframe(
            df_filtre,
            use_container_width=True,
            column_config={
                "Aspect": st.column_config.TextColumn("Aspect réglementaire", width="large"),
                "MiCA": st.column_config.NumberColumn("Score MiCA (1-10)", width="small"),
                "Maroc": st.column_config.NumberColumn("Score Maroc (1-10)", width="small"),
                "Gap": st.column_config.NumberColumn("Écart", width="small"),
                "Priorité": st.column_config.TextColumn("Priorité", width="small")
            }
        )
        
        # Graphique radar
        st.markdown("#### 📈 Analyse Radar des Performances")
        
        aspects = self.analyse_comparative['Aspect'].tolist()
        scores_mica = self.analyse_comparative['MiCA'].tolist()
        scores_maroc = self.analyse_comparative['Maroc'].tolist()
        
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
        
        # Analyse par catégorie
        st.markdown("#### 🎯 Analyse des Écarts par Catégorie")
        
        categories = {
            'Cadre Juridique': ['Base juridique', 'Coordination des autorités'],
            'Structure': ['Classification des tokens', 'Licensing des prestataires', 'Exigences de capital'],
            'Protection': ['Protection des investisseurs', 'Surveillance du marché'],
            'Conformité': ['Gouvernance', 'Règles AML/CFT', 'Traitement des stablecoins']
        }
        
        for categorie, aspects_cat in categories.items():
            with st.expander(f"📂 {categorie}"):
                df_cat = self.analyse_comparative[self.analyse_comparative['Aspect'].isin(aspects_cat)]
                
                for _, row in df_cat.iterrows():
                    col1, col2, col3 = st.columns([3, 1, 1])
                    
                    with col1:
                        st.markdown(f"**{row['Aspect']}**")
                    
                    with col2:
                        st.markdown(f"**MiCA:** {row['MiCA']}/10")
                    
                    with col3:
                        st.markdown(f"**Maroc:** {row['Maroc']}/10")
                    
                    # Barre de progression pour l'écart
                    progress = (row['Maroc'] / row['MiCA']) * 100 if row['MiCA'] > 0 else 0
                    st.progress(min(progress / 100, 1.0), text=f"Alignement: {progress:.1f}%")
                    
                    st.markdown("---")
    
    def page_actifs(self):
        """Page d'analyse des actifs crypto"""
        st.markdown('<div class="section-header">💰 ANALYSE DES ACTIFS CRYPTO MAJEURS</div>', unsafe_allow_html=True)
        
        # Sélection d'actif
        actif_selectionne = st.selectbox(
            "Sélectionner un actif pour analyse détaillée",
            options=list(self.actifs.keys()),
            format_func=lambda x: f"{self.actifs[x]['nom']} ({x})",
            key="select_asset"
        )
        
        if actif_selectionne:
            actif = self.actifs[actif_selectionne]
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                # Analyse MiCA
                st.markdown("#### 🇪🇺 Analyse sous MiCA")
                st.markdown(f"**Type:** {actif['type']}")
                st.markdown(f"**Classification:** {actif['mica_status']}")
                st.markdown(f"**Capitalisation:** {actif['capit_marché']}")
                
                # Score de risque MiCA
                st.markdown(f"**Risque réglementaire MiCA:** {actif['risque_mica']}/100")
                st.progress(actif['risque_mica']/100, 
                          text=self.categoriser_risque(actif['risque_mica']))
            
            with col2:
                # Analyse Maroc
                st.markdown("#### 🇲🇦 Analyse au Maroc")
                st.markdown(f"**Statut actuel:** {actif['maroc_status']}")
                
                # Score de risque Maroc
                st.markdown(f"**Risque réglementaire Maroc:** {actif['risque_maroc']}/100")
                categorie = self.categoriser_risque(actif['risque_maroc'])
                couleur = self.couleur_risque(actif['risque_maroc'])
                
                st.markdown(f"""
                <div style="background-color: {couleur}; color: white; padding: 8px 12px; 
                          border-radius: 8px; text-align: center; margin: 10px 0;">
                    <strong>Catégorie: {categorie}</strong>
                </div>
                """, unsafe_allow_html=True)
            
            # Recommandation
            st.markdown("#### 🎯 Recommandation pour le Maroc")
            st.markdown(f"**{actif['recommandation']}**")
            
            # Comparaison des risques
            st.markdown("#### 📊 Comparaison des Risques")
            
            risques = pd.DataFrame({
                'Actif': [self.actifs[a]['nom'] for a in self.actifs],
                'Risque MiCA': [self.actifs[a]['risque_mica'] for a in self.actifs],
                'Risque Maroc': [self.actifs[a]['risque_maroc'] for a in self.actifs],
                'Écart': [self.actifs[a]['risque_maroc'] - self.actifs[a]['risque_mica'] for a in self.actifs]
            })
            
            fig = go.Figure()
            
            fig.add_trace(go.Bar(
                x=risques['Actif'],
                y=risques['Risque MiCA'],
                name='Risque MiCA',
                marker_color='#003366',
                text=risques['Risque MiCA'],
                textposition='auto'
            ))
            
            fig.add_trace(go.Bar(
                x=risques['Actif'],
                y=risques['Risque Maroc'],
                name='Risque Maroc',
                marker_color='#D4AF37',
                text=risques['Risque Maroc'],
                textposition='auto'
            ))
            
            fig.update_layout(
                barmode='group',
                height=400,
                yaxis_title="Score de risque (0-100)",
                yaxis_range=[0, 100]
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    def page_roadmap(self):
        """Page de feuille de route"""
        st.markdown('<div class="section-header">🗺️ FEUILLE DE ROUTE POUR LE MAROC</div>', unsafe_allow_html=True)
        
        # Introduction
        st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(0, 51, 102, 0.1) 0%, rgba(0, 85, 164, 0.1) 100%);
                    border-left: 4px solid #003366; padding: 15px; border-radius: 0 8px 8px 0; margin: 20px 0;">
            <strong>🏗️ Objectif :</strong> Cette feuille de route propose une approche progressive pour 
            aligner le cadre réglementaire marocain sur les standards internationaux, en tirant parti 
            des enseignements de MiCA tout en adaptant aux spécificités locales.
        </div>
        """, unsafe_allow_html=True)
        
# Dashboard d'Intelligence Réglementaire Maroc-MiCA

## 🇲🇦 Analyse Comparative des Cadres Réglementaires Crypto

Ce dashboard fournit une analyse comparative complète entre le règlement MiCA de l'UE et le cadre réglementaire émergent du Maroc (Loi 42-25, Livre Blanc, directives BAM).

## Fonctionnalités Principales

### 📊 Tableau de Bord Synthétique
- Scores de maturité réglementaire
- Alertes prioritaires
- Métriques clés en temps réel

### ⚖️ Analyse Comparative Détaillée
- Comparaison de 10 aspects réglementaires
- Visualisation radar des écarts
- Filtrage par priorité et écart

### 💰 Analyse des Actifs Crypto
- 5 actifs majeurs analysés
- Scores de risque MiCA vs Maroc
- Recommandations spécifiques par actif

### 🗺️ Feuille de Route Stratégique
- Plan d'implémentation sur 3 ans
- Timeline interactive
- Analyse des risques et mitigations

### 🎯 Recommandations Stratégiques
- Priorités d'action immédiates
- Analyse SWOT complète
- Plan de mise en œuvre

## Déploiement

### Installation locale
```bash
pip install -r requirements.txt
streamlit run dashboard.py
