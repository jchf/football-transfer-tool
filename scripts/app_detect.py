import streamlit as st
import pandas as pd
import numpy as np
import app_compare


def app():
    st.markdown("<h1>&#x1F4C8 Football Transfer Tool &#x26BD</h1> ",
                unsafe_allow_html=True)

    st.markdown("L'outil qui te permet de détecter le joueur de tes **rêves** :tada:",
                unsafe_allow_html=True)

    st.markdown("<h2>&#x1F3AF Détecte le joueur idéal &#x1F50D</h2> ",
                unsafe_allow_html=True)
    st.markdown('')

    # Initialisation, Lecture des données
    fifa_stats = pd.read_csv('../data/joueurs_avec_stats_fifa.csv')
    styles = fifa_stats.filter(like='style_').columns.sort_values()
    styles_propre = ['2 pieds', 'Architecte','Artiste','Bouclier','Buteur','Catalyseur','Tireur de coups francs',
                     'Chasseur', 'Chat','Colonne Vertébrale','Faucon','Finisseur', 'Gant','Garde','Gladiateur','Legende',
                     'Maestro','Magicien','Moteur','Mur','Oeil de lynx',"Homme de l'ombre",'Pilier','Roc','Sentinelle','Star',"Tireur d'élite"]
    cols = ['Player Name','age','Team', 'poste', 'nationality']

    st.sidebar.subheader("Mon joueur idéal")

    poste = st.sidebar.selectbox('Poste', ['Tous','GK','DC','LAT','MDC','MOC','ATT'])
    idx_poste = fifa_stats[fifa_stats['poste'] == poste] if poste != 'Tous' else fifa_stats.copy()
    liste_styles = list(set(np.where(idx_poste[styles] == 1)[1]))
    selected_styles = st.sidebar.multiselect('Choisis le(s) style(s) du joueur', np.array(styles_propre)[liste_styles])
    ligues_propres = ['Toutes', 'Premier League', 'Serie A', 'Bundesliga', 'LaLiga', 'Ligue 1', 'Liga NOS', 'Eredivisie']
    selected_ligue = st.sidebar.selectbox('Choisis une ligue', ligues_propres)
    ligues = ['All', 'EPL', 'ISA', 'GB', 'SLL', 'FL1', 'PLN', 'NE']

    filtre_styles = []
    for col, selected_style in zip(styles, styles_propre):
        if selected_style in selected_styles:
            filtre_styles.append(col)

    for col, ligue in zip(ligues, ligues_propres):
        if ligue in selected_ligue:
            filtre_ligues = col

    ligue_idx = idx_poste[idx_poste['Tournament'] == filtre_ligues] if selected_ligue != 'Toutes' else idx_poste.copy()
    idx_style = ligue_idx[(np.alltrue(fifa_stats[filtre_styles], axis=1))]

    try:
        min_val = int(idx_style['value_eur'].values.min())/1e6
        max_val = int(idx_style['value_eur'].values.max())/1e6
        values = st.sidebar.slider('Valeur marchande (M€)', min_val, max_val, (min_val, max_val), format="%d M€")
        left, right = np.floor(values)[0]*1e6, np.ceil(values)[1]*1e6
        range_valeur = idx_style['value_eur'].between(left, right)

        min_sal = int(idx_style['wage_eur'][range_valeur].values.min())/1e3
        max_sal = int(idx_style['wage_eur'][range_valeur].values.max())/1e3
        salaires = st.sidebar.slider('Salaire mensuel (K€)', min_sal, max_sal, (min_sal, max_sal), format="%d K€")
        left_, right_ = np.floor(salaires)[0] * 1e3, np.ceil(salaires)[1] * 1e3
        range_salaires = idx_style['wage_eur'].between(left_, right_)

        result_filtres = idx_style[(range_valeur) & (range_salaires)]

        # nb = result_filtres.shape[0]
        with st.spinner('Recherche en cours...'):
            if st.sidebar.checkbox("N'affichez que les pépites 🌟"):
                data = result_filtres[cols][result_filtres['pepite'] == 1].reset_index(drop=True)
                nb = data.shape[0]
            else:
                data = result_filtres[cols].reset_index(drop=True)
                nb = data.shape[0]
            if nb == 0:
                data.iloc[0]
            st.info(f'{nb} joueurs trouvés')
            st.write(data)

        select_name = st.multiselect('Choisis un ou plusieurs joueurs pour les comparer!', data['Player Name'].values)

        if len(select_name) > 1:
            compare = st.button('Comparer les joueurs')
        elif len(select_name)==1:
            compare = st.button(f'Afficher les stats de {select_name[0]}')

        app_compare.app(select_name, False)

    except (ValueError, IndexError):
        st.error('Aucun joueur trouvé, réessayer')
        st.image('https://cdn.sofifa.net/players/notfound_0_120.png', width=150)
