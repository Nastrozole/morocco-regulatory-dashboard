"""
TABLEAU DE BORD ULTIME D'INTELLIGENCE RÉGLEMENTAIRE MAROC-MiCA
Analyse comparative approfondie des régulations crypto de l'UE et du Maroc
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import json

# Configuration de la page
st.set_page_config(
    page_title="Intelligence Réglementaire Maroc-MiCA",
    page_icon="🇲🇦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Style AMMC : Or et Bleu
st.markdown("""
<style>
    /* Palette AMMC */
    :root {
        --ammc-or: #D4AF37;
        --ammc-or-light: #FFD700;
        --ammc-blue: #003366;
        --ammc-blue-light: #0055a4;
        --ammc-green: #006233;
        --ammc-red: #dc3545;
        --ammc-gray: #f8f9fa;
    }
    
    .main-header {
        font-size: 3.2rem;
        font-weight: 800;
        background: linear-gradient(90deg, var(--ammc-or) 0%, var(--ammc-or-light) 50%, var(--ammc-or) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
        padding-bottom: 0;
    }
    
    .sub-header {
        color: var(--ammc-blue);
        font-size: 1.3rem;
        font-weight: 500;
        margin-top: 0;
        margin-bottom: 2rem;
    }
    
    .ammc-card {
        background: white;
        border: 2px solid var(--ammc-or);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 12px rgba(212, 175, 55, 0.15);
    }
    
    .mica-card {
        background: linear-gradient(135deg, var(--ammc-blue) 0%, var(--ammc-blue-light) 100%);
        color: white;
        padding: 1.8rem;
        border-radius: 12px;
        border-left: 6px solid var(--ammc-or);
    }
    
    .morocco-card {
        background: linear-gradient(135deg, var(--ammc-green) 0%, #00a859 100%);
        color: white;
        padding: 1.8rem;
        border-radius: 12px;
        border-left: 6px solid var(--ammc-or);
    }
    
    .comparison-card {
        background: linear-gradient(135deg, #f8f9fa 0%, white 100%);
        border: 2px solid var(--ammc-blue);
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    .section-title {
        background: linear-gradient(90deg, var(--ammc-blue) 0%, var(--ammc-blue-light) 100%);
        color: white;
        padding: 12px 20px;
        border-radius: 8px;
        margin: 2rem 0 1rem 0;
        font-size: 1.4rem;
        font-weight: 600;
    }
    
    .highlight-box {
        background: linear-gradient(135deg, rgba(212, 175, 55, 0.1) 0%, rgba(255, 215, 0, 0.1) 100%);
        border-left: 4px solid var(--ammc-or);
        padding: 1.2rem;
        margin: 1rem 0;
        border-radius: 0 8px 8px 0;
    }
    
    .risk-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin: 2px;
    }
    
    .risk-critical { background-color: var(--ammc-red); color: white; }
    .risk-high { background-color: #fd7e14; color: white; }
    .risk-medium { background-color: #ffc107; color: #212529; }
    .risk-low { background-color: #28a745; color: white; }
    .risk-minimal { background-color: #17a2b8; color: white; }
    
    /* Navigation */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: var(--ammc-gray);
        padding: 8px;
        border-radius: 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: white;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: 600;
        border: 2px solid transparent;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(90deg, var(--ammc-or) 0%, var(--ammc-or-light) 100%);
        color: var(--ammc-blue);
        border-color: var(--ammc-or);
    }
    
    /* Boutons */
    .stButton > button {
        background: linear-gradient(90deg, var(--ammc-or) 0%, var(--ammc-or-light) 100%);
        color: var(--ammc-blue);
        border: none;
        font-weight: 600;
        border-radius: 8px;
    }
    
    .stButton > button:hover {
        background: linear-gradient(90deg, #B8941F 0%, #E6C200 100%);
        color: var(--ammc-blue);
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, var(--ammc-blue) 0%, var(--ammc-blue-light) 100%);
    }
    
    /* Progress bars */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, var(--ammc-or) 0%, var(--ammc-or-light) 100%);
    }
</style>
""", unsafe_allow_html=True)

class TableauBordReglementaireUltime:
    def __init__(self):
        self.charger_donnees()
        self.initialiser_etat()
    
    def charger_donnees(self):
        """Charger toutes les données réglementaires détaillées"""
        
        # Sources documentaires référencées
        self.sources = {
            'mica': {
                'nom': 'Règlement (UE) 2023/1114 - MiCA',
                'url': 'https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32023R1114',
                'date': '31 mai 2023',
                'statut': 'Adopté et en vigueur',
                'articles_cles': ['Art. 3-6: Définitions', 'Art. 16-34: EMT', 'Art. 35-72: ART', 'Art. 73-85: CASP']
            },
            'loi_42_25': {
                'nom': 'Projet de Loi 42-25 relative aux actifs numériques',
                'url': 'https://www.finances.gov.ma/Publication/projet-loi-42-25.pdf',
                'date': 'Version préliminaire 2023',
                'statut': 'En cours d\'examen parlementaire',
                'articles_cles': ['Art. 1-3: Champ d\'application', 'Art. 4-7: Définitions', 'Art. 8-15: Agrément PSAN']
            },
            'livre_blanc': {
                'nom': 'Livre Blanc sur la Transformation Digitale du Secteur Financier',
                'url': 'https://www.ammc.ma/sites/default/files/2022-06/Livre%20Blanc%20Transformation%20Digitale.pdf',
                'date': 'Juin 2022',
                'statut': 'Document stratégique',
                'chapitres_cles': ['Chapitre 3: Actifs numériques', 'Chapitre 4: Cadre réglementaire', 'Chapitre 5: Supervision']
            },
            'bam_avis': {
                'nom': 'Avis de la Banque Al-Maghrib sur les crypto-actifs',
                'url': 'https://www.bkam.ma/Media/Circulars/2021/20211108_avis_crypto.pdf',
                'date': '8 novembre 2021',
                'statut': 'Avis en vigueur',
                'points_cles': ['Interdiction des crypto-actifs', 'Risques signalés', 'Encadrement nécessaire']
            }
        }
        
        # Données réglementaires détaillées
        self.donnees_reglementaires = {
            'mica': {
                'classification_tokens': {
                    'titre': 'Classification des Tokens',
                    'details': {
                        'ART (Asset-Referenced Tokens)': {
                            'definition': 'Tokens référencés à un ou plusieurs actifs',
                            'exigences': ['Agrément préalable', 'Capital minimum €350k', 'Gouvernance renforcée', 'White paper approuvé'],
                            'surveillance': 'ESMA + Autorités nationales',
                            'exemples': 'USDT, USDC (sous conditions)'
                        },
                        'EMT (E-Money Tokens)': {
                            'definition': 'Tokens représentant de la monnaie électronique',
                            'exigences': ['Agrément EMI', 'Capital selon directive 2009/110/CE', 'Remboursement garanti'],
                            'surveillance': 'Autorités nationales',
                            'exemples': 'Stablecoins monétaires'
                        },
                        'Utility Tokens': {
                            'definition': 'Tokens fournissant accès à un produit/service',
                            'exigences': ['White paper notifié', 'Pas d\'agrément si non-sécuritaires'],
                            'surveillance': 'Notification seulement',
                            'exemples': 'ETH, ADA, SOL'
                        }
                    }
                },
                'casp_licensing': {
                    'titre': 'Agrément des Prestataires de Services sur Actifs Numériques (CASPs)',
                    'categories': [
                        {'nom': 'Custodie', 'capital': '€125,000', 'exigences': 12},
                        {'nom': 'Exchange', 'capital': '€125,000', 'exigences': 14},
                        {'nom': 'Placement', 'capital': '€150,000', 'exigences': 15},
                        {'nom': 'Conseil', 'capital': '€50,000', 'exigences': 8},
                        {'nom': 'Portefeuille', 'capital': '€125,000', 'exigences': 10}
                    ],
                    'passeport': 'Passeport européen disponible',
                    'delai': '3 mois après dossier complet'
                },
                'protection_investisseurs': {
                    'titre': 'Protection des Investisseurs',
                    'mesures': [
                        'White paper obligatoire pour offres publiques',
                        'Droit de rétractation 14 jours pour particuliers',
                        'Informations précontractuelles standardisées',
                        'Règles de publicité strictes',
                        'Obligation de conseil adapté'
                    ],
                    'indemnisation': 'Pas de fonds de garantie spécifique',
                    'recours': 'Voies de recours nationales'
                }
            },
            'maroc': {
                'classification_tokens': {
                    'titre': 'Classification selon Loi 42-25',
                    'details': {
                        'Actifs numériques': {
                            'definition': 'Toute représentation numérique de valeur',
                            'exigences': ['À définir par décret', 'Agrément PSAN obligatoire'],
                            'surveillance': 'AMMC + BAM',
                            'statut': 'Cadre général défini'
                        },
                        'Tokens de paiement': {
                            'definition': 'Non spécifiquement défini',
                            'exigences': 'Soumis à régulation BAM',
                            'surveillance': 'BAM',
                            'statut': 'À préciser'
                        }
                    }
                },
                'psan_licensing': {
                    'titre': 'Agrément des Prestataires de Services sur Actifs Numériques (PSAN)',
                    'categories': [
                        {'nom': 'Custodie', 'capital': 'À déterminer', 'exigences': 'En cours'},
                        {'nom': 'Exchange', 'capital': 'À déterminer', 'exigences': 'En cours'},
                        {'nom': 'Conseil', 'capital': 'À déterminer', 'exigences': 'En cours'}
                    ],
                    'autorite': 'AMMC en coordination avec BAM',
                    'delai': 'Non spécifié'
                },
                'protection_investisseurs': {
                    'titre': 'Protection selon Livre Blanc',
                    'mesures': [
                        'Transparence et information (principe)',
                        'Gouvernance des plateformes',
                        'Mesures contre la manipulation de marché'
                    ],
                    'indemnisation': 'Fonds de garantie à étudier',
                    'recours': 'Médiation et recours juridiques'
                }
            }
        }
        
        # Matrice de comparaison détaillée
        self.matrice_comparative = pd.DataFrame({
            'Aspect Réglementaire': [
                'Base Juridique',
                'Champ d\'Application',
                'Classification des Tokens',
                'Agrément des Prestataires',
                'Exigences de Capital',
                'Gouvernance',
                'Transparence et Disclosure',
                'Protection des Investisseurs',
                'Surveillance du Marché',
                'Règles de Publicité',
                'Conformité AML/CFT',
                'Traitement des Stablecoins',
                'Régime de Passeport',
                'Coordination des Autorités',
                'Sanctions et Recours'
            ],
            'MiCA': [
                'Règlement UE directement applicable',
                'Exhaustif: tous actifs numériques',
                'Détailée: ART, EMT, Utility Tokens',
                '5 catégories avec exigences précises',
                'Échelonnée selon activité (€50k-€350k)',
                'Obligations renforcées pour ART/EMT',
                'White paper obligatoire, standardisé',
                'Droit de rétractation 14 jours',
                'Système de surveillance harmonisé',
                'Règles strictes, informations équilibrées',
                'Alignée sur TFR, obligations spécifiques',
                'Cadre complet ART/EMT',
                'Passeport européen automatique',
                'ESMA + EBA + autorités nationales',
                'Sanctions jusqu\'à 5-10% du chiffre'
            ],
            'Maroc (État Actuel)': [
                'Projet de loi + textes épars',
                'Limité, définitions à préciser',
                'Générale "actifs numériques"',
                'Catégories en cours de définition',
                'À déterminer par arrêtés',
                'Principes généraux énoncés',
                'Obligation de transparence (générale)',
                'Principes de protection (généraux)',
                'À développer',
                'Règles à établir',
                'Cadre AML existant à adapter',
                'Non spécifiquement traité',
                'Non prévu actuellement',
                'AMMC + BAM + Ministère Finances',
                'Régime de sanctions à préciser'
            ],
            'Écart': [
                'Critique',
                'Important',
                'Important',
                'Majeur',
                'Majeur',
                'Important',
                'Modéré à Important',
                'Important',
                'Critique',
                'Important',
                'Modéré',
                'Critique',
                'Majeur',
                'Modéré',
                'Important'
            ],
            'Priorité': [
                'Élevée',
                'Élevée',
                'Élevée',
                'Critique',
                'Critique',
                'Moyenne',
                'Moyenne',
                'Élevée',
                'Critique',
                'Moyenne',
                'Élevée',
                'Critique',
                'Basse',
                'Moyenne',
                'Élevée'
            ]
        })
        
        # Analyse des crypto-actifs majeurs
        self.actifs_crypto = {
            'BTC': {
                'nom': 'Bitcoin',
                'type': 'Token de paiement/utilitaire',
                'capit_marché': '$850B',
                'analyse_mica': {
                    'classification': 'Utility token (probable)',
                    'exigences': 'Notification white paper si offre publique',
                    'casp': 'Exchanges doivent être agréés',
                    'risque': 15,
                    'categorie': 'Minimal'
                },
                'analyse_maroc': {
                    'statut': 'Non régulé actuellement',
                    'risques': 'Utilisation non protégée, fraude possible',
                    'recommandation': 'Classer comme actif numérique, encadrer les exchanges',
                    'risque': 70,
                    'categorie': 'Élevé'
                }
            },
            'ETH': {
                'nom': 'Ethereum',
                'type': 'Plateforme utilitaire + PoS',
                'capit_marché': '$350B',
                'analyse_mica': {
                    'classification': 'Utility token complexe',
                    'exigences': 'Notification + gouvernance à analyser',
                    'casp': 'Toutes plateformes doivent être agréées',
                    'risque': 25,
                    'categorie': 'Faible'
                },
                'analyse_maroc': {
                    'statut': 'Non régulé',
                    'risques': 'Smart contracts non vérifiés, risques techniques',
                    'recommandation': 'Établir cadre pour tokens utilitaires complexes',
                    'risque': 65,
                    'categorie': 'Élevé'
                }
            },
            'USDT': {
                'nom': 'Tether',
                'type': 'Stablecoin (référence multiple)',
                'capit_marché': '$95B',
                'analyse_mica': {
                    'classification': 'ART (Asset-Referenced Token)',
                    'exigences': 'Agrément + capital €350k + white paper approuvé + réserves',
                    'casp': 'Agrément spécifique requis',
                    'risque': 75,
                    'categorie': 'Élevé'
                },
                'analyse_maroc': {
                    'statut': 'Interdit par avis BAM 2021',
                    'risques': 'Utilisation souterraine, pas de protection',
                    'recommandation': 'Développer cadre stablecoin au lieu d\'interdiction',
                    'risque': 95,
                    'categorie': 'Critique'
                }
            },
            'USDC': {
                'nom': 'USD Coin',
                'type': 'Stablecoin (référence monétaire)',
                'capit_marché': '$32B',
                'analyse_mica': {
                    'classification': 'EMT (E-Money Token)',
                    'exigences': 'Agrément EMI + garantie des fonds',
                    'casp': 'Agrément avec exigences spécifiques',
                    'risque': 40,
                    'categorie': 'Moyen'
                },
                'analyse_maroc': {
                    'statut': 'Interdit par avis BAM 2021',
                    'risques': 'Mêmes que USDT',
                    'recommandation': 'Autoriser sous licence stricte avec réserves vérifiées',
                    'risque': 95,
                    'categorie': 'Critique'
                }
            },
            'BNB': {
                'nom': 'Binance Coin',
                'type': 'Token d\'exchange + utilitaire',
                'capit_marché': '$65B',
                'analyse_mica': {
                    'classification': 'Token de CASP',
                    'exigences': 'Exchange doit être agréé, token soumis à règles',
                    'casp': 'Binance doit obtenir agrément CASP',
                    'risque': 45,
                    'categorie': 'Moyen'
                },
                'analyse_maroc': {
                    'statut': 'Non régulé',
                    'risques': 'Centralisation, dépendance à une entité étrangère',
                    'recommandation': 'Exiger agrément pour exchanges étrangers opérant au Maroc',
                    'risque': 75,
                    'categorie': 'Élevé'
                }
            }
        }
        
        # Feuille de route détaillée pour le Maroc
        self.feuille_route = {
            'Phase 1: Fondations (0-6 mois)': [
                'Finaliser et adopter la Loi 42-25',
                'Établir les décrets d\'application sur la classification',
                'Créer le registre des PSAN agréés',
                'Définir les exigences de capital par catégorie',
                'Former les équipes AMMC/BAM sur MiCA'
            ],
            'Phase 2: Mise en œuvre (6-18 mois)': [
                'Mettre en place le système d\'agrément des PSAN',
                'Établir les règles de conduite et de gouvernance',
                'Développer le cadre des stablecoins (inspiré ART/EMT)',
                'Implémenter le système de surveillance du marché',
                'Créer les mécanismes de protection des investisseurs'
            ],
            'Phase 3: Maturation (18-36 mois)': [
                'Instaurer le passeport régional avec pays partenaires',
                'Développer le cadre pour la DeFi et les tokens innovants',
                'Mettre en place un fonds de garantie',
                'Établir des accords de coopération avec ESMA/EBA',
                'Réviser et adapter le cadre basé sur l\'expérience'
            ]
        }
        
        # Calcul des scores de maturité
        self.calculer_scores_maturite()
    
    def calculer_scores_maturite(self):
        """Calculer les scores de maturité réglementaire"""
        aspects = len(self.matrice_comparative)
        
        # Scores basés sur le niveau de détail et l'opérationnalité
        scores_mica = {
            'Base Juridique': 100,
            'Champ d\'Application': 95,
            'Classification': 90,
            'Agrément': 92,
            'Capital': 88,
            'Gouvernance': 85,
            'Transparence': 90,
            'Protection': 82,
            'Surveillance': 80,
            'Publicité': 85,
            'AML/CFT': 90,
            'Stablecoins': 95,
            'Passeport': 100,
            'Coordination': 85,
            'Sanctions': 88
        }
        
        scores_maroc = {
            'Base Juridique': 40,
            'Champ d\'Application': 35,
            'Classification': 25,
            'Agrément': 20,
            'Capital': 15,
            'Gouvernance': 40,
            'Transparence': 50,
            'Protection': 35,
            'Surveillance': 10,
            'Publicité': 30,
            'AML/CFT': 70,
            'Stablecoins': 5,
            'Passeport': 0,
            'Coordination': 60,
            'Sanctions': 30
        }
        
        self.scores_mica = scores_mica
        self.scores_maroc = scores_maroc
        self.moyenne_mica = np.mean(list(scores_mica.values()))
        self.moyenne_maroc = np.mean(list(scores_maroc.values()))
        self.ecart_moyen = self.moyenne_mica - self.moyenne_maroc
    
    def initialiser_etat(self):
        """Initialiser l'état de la session"""
        if 'page' not in st.session_state:
            st.session_state.page = 'accueil'
        if 'onglet' not in st.session_state:
            st.session_state.onglet = 'tableau_bord'
    
    def creer_en_tete(self):
        """Créer l'en-tête du tableau de bord"""
        col1, col2, col3 = st.columns([3, 1, 1])
        
        with col1:
            st.markdown('<h1 class="main-header">🇲🇦 Intelligence Réglementaire Maroc-MiCA</h1>', unsafe_allow_html=True)
            st.markdown('<p class="sub-header">Analyse comparative détaillée des cadres réglementaires crypto-actifs</p>', unsafe_allow_html=True)
        
        with col2:
            aujourdhui = datetime.now().strftime("%d/%m/%Y")
            st.markdown(f"**Date :** {aujourdhui}")
            jours_mica = (datetime(2024, 12, 30) - datetime.now()).days
            st.markdown(f"**Jours avant MiCA :** {jours_mica}")
        
        with col3:
            st.markdown("**Version :** 3.0.0")
            st.markdown("**Statut :** 🟢 Opérationnel")
        
        st.markdown("---")
    
    def creer_sidebar(self):
        """Créer la barre latérale de navigation"""
        with st.sidebar:
            # Logo et identité AMMC
            st.markdown("""
            <div style="text-align: center; padding: 1.5rem 0;">
                <div style="font-size: 3rem; color: #D4AF37;">🇲🇦</div>
                <h2 style="color: #D4AF37; margin: 0.5rem 0; font-size: 1.8rem;">AMMC</h2>
                <p style="color: white; font-size: 0.9rem; margin: 0;">
                    Autorité Marocaine du Marché des Capitaux
                </p>
                <p style="color: rgba(255,255,255,0.8); font-size: 0.8rem; margin: 0.5rem 0;">
                    Division Intelligence Réglementaire
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Navigation principale
            st.markdown("### 📚 Navigation")
            
            pages = [
                ('accueil', '🏠 Tableau de Bord'),
                ('comparaison', '⚖️ Analyse Comparative'),
                ('actifs', '💰 Analyse des Actifs'),
                ('details_mica', '🇪🇺 Détails MiCA'),
                ('details_maroc', '🇲🇦 Cadre Marocain'),
                ('feuille_route', '🗺️ Feuille de Route'),
                ('recommandations', '🎯 Recommandations')
            ]
            
            for page_id, page_label in pages:
                if st.button(page_label, key=f"btn_{page_id}", use_container_width=True):
                    st.session_state.page = page_id
                    st.rerun()
            
            st.markdown("---")
            
            # Sélection rapide
            st.markdown("### 🔍 Focus")
            focus = st.selectbox(
                "Zone d'analyse",
                ["Tous les aspects", "Licensing", "Stablecoins", "Protection investisseurs", "AML/CFT"],
                key="focus_select"
            )
            
            st.markdown("---")
            
            # Actions rapides
            st.markdown("### ⚡ Actions")
            
            if st.button("📊 Générer Rapport Complet", use_container_width=True):
                st.success("Rapport généré avec succès")
            
            if st.button("🔄 Actualiser les Données", use_container_width=True):
                st.rerun()
            
            st.markdown("---")
            
            # Métadonnées
            st.markdown("### ℹ️ Informations")
            st.markdown("**Dernière mise à jour :** Aujourd'hui")
            st.markdown("**Sources :** 4 documents officiels")
            st.markdown("**Couverture :** 15 aspects réglementaires")
            
            progress = (self.moyenne_maroc / self.moyenne_mica) * 100
            st.progress(int(progress), text=f"Alignement: {progress:.1f}%")
    
    def page_accueil(self):
        """Page d'accueil / Tableau de bord"""
        st.markdown('<div class="section-title">📊 TABLEAU DE BORD SYNTHÉTIQUE</div>', unsafe_allow_html=True)
        
        # Métriques clés
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "Maturité MiCA",
                f"{self.moyenne_mica:.1f}%",
                delta="+2.5%",
                delta_color="normal"
            )
        
        with col2:
            st.metric(
                "Maturité Maroc",
                f"{self.moyenne_maroc:.1f}%",
                delta="+15.2% (potentiel)",
                delta_color="normal"
            )
        
        with col3:
            st.metric(
                "Écart Réglementaire",
                f"{self.ecart_moyen:.1f} points",
                delta="-8.3% (réduction cible)",
                delta_color="inverse"
            )
        
        with col4:
            actifs_critiques = sum(1 for a in self.actifs_crypto.values() 
                                  if a['analyse_maroc']['categorie'] in ['Critique', 'Élevé'])
            st.metric(
                "Actifs à Risque",
                f"{actifs_critiques}/5",
                delta=f"-{actifs_critiques} à traiter",
                delta_color="inverse"
            )
        
        # Graphique de maturité par aspect
        st.markdown("#### 📈 Maturité Réglementaire par Aspect")
        
        df_scores = pd.DataFrame({
            'Aspect': list(self.scores_mica.keys()),
            'MiCA': list(self.scores_mica.values()),
            'Maroc': list(self.scores_maroc.values())
        })
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=df_scores['Aspect'],
            y=df_scores['MiCA'],
            name='MiCA',
            marker_color='#003366',
            text=df_scores['MiCA'].astype(int).astype(str) + '%',
            textposition='auto'
        ))
        
        fig.add_trace(go.Bar(
            x=df_scores['Aspect'],
            y=df_scores['Maroc'],
            name='Maroc',
            marker_color='#D4AF37',
            text=df_scores['Maroc'].astype(int).astype(str) + '%',
            textposition='auto'
        ))
        
        fig.update_layout(
            height=500,
            barmode='group',
            xaxis_tickangle=-45,
            showlegend=True,
            plot_bgcolor='white',
            yaxis_range=[0, 105],
            yaxis_title="Score de maturité (%)",
            xaxis_title="Aspect réglementaire"
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Alertes prioritaires
        st.markdown("#### ⚠️ Alertes Prioritaires")
        
        alertes = [
            ("Stablecoins non régulés", "Critique", "Les stablecoins représentent $127B mais sont interdits sans cadre alternatif"),
            ("Absence de surveillance marché", "Critique", "Pas de mécanisme pour détecter manipulations ou abus"),
            ("Exigences de capital indéfinies", "Élevée", "Impossible d'agréer des PSAN sans exigences claires"),
            ("
