import pandas as pd
import hydralit as hy

def killfeed(killfeed_img):
    hy.markdown(
        f"""
        <style>
        a {{
            text-decoration: none;
            }}

        .container {{
            text-align: center;
            }}

        .killFeed {{
            margin-top: 15px;
            min-width: 100px;
            position: relative;
            display: inline-block;
            height: 40px;
            background: rgba(0,0,0,0.5);
            border: 2px #B50000 solid;
            border-radius: 6px;
            padding: 0 10px;
            transform: scale(1);
            transition: .1s;
            }}

        .killer {{
            color: #ECCE51;
            line-height: 40px;
            display: inline-block;
            margin-right: 10px;
            float: left;
            }}

        .weapon {{
            margin-top: 8px;
            height: 25px;
            width: 80px;
            background: url({killfeed_img}) no-repeat;
            background-size: cover;
            float: left;
            }}

        .headshot.true {{
            margin: 8px 0px 0px 10px;
            height: 22px;
            width: 22px;
            background-image: url(https://www.steamid.co.uk/images/headshot.png);
            background-size: cover;
            float: left;
            }}

        .wallbang {{
            float: left;
            }}

        .wallbang.true {{
            margin: 8px 0px 0px 10px;
            height: 22px;
            width: 22px;
            background: url(http://i.imgur.com/FmmFb28.png);
            background-size: cover;
            float: left;
            }}

        .headshot {{
            float: left;
            }}

        .killed {{
            margin-left: 10px;
            color: #cbe564 !important;
            line-height: 40px;
            display: inline-block;
            float: left;
            }}
        .css-xr8hm4 {{
            flex-direction: column-reverse;
        }}
        </style>
        """, unsafe_allow_html=True)

    hy.markdown('''<link href='https://fonts.googleapis.com/css?family=Rajdhani:600' rel='stylesheet' type='text/css'>
        <div class="container">
        <div class="killFeed">
            <a href="" class="killer">banned</a>
            <div class="weapon"></div>
            <div class="headshot"></div>
            <div class="wallbang"></div>
            <a href="" class="killed">storM</a>
        </div>
        </div>
        <div class="container">
        <div class="killFeed">
            <a href="" class="killer">bro you fukin suk</a>
            <div class="weapon"></div>
            <div class="headshot true"></div>
            <div class="wallbang"></div>
            <a href="" class="killed">storM</a>
        </div>
        </div>
        <div class="container">
        <div class="killFeed">
            <a href="" class="killer">HACKS</a>
            <div class="weapon"></div>
            <div class="headshot"></div>
            <div class="wallbang true"></div>
            <a href="" class="killed">storM</a>
        </div>
        </div>
        <div class="container">
        <div class="killFeed">
            <a href="" class="killer">FaZe TrickshoT</a>
            <div class="weapon"></div>
            <div class="headshot true"></div>
            <div class="wallbang true"></div>
            <a href="" class="killed">Mrots</a>
        </div>
        </div>''', unsafe_allow_html=True)
