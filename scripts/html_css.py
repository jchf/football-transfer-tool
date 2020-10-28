STYLE_STARS = """
    <style>
        .star-ratings-css {{
          unicode-bidi: bidi-override;
          color: #c5c5c5;
          font-size: 25px;
          height: 25px;
          width: 100px;
          margin-bottom: 10px ;
          position: relative;
          padding: 0;
          text-shadow: 0px 1px 0 #a2a2a2;
          }}
          
        .star-ratings-css-top {{
        color: #e7711b;
        padding: 0;
        position: absolute;
        z-index: 1;
        display: block;
        top: 0;
        left: 0;
        overflow: hidden;
        }}
        
        .star-ratings-css-bottom {{
        padding: 0;
        display: block;
        z-index: 0;
        }}
        
    </style>
    
    <div class="star-ratings-css">
        <div class="star-ratings-css-top" style="width: {}%";><span>★</span><span>★</span><span>★</span><span>★</span><span>★</span></div>
        <div class="star-ratings-css-bottom"><span>★</span><span>★</span><span>★</span><span>★</span><span>★</span></div>
    </div>
"""

CENTRE_IMG = """
    <style>
        .center {{
          display: block;
          margin-left: auto;
          margin-right: auto;
          width: 50%;
        }}
    </style>
    
    <div class="center">
        <img src="{}">
    </div>
}"""

YTB_VIDEO = """
    <style>
        .video,
        iframe {{
          margin-left: 20%;
          }}
    </style>
    
    <iframe width="500" height="300" src="https://www.youtube.com/embed/{}" frameborder="0"
    allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

"""

LEGENDE = """
    <div style="font-size: x-small">
        <tr>  
            <td><strong>Mins</strong>: Minutes jouées</td>
            <td><strong>Goals</strong>: Total Buts</td>
            <td><strong>Assists</strong>: Total Passes décisives</td>
            <td><strong>AerialWon</strong>: Duels aériens gagnés par match</td>
            <td><strong>MotM</strong>: Homme du match</td> 
            <td><strong>Rating</strong>: Note moyenne</td> 
        </tr>
        <tr>
            <td><strong>Tackles</strong>: Tacles par match</td>
            <td><strong>Interceptions</strong>: Interceptions par match</td>
            <td><strong>Fouls</strong>: Fautes commises par match</td>
            <td><strong>OffsidesWon</strong>: Hors-jeu gagné par match</td>
            <td><strong>Clear</strong>: Dégagements par match</td>
            <td><strong>HasBeenDribbled</strong>: Dribbles subis par match</td>
            <td><strong>Blocks</strong>: Tirs contrés par match</td>
        </tr>
        <tr>
            <td><strong>SpG</strong>: Tirs par match</td>
            <td><strong>PS%</strong>: Taux de passes réussies</td>
            <td><strong>KeyPasses</strong>: Passes clés par match</td>
            <td><strong>Fouled</strong>: Fautes subies par match</td>
            <td><strong>Dispossessed</strong>: Pertes de balle par match</td>
            <td><strong>BadControl</strong>: Mauvais controles par match</td>
        </tr>
    </div>
                
"""

test = """
    <style>
        .star-ratings-css {{
          unicode-bidi: bidi-override;
          color: #c5c5c5;
          font-size: 25px;
          height: 25px;
          width: 100px;
          margin-bottom: 10px ;
          position: relative;
          padding: 0;
          text-shadow: 0px 1px 0 #a2a2a2;
          }}
          
        .star-ratings-css-top {{
        color: #e7711b;
        padding: 0;
        position: absolute;
        z-index: 1;
        display: block;
        top: 0;
        left: 0;
        overflow: hidden;
        }}
        
        .star-ratings-css-bottom {{
        padding: 0;
        display: block;
        z-index: 0;
        }}
        
    </style>
    

    <div>
        <div>
            <tr>
                <td><img src={}></td>
                <td><img src={}></td>
            </tr>
            <tr>
                <td><h3>{} {}, {}, {}</h3>
                    Valeur : {} M€
                    <br>Salaire : {} K€</br>
                    <font size="2">Nationalité : {}</font> 
                    <div class="star-ratings-css">
                        <div class="star-ratings-css-top" style="width: {}%";><span>★</span><span>★</span><span>★</span><span>★</span><span>★</span></div>
                        <div class="star-ratings-css-bottom"><span>★</span><span>★</span><span>★</span><span>★</span><span>★</span></div>
                    </div>
                    Note de performance
                    <br>
                    </td>
                <td><h3>{} {}, {}, {}</h3>
                    Valeur : {} M€
                    <br>Salaire : {} K€</br>
                    <font size="2">Nationalité : {}</font> 
                    <div class="star-ratings-css">
                        <div class="star-ratings-css-top" style="width: {}%";><span>★</span><span>★</span><span>★</span><span>★</span><span>★</span></div>
                        <div class="star-ratings-css-bottom"><span>★</span><span>★</span><span>★</span><span>★</span><span>★</span></div>
                    </div>
                    Note de performance</td>
            </tr>
            <tr>
                <td></td>
                <td></td>
            </tr>
        </div>
    </div>

"""

