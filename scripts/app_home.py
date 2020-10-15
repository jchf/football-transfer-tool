import streamlit as st


def app():
    st.markdown("<h1>&#x1F4C8 Football Transfer Tool &#x26BD</h1> ",
                unsafe_allow_html=True)

    st.markdown("L'outil qui te permet de détecter le joueur de tes **rêves** :tada:",
                unsafe_allow_html=True)

    st.markdown("<h2>Bienvenue!</h2> ",
                unsafe_allow_html=True)

    st.markdown("""
    Pour pouvoir détecter un joueur en fonction de ses caractéristiques rendez vous dans l'onglet 
    **Détecter un joueur**, vous pourrez ensuite avoir un aperçu sur ses statistiques et comparer des joueurs
    entre eux si vous hésitez...
    
    Si vous avez déjà des joueurs en tête rendez vous directement dans l'onglet **Comparer des joueurs**
    
    Dans  l'onglet **Aide** vous trouverez le glossaire des styles et comment la note de performance a
    été définie.
    """)