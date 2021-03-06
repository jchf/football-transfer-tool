import app_detect
import app_compare
import app_about
import app_home
import streamlit as st
import warnings
warnings.filterwarnings("ignore")

PAGES = {
    "Page d'accueil" : app_home,
    "Détecter un joueur": app_detect,
    "Comparer des joueurs": app_compare,
    "Aide": app_about
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Aller à", list(PAGES.keys()))
if selection == 'Détecter un joueur':
    st.sidebar.info("Pour lire les définitions de chaque style rendez vous sur l'onglet Aide")
page = PAGES[selection]
page.app()
