import streamlit as st


def app():
    st.markdown("<h1>&#x1F4C8 Football Transfer Tool &#x26BD</h1> ",
                unsafe_allow_html=True)

    st.markdown("L'outil qui te permet de détecter et de transferer le joueur de tes **rêves** :tada:",
                unsafe_allow_html=True)

    st.markdown("<h2>Glossaire des styles</h2> ",
                unsafe_allow_html=True)

    aide = """
        Styles pour gardiens :
        -	<b>Bouclier</b>
        Dégagement, agilité, accélération et vitesse
        -	<b>Chat</b>
        Agilité, accélération, vitesse, positionnement
        -	<b>Gant</b>
        Plongeon, jeu à la main, positionnement
        -	<b>Mur</b>
        Plongeon, jeu à la main, dégagement

        Styles pour défenseurs :
        -	<b>Colonne vertébrale</b>
        Vista, centres, longs ballons, passes courtes, effets, interceptions, précision tête, marquage, tacle debout, tacle glissé, détente, force
        -	<b>Garde</b>
        Agilité, conduite de balle, dribbles, calme, interceptions, précision tête, marquage, tacle debout, tacle glissé 
        -	<b>Gladiateur</b>
        Positionnement, finition, puissance de frappe, tir de loi, interception, précision tête, marquage, tacle debout, tacle glissé
        -	<b>Homme de l’Ombre</b>
        Accélération, vitesse, interceptions, précision tête, marquage, tacle debout, tacle glissé
        -	<b>Pilier</b>
        Accélération, vitesse, interceptions, précision tête, marquage, tacle debout, tacle glissé, détente, force, engagement
        -	<b>Sentinelle</b>
        Interceptions, précision tête, marquage, tacle debout, tacle glissé, détente, force, engagement

        Styles pour milieux de terrain
        -	<b>Artiste</b>
        Vista, centre, longs ballons, passes courtes, effets, agilité, équilibre, conduite de balle, dribbles
        -	<b>Architecte</b>
        Vista, centre, longs ballons, passes courtes, effets, détente, force, engagement
        -	vCatalyseur</b>
        Accélération, vitesse, vista, centres, précision coup franc, passes courtes, effets
        -	<b>Maestro</b>
        Positionnement, puissance de frappe, tir de loin, reprise de volée, vista, précision coup franc, longs ballons, passes courtes, agilité, reflexes, conduite de balle, dribbles
        -	<b>Moteur</b>
        Accélération, vitesse, vista, centres, précision coup franc, longs ballons, passes courtes, agilité, reflexes, conduite de balle, dribbles, équilibre
        -	<b>Roc</b>
        Vista, centre, longs ballons, passes courtes, effets, interceptions, marquage, tacle debout, tacle glissé

        Styles pour attaquants
        -	<b>Chasseur</b>
        Accélération, vitesse, positionnement, finition, puissance de frappe, reprise de volée, pénalty
        -	<b>Finisseur</b>
        Placement offensif, finition, puissance de frappe, tir de loin, reprise de volée, pénalty, détente, force, engagement
        -	<b>Buteur</b>
        Positionnement, finition, puissance de frappe, reprise de volée, pénalty, agilité, reflexes, conduite de balle, dribble, détente, force, engagement
        -	<b>Œil de lynx</b>
        Accélération, vitesse, positionnement, finition, puissance de frappe, reprise de volée, pénalty, détente, force, engagement
        -	<b>Tireur d’élite</b>
        Positionnement, finition, puissance de frappe, reprise de volée, pénalty, agilité, équilibre, reflexes, conduite de balle, dribbles, calme
        -	<b>Faucon</b>
        Positionnement, finition, puissance de frappe, tir de loi, pénalty, vista, centre, précision coup franc, passes courtes, effets

        Styles communs :
        -	<b>Tireur de coups francs</b>
        Spécialiste des coups francs.
        -	<b>Magicien</b>
        Régale le public et ses partenaires, écœure ses adversaires ! Joga bonito !
        -	<b>Légende</b>
        Toute la planète connait son nom… il a tout gagné… une véritable légende du football.
        -	<b>Star internationale</b>  
        Star de son équipe et de sa sélection, c’est un joueur sur qui on peut compter.

    """

    st.markdown(aide, unsafe_allow_html=True)

