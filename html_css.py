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
