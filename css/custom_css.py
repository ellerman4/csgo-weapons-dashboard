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
            <a href="" class="killer">woxic</a>
            <div class="weapon{unique_id}"></div>
            <div class="headshot"></div>
            <div class="wallbang"></div>
            <a href="" class="killed">electroNic</a>
        </div>
        </div>
        <div class="container">
        <div class="killFeed">
            <a href="" class="killer">paz</a>
            <div class="weapon{unique_id}"></div>
            <div class="headshot true"></div>
            <div class="wallbang"></div>
            <a href="" class="killed">b1t</a>
        </div>
        </div>
        <div class="container">
        <div class="killFeed">
            <a href="" class="killer">s1mple</a>
            <div class="weapon{unique_id}"></div>
            <div class="headshot"></div>
            <div class="wallbang true"></div>
            <a href="" class="killed">electroNic</a>
        </div>
        </div>
        <div class="container">
        <div class="killFeed">
            <a href="" class="killer">XANTARES</a>
            <div class="weapon{unique_id}"></div>
            <div class="headshot true"></div>
            <div class="wallbang true"></div>
            <a href="" class="killed">sdy</a>
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

# Some simple icons for social media
def footer_icons():
    # Footer CSS styles
    hy.markdown(
    """
    <style>
    @import url('//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css');
    a, a:hover {
        text-decoration: none;
    }
    .socialbtns, .socialbtns ul, .socialbtns li {
        margin: 0;
        padding: 5px;
    }
    .socialbtns li {
        list-style: none outside none;
        display: inline-block;
    }
    .socialbtns .fa {
        width: 40px;
        height: 28px;
        color: #fff;
        background-color: #000;
        border: 1px solid #ffffff;
        padding-top: 6px;
        border-radius: 22px;
        -moz-border-radius: 22px;
        -webkit-border-radius: 22px;
        -o-border-radius: 22px;
    }
    .socialbtns .fa:hover {
        color: #000;
        background-color: #ffffff;
        border: 1px solid #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    # Footer HTML
    hy.markdown(
    """
    <div align="center" class="socialbtns">
        <ul>
            <li><a href="https://github.com/ellerman4" class="fa fa-lg fa-github"></a></li>
            <li><a href="https://twitter.com/" class="fa fa-lg fa-twitter"></a></li>
            <li><a href="https://www.linkedin.com/" class="fa fa-lg fa-linkedin"></a></li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
    )