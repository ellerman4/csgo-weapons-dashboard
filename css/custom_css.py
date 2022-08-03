import hydralit as hy
import base64
import uuid

# Function called on each weapon page to fix alignment and apply border to gif
def align_justify():
    hy.markdown('<style> .etr89bj1 > img { border-radius: 25px; } </style>', unsafe_allow_html=True)
    hy.markdown('<style> .css-ocqkz7 { align-items: center; } </style>', unsafe_allow_html=True)
    hy.markdown('<style> .css-1kyxreq { justify-content: center; } </style>', unsafe_allow_html=True)

def killfeed(weapon_data):
    unique_id = str(uuid.uuid4())   # Generate a unique id to not overwrite existing .weapon css element everytime function is called
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

        .weapon{unique_id} {{
            margin-top: 8px;
            height: 19px;
            width: 60px;
            background: url({weapon_data['Killfeed']}) no-repeat;
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

    hy.markdown(f'''<link href='https://fonts.googleapis.com/css?family=Rajdhani:600' rel='stylesheet' type='text/css'>
        <div class="container">
        <div class="killFeed">
            <a href="" class="killer">banned</a>
            <div class="weapon{unique_id}"></div>
            <div class="headshot"></div>
            <div class="wallbang"></div>
            <a href="" class="killed">storM</a>
        </div>
        </div>
        <div class="container">
        <div class="killFeed">
            <a href="" class="killer">bro you fukin suk</a>
            <div class="weapon{unique_id}"></div>
            <div class="headshot true"></div>
            <div class="wallbang"></div>
            <a href="" class="killed">storM</a>
        </div>
        </div>
        <div class="container">
        <div class="killFeed">
            <a href="" class="killer">HACKS</a>
            <div class="weapon{unique_id}"></div>
            <div class="headshot"></div>
            <div class="wallbang true"></div>
            <a href="" class="killed">storM</a>
        </div>
        </div>
        <div class="container">
        <div class="killFeed">
            <a href="" class="killer">FaZe TrickshoT</a>
            <div class="weapon{unique_id}"></div>
            <div class="headshot true"></div>
            <div class="wallbang true"></div>
            <a href="" class="killed">Mrots</a>
        </div>
        </div>''', unsafe_allow_html=True)

def draw_name_ammo(weapon_name,weapon_ammo):
    ammo_img = './assets/hud_imgs/icon_bullets_default.png'

    hy.markdown(
    """
    <style>
    .container {
        display: flex;
        align-items: center;
    }
    .logo-text {
        font-weight:600 !important;
        font-size:36px !important;
        color: #FAFAFA !important;  
    }
    .ammo-text {
        font-weight:600 !important;
        font-size:16px !important;
        color: #b7ff8a !important;
        padding-left: 5px;
        padding-bottom: 0px;
    }
    .logo-img {
        height: 39px !important;
        padding-left: 10px;
        padding-bottom: 10px;
        -webkit-filter: invert(100%);
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    hy.markdown(
        f"""
        <div class="container">
            <p class="logo-text">
                {weapon_name}<p class="ammo-text"> {weapon_ammo} </p>
            </p>
            <img class="logo-img" title="Ammo" src="data:image/png;base64,{base64.b64encode(open(ammo_img, "rb").read()).decode()}">
        </div>
        """,
        unsafe_allow_html=True
    )