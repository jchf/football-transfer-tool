import streamlit as st
import pandas as pd
import plotly.express as px
import html_css
import plotly.graph_objects as go
import urllib.request
import re
from googletrans import Translator
import bokeh
from utils import *


def app(name_detected='', header=True):
    if header:
        st.markdown("<h1>&#x1F4C8 Football Transfer Tool &#x26BD</h1> ",
                    unsafe_allow_html=True)

        st.markdown("L'outil qui te permet de détecter le joueur de tes **rêves** :tada:",
                    unsafe_allow_html=True)

        st.markdown("<h2>Compare des joueurs  &#129340</h2> ",
                    unsafe_allow_html=True)

    # Initialisation, Lecture des données
    real_stats = pd.read_csv('data/joueurs_avec_stats_reelles.csv')
    fifa_stats = pd.read_csv('data/joueurs_avec_stats_fifa.csv')
    style_df = pd.read_csv('data/style_id.csv')
    translator = Translator()

    # Sélection des noms de joueurs
    if name_detected == '':
        name = st.multiselect('🔎 Rechercher un ou plusieurs nom(s) de joueur', fifa_stats['Player Name'])
    else:
        name = name_detected

    if name:
        data = fifa_stats[fifa_stats['Player Name'].isin(name)]

        # Différence d'affichage entre les gardiens et le reste
        if next(iter(set(data['poste'].values))) == 'GK':
            cols_gen = ['Team','Apps', 'Mins', 'Yellow', 'Red', 'MotM', 'Rating']
            cols_def = ['Season', 'Team','Apps', 'Mins','Tackles','Interceptions','Fouls','OffsidesWon',
                        'Clear','HasBeenDribbled','Blocks']
            cols_off = ['Season', 'Team','Apps', 'Mins', 'SpG', 'PS%','KeyPasses','Dribbles','Fouled',
                        'Dispossessed','BadControl']
            col_aptitudes = ['Plongeon', 'Jeu à la main', 'Jeu au pied', 'Reflexes', 'Vitesse', 'Positionnement']
            data_radar = data.set_index('Player Name')[
                ['gk_diving', 'gk_handling', 'gk_kicking', 'gk_reflexes', 'gk_speed', 'gk_positioning']]
            data_radar.columns = col_aptitudes
            data_radar.drop_duplicates(inplace=True)
            data_radar = data_radar.transpose().rename_axis('Aptitudes').reset_index()
            gk = True
        else:
            cols_gen = ['Season','Team','Apps', 'Mins', 'Goals', 'Assists', 'Goals/90min',
                    'Assists/90min', 'AerialWon','MotM', 'Rating']
            cols_def = ['Season', 'Team','Apps', 'Mins','Tackles','Interceptions','Fouls','OffsidesWon',
                        'Clear','HasBeenDribbled','Blocks']
            cols_off = ['Season', 'Team','Apps', 'Mins', 'SpG', 'PS%','KeyPasses','Dribbles','Fouled',
                        'Dispossessed','BadControl']
            
            col_aptitudes = ['Vitesse', 'Tir', 'Physique', 'Passes', 'Défense', 'Dribbles']

            data_radar = data.set_index('Player Name')[
                ['pace', 'shooting', 'physic', 'passing', 'defending', 'dribbling']]
            data_radar.columns = col_aptitudes
            data_radar.drop_duplicates(inplace=True)
            data_radar = data_radar.transpose().rename_axis('Aptitudes').reset_index()
            gk = False

        ligues = ['EPL', 'FL1', 'ISA', 'PLN', 'NE', 'GB', 'SLL']
        cols = st.beta_columns(len(name))
        # Pour chaque nom on récupère les infos
        for i, nom_ in enumerate(name):
            idx = data['sofifa_id'].values[i]
            img = data['url_img'].values[i]
            nom = data['Player Name'].values[i]
            club = data['Team'].values[i]
            age = int(data['age'].values[i])
            taille = data['height_cm'].values[i]
            poids = data['weight_kg'].values[i]
            perf = data['perf'].values[i] * 20  # *20 pour ramener a 100 et modifier le paramètre "width" des étoiles
            poste = data['poste'].values[i]
            pied = 'Droitier' if data['preferred_foot'].values[i] == 'Right' else 'Gaucher'
            contrat = data['contract_valid_until'].values[i]
            styles = style_df[style_df['index'] == idx]['style'].values
            valeur = data['value_eur'].values[i] / 1e6
            salaire = data['wage_eur'].values[i] / 1e3
            nation = data['nationality'].values[i]
            tags = data['player_tags'].values[i]
            potentiel = '&#x1F31F' if data['pepite'].values[i] == 1 else ''

            # Affichage des infos
            cols[i].markdown(f'<img src=' + img + '>', unsafe_allow_html=True)
            cols[i].write(f'<h3>{potentiel} {nom}, {club}</h3>', unsafe_allow_html=True)
            cols[i].write(f'**{poste}, {age} ans**<br>{taille} cm, {poids} kg, {pied}<br>Nationalité : {nation}',
                          unsafe_allow_html=True)
            cols[i].write(f'Valeur : {valeur} M€, Salaire : {salaire} K€<br>Fin de contrat en {int(contrat)}<br>',
                          unsafe_allow_html=True)
            cols[i].markdown(html_css.STYLE_STARS.format(perf), unsafe_allow_html=True)
            cols[i].markdown('Note de performance')
            if len(styles) > 0:
                cols[i].markdown(f"**Style(s) du joueur** : {', '.join(styles)}")
            if not pd.isna(tags):
                cols[i].markdown(f"<i>{tags}</i>", unsafe_allow_html=True)

            data_joueur = data[data['Player Name'] == nom]
            forts = data_joueur.loc[data_joueur.index[0], 'attacking_crossing':'defending_sliding_tackle']. \
                sort_values(ascending=False).head(5)
            faibles = data_joueur.loc[data_joueur.index[0], 'attacking_crossing':'defending_sliding_tackle']. \
                sort_values().head(5)
            points_forts = [translator.translate(
                re.sub(r'(attacking_|skill_|mentality_|power_|movement_|defending_|_)', ' ', s),
                src='en', dest='fr').text.capitalize() for s in forts.index]
            points_faibles = [translator.translate(
                re.sub(r'(attacking_|skill_|mentality_|power_|movement_|defending_|_)', ' ', s),
                src='en', dest='fr').text.capitalize() for s in faibles.index]
            cols[i].dataframe(pd.DataFrame({'Points forts': points_forts, 'Points faibles': points_faibles})
                              .assign(hack='').set_index('hack'))

        # initialisation de la figure
        fig = go.Figure()
        #Si un seul joueur
        if len(name) == 1:
            # affichage du graph radar
            st.header('Attributs techniques')
            fig = px.line_polar(data_radar, r=nom, theta='Aptitudes', line_close=True, width=400, height=400)
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 100]
                    )),
                showlegend=False
            )
            st.plotly_chart(fig)

            # affichage des stats
            data_joueur = real_stats[real_stats['Player Name'] == nom]
            st.markdown('<h2>Statistiques<p>(Ligues nationales)</p></h2>', unsafe_allow_html=True)

            df = data_joueur[data_joueur['Tournament'].isin(ligues)].head(5)
            tabs = bokeh.models.Tabs(
                tabs=[
                    print_tab(df[cols_gen], titre='Général'),
                    print_tab(df[cols_def], titre='Défense'),
                    print_tab(df[cols_off], titre='Attaque')
                    ]
            )
            st.bokeh_chart(tabs, use_container_width=True)
            with st.beta_expander("Voir la légende"):
                st.markdown(html_css.LEGENDE, unsafe_allow_html=True)

            search_keyword = nom
            search_keyword = '+'.join(search_keyword.split(' ')) + '+highlights'
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            st.header('Résumé vidéo du joueur')
            st.markdown(html_css.YTB_VIDEO.format(video_ids[0]), unsafe_allow_html=True)

        # Si plus pour la comparaison
        else:
            st.header('Comparaison des attributs techniques')
            for nom_ in name:
                fig.add_trace(go.Scatterpolar(
                    r=data_radar[nom_], theta=data_radar['Aptitudes'],
                    fill='tonext',
                    name=nom_
                ))
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 100]
                    )),
                showlegend=True
            )
            st.plotly_chart(fig)

            st.markdown('<h2>Comparaison des stats<p>(Ligues nationales)</p></h2>', unsafe_allow_html=True)
            df = real_stats[(real_stats['Player Name'].isin(name)) & (real_stats['Tournament'].isin(ligues))]\
                .set_index('Player Name')
            saison = st.selectbox('Choisis une saison', options=df.Season.unique())
            cols_gen.pop(0)
            st.dataframe(df[df['Season'] == saison][cols_gen].style.background_gradient(cmap='YlGn').set_precision(2))

            for nom_ in name:
                search_keyword = nom_
                search_keyword = '+'.join(search_keyword.split(' ')) + '+highlights'
                html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
                video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                st.header('Résumé vidéo de ' + nom_)
                st.markdown(html_css.YTB_VIDEO.format(video_ids[0]), unsafe_allow_html=True)


            # if not gk:
            #     data_ = data.set_index('Player Name')
            #     fig2 = px.bar(data_[['Goals', 'Assists']])
            #     fig2.update_layout(barmode='group')
            #     st.plotly_chart(fig2)
