import streamlit as st
import pandas as pd
import plotly.express as px
import html_css
import plotly.graph_objects as go
import urllib.request
import re
from googletrans import Translator

def app(name_detected='', header=True):
    if header:
        st.markdown("<h1>&#x1F4C8 Football Transfer Tool &#x26BD</h1> ",
                    unsafe_allow_html=True)

        st.markdown("L'outil qui te permet de détecter le joueur de tes **rêves** :tada:",
                    unsafe_allow_html=True)

        st.markdown("<h2>Compare des joueurs  &#129340</h2> ",
                    unsafe_allow_html=True)

    # Initialisation, Lecture des données
    df = pd.read_csv('data/dataset_final.csv')
    style_df = pd.read_csv('data/style_id.csv')
    translator = Translator()

    # Sélection des noms de joueurs
    if name_detected == '':
        name = st.multiselect('🔎 Rechercher un ou plusieurs nom(s) de joueur', df['Player Name'])
    else:
        name = name_detected

    if name:
        data = df[df['Player Name'].isin(name)]

        # Différence d'affichage entre les gardiens et le reste
        if next(iter(set(data['poste'].values))) == 'GK':
            cols = ['Apps', 'Mins', 'Yellow', 'Red', 'MotM', 'Rating']
            names_col = ['Plongeon', 'Jeu à la main', 'Jeu au pied', 'Reflexes', 'Vitesse', 'Positionnement']
            data_radar = data.set_index('Player Name')[
                ['gk_diving', 'gk_handling', 'gk_kicking', 'gk_reflexes', 'gk_speed', 'gk_positioning']]
            data_radar.columns = names_col
            data_radar.drop_duplicates(inplace=True)
            data_radar = data_radar.transpose().rename_axis('Aptitudes').reset_index()
            gk = True
        else:
            cols = ['Apps', 'Mins', 'Goals', 'Assists', 'Goals/90min', 'Assists/90min', 'Yellow', 'Red', 'SpG', 'PS%',
                    'AerialWon', 'MotM', 'Rating']
            names_col = ['Vitesse', 'Tir', 'Physique', 'Passes', 'Défense', 'Dribbles']
            data_radar = data.set_index('Player Name')[
                ['pace', 'shooting', 'physic', 'passing', 'defending', 'dribbling']]
            data_radar.columns = names_col
            data_radar.drop_duplicates(inplace=True)
            data_radar = data_radar.transpose().rename_axis('Aptitudes').reset_index()
            gk = False

        # Pour chaque nom on récupère les infos
        for i, nom_ in enumerate(name):
            idx = data['sofifa_id'].values[i]
            img = data['url_img'].values[i]
            nom = data['Player Name'].values[i]
            club = data['Club'].values[i]
            age = int(data['age'].values[i])
            taille = data['Height'].values[i]
            poids = data['Weight'].values[i]
            perf = data['perf'].values[i]*20  # *20 pour ramener a 100 et modifier le paramètre "width" des étoiles
            poste = data['poste'].values[i]
            pied = 'Droitier' if data['preferred_foot'].values[i] == 'Right' else 'Gaucher'
            contrat = data['contract_valid_until'].values[i]
            styles = style_df[style_df['index'] == idx]['style'].values
            valeur = data['value_eur'].values[i]/1e6
            salaire = data['wage_eur'].values[i]/1e3
            nation = data['nationality'].values[i]
            tags = data['player_tags'].values[i]
            potentiel = '&#x1F31F' if data['pepite'].values[i] == 1 else ''

            #Affichage des infos
            st.markdown(f'<img src='+img+'>', unsafe_allow_html=True)
            st.markdown(f'<h2>{potentiel} {nom}, {club}, {poste} <br>Valeur : {valeur} M€, Salaire : {salaire} K€</br></h2>',
                        unsafe_allow_html=True)
            st.subheader(f'{age} ans, fin de contrat en {int(contrat)}\n {taille} cm, {poids} kg, {pied}')
            st.text(f'Nationalité : {nation}')
            st.markdown(html_css.STYLE_STARS.format(perf), unsafe_allow_html=True)
            st.markdown('Note de performance')
            if len(styles) > 0:
                st.markdown(f"**Style(s) du joueur** : {', '.join(styles)}")
            if not pd.isna(tags):
                st.markdown(f"<i>{tags}</i>", unsafe_allow_html=True)

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
            st.dataframe(pd.DataFrame({'Points forts': points_forts, 'Points faibles': points_faibles})
                         .assign(hack='').set_index('hack'))

        # initialisation de la figure
        fig = go.Figure()
        #Si un seul joueur
        if len(name) == 1:
            # affichage des stats
            data_joueur = data[data['Player Name'] == nom]
            st.header('Statistiques')
            st.table(data_joueur.set_index('saison')[cols])

            # affichage du graph radar
            st.header('Attributs techniques')
            fig = px.line_polar(data_radar, r=nom, theta='Aptitudes', line_close=True)
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 100]
                    )),
                showlegend=False
            )
            st.plotly_chart(fig)

            search_keyword = nom
            search_keyword = '+'.join(search_keyword.split(' ')) + '+highlights'
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            st.header('Résumé vidéo du joueur')
            st.markdown(html_css.YTB_VIDEO.format(video_ids[0]), unsafe_allow_html=True)

        # Si plus pour la comparaison
        else:
            st.header('Comparaison des stats')
            st.table(data[data['Player Name'].isin(name)].set_index('Player Name')[cols].
                     style.background_gradient(cmap='YlGn').
                     set_precision(2))

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
