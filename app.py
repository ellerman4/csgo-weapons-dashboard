#when we import hydralit, we automatically get all of Streamlit
import hydralit as hy
import hydralit_components as hc
import pandas as pd
from streamlit_echarts import st_echarts
from charts import render_ring_gauge
from st_aggrid import AgGrid
from css.streamlit_download_button import download_button
from css.killfeed_css import killfeed
import base64

def title_card(weapon_data, weapon_name, weapon_img, weapon_caption,weapon_table, weapon_gif):
    if [weapon_data['Team'] == 'CT']:
        team_img = './assets/hud_imgs/logo_CT_default.png'
    elif [weapon_data['Team'] == 'T']:
        team_img = './assets/hud_imgs/logo_T_default.png'

    title_col = hy.columns(3)
    with title_col[0]:
        # Some css hacking
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
            .logo-img {
                height: 39px !important;
                padding-left: 10px;
                padding-bottom: 10px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        hy.markdown(
            f"""
            <div class="container">
                <p class="logo-text">
                    {weapon_name} 
                </p>
                <img class="logo-img" title="Team" src="data:image/png;base64,{base64.b64encode(open(team_img, "rb").read()).decode()}">
            </div>
            """,
            unsafe_allow_html=True
        )

    with title_col[1]:
        hy.metric(
            label="Cost",
            value=str(weapon_data['Cost'].values[0]),
            delta="test")

    with title_col[2]:
        hy.metric(
            label="Armor Penetration",
            value=str(weapon_data['Armor Penetration'].values[0]),
            delta="test")

    weapon_col = hy.columns(5)
    with weapon_col[0]:
        hy.image(f'./assets/weapon_imgs/{weapon_img}',
                width=260,
                caption=weapon_caption)

    with weapon_col[1]:
        render_ring_gauge(weapon_data)

    with weapon_col[2]:
        hy.dataframe(weapon_table[:-1])

    with weapon_col[3]:
        hy.image(weapon_gif, width=140)

    with weapon_col[4]:
        killfeed(weapon_data)


    with hy.expander("Trivia"):
        hy.write("""""")

if __name__ == '__main__':
    data = pd.read_csv('./data/CSGO-Weapons-Data.csv')
    data['Cost'] = data['Cost'].astype('str') 

    # Load weapon data individually
    aug_data = data.loc[data['Name'] == 'AUG']



    over_theme = {'txc_inactive': '#FFFFFF'}
    app = hy.HydraApp(
        title='Secure Hydralit Data Explorer',
        favicon="🐙",
        hide_streamlit_markers=True,
        #add a nice banner, this banner has been defined as 5 sections with spacing defined by the banner_spacing array below. 
        banner_spacing=[5,30,60,30,5],
        use_navbar=True, 
        navbar_sticky=False,
        navbar_theme=over_theme
    )

    # Create a homepage
    @app.addapp(is_home=True)
    def my_home():
        
        hy.title('This is a title')

        AgGrid(data, theme='streamlit',height=500, fit_columns_on_grid_load=True)

        # Convert dataframe to csv
        @hy.cache()
        def convert_df(data):
            return data.to_csv().encode('utf-8')

        hy.markdown(
            download_button(convert_df(data), "weapon_stats.csv", "Press to Download"),     # Load custom download button with a streamlit markdown (re-run workaround)
            unsafe_allow_html=True)

        hy.image("http://vignette3.wikia.nocookie.net/logopedia/images/c/c8/CSGO.png", width=300)
        hy.markdown('<style> .css-1kyxreq { justify-content: center; -webkit-filter: invert(100%); } </style>', unsafe_allow_html=True) 

    # Create page for Rifle stats
    @app.addapp(title='Rifles')
    def rifle_stats():
        hy.markdown('<style> .etr89bj1 > img { border-radius: 25px; } </style>', unsafe_allow_html=True)
        hy.markdown('<style> .css-ocqkz7 { align-items: center; } </style>', unsafe_allow_html=True)
        hy.markdown('<style> .css-1kyxreq { justify-content: center; } </style>', unsafe_allow_html=True)

        ### Load M4A1-S data ###
        m4a1_data = data.loc[data['Name'] == 'M4A4-S']
        m4a1_table = pd.read_html('https://counterstrike.fandom.com/wiki/M4A1-S', skiprows=1)[0]

        title_card( weapon_data = m4a1_data,
            weapon_name = 'm4a1-s',
            weapon_img = 'm4a1s.png',
            weapon_caption = '''“With a smaller magazine than its
                                unmuffled counterpart, the silenced M4A1
                                provides quieter shots with less recoil and
                                better accuracy.”''',
            weapon_table = m4a1_table,
            weapon_gif = 'https://i.imgur.com/xsGKrzZ.gif')

        ### Load M4A4 data ###
        m4a4_data = data.loc[data['Name'] == 'M4A4']
        m4a4_table = pd.read_html('https://counterstrike.fandom.com/wiki/M4A4', skiprows=1)[0]

        title_card( weapon_data = m4a4_data,
            weapon_name = 'm4a4',
            weapon_img = 'm4a4.png',
            weapon_caption = '''“More accurate but less damaging
                                than its AK-47 counterpart, the M4A4
                                is the full-auto assault rifle of choice for CTs.”''',
            weapon_table = m4a4_table,
            weapon_gif = 'https://i.imgur.com/YHESoX4.gif')

        ### Load AK-47 data ###
        ak_data = data.loc[data['Name'] == 'AK-47']
        ak_table = pd.read_html('https://counterstrike.fandom.com/wiki/AK-47', skiprows=2)[0].drop(columns=['Unnamed: 3_level_0'])

        title_card( weapon_data = ak_data,
            weapon_name = 'ak-47',
            weapon_img = 'ak_47.png',
            weapon_caption = '''“Powerful and reliable, the AK-47 is one of
                                the most popular assault rifles in the world.
                                It is most deadly in short, controlled bursts
                                of fire.”''',
            weapon_table = ak_table,
            weapon_gif = 'https://i.imgur.com/D3nGgG8.gif')

        ### Load Famas data ###
        famas_data = data.loc[data['Name'] == 'FAMAS']
        famas_table = pd.read_html('https://counterstrike.fandom.com/wiki/FAMAS', skiprows=1)[0]

        title_card( weapon_data = famas_data,
            weapon_name = 'famas',
            weapon_img = 'famas.png',
            weapon_caption = '''“A cheap option for cash-strapped players,
                                the FAMAS effectively fills the niche between
                                more expensive rifles and the less-effective SMGs.”''',
            weapon_table = famas_table,
            weapon_gif = 'https://i.imgur.com/yUM6pou.gif')

        ### Load Galil data ###
        galil_data = data.loc[data['Name'] == 'Galil AR']
        galil_table = pd.read_html('https://counterstrike.fandom.com/wiki/Galil_AR', skiprows=1)[0]

        title_card( weapon_data = galil_data,
            weapon_name = 'galil',
            weapon_img = 'galil.png',
            weapon_caption = '''“A less expensive option among the
                                terrorist-exclusive assault rifles, the
                                Galil AR is a serviceable weapon in medium to long-range combat.”''',
            weapon_table = galil_table,
            weapon_gif = 'https://i.imgur.com/ktrFt2U.gif')

        ### Load AUG data ###
        aug_data = data.loc[data['Name'] == 'AUG']
        aug_table = pd.read_html('https://counterstrike.fandom.com/wiki/AUG', skiprows=2)[0].drop(columns=['Unnamed: 3_level_0'])

        title_card( weapon_data = aug_data,
            weapon_name = 'aug',
            weapon_img = 'aug.png',
            weapon_caption = '''“Powerful and accurate, the AUG
                                scoped assault rifle compensates for
                                its long reload times with low spread
                                and a high rate of fire.”''',
            weapon_table = aug_table,
            weapon_gif = 'https://i.imgur.com/hkPyZ6O.gif')

        ### Load SG data ###
        sg_data = data.loc[data['Name'] == 'SG 553']
        sg_table = pd.read_html('https://counterstrike.fandom.com/wiki/SG_553', skiprows=1)[0]

        title_card( weapon_data = sg_data,
            weapon_name = 'sg-553',
            weapon_img = 'sg553.png',
            weapon_caption = '''“The terrorist-exclusive SG 553 is
                                a premium scoped alternative to the AK-47
                                for effective long-range engagement.”''',
            weapon_table = sg_table,
            weapon_gif = 'https://i.imgur.com/H8o6Hyo.gif')

    # Create page for pistol stats
    @app.addapp(title='Pistols')
    def pistol_stats():
        hy.markdown('<style> .etr89bj1 > img { border-radius: 25px; } </style>', unsafe_allow_html=True)
        hy.markdown('<style> .css-ocqkz7 { align-items: center; } </style>', unsafe_allow_html=True)
        hy.markdown('<style> .css-1kyxreq { justify-content: center; } </style>', unsafe_allow_html=True)

        ### Load USP-S data ###
        usp_data = data.loc[data['Name'] == 'USP-S']
        usp_table = pd.read_html('https://counterstrike.fandom.com/wiki/USP-S', skiprows=1)[0]

        title_card( weapon_data=usp_data,
            weapon_name = 'usp-s',
            weapon_img = 'usp-s.png',
            weapon_caption = '''“A fan favorite from Counter-Strike: Source,
                                the Silenced USP Pistol has a detachable
                                silencer that gives shots less recoil while
                                suppressing attention-getting noise.”''',
            weapon_table=usp_table,
            weapon_gif = 'https://i.imgur.com/QabkWlI.gif')

        ### Load Glock-18 data ###
        glock_data = data.loc[data['Name'] == 'Glock 18']
        glock_table = pd.read_html('https://counterstrike.fandom.com/wiki/Glock-18', skiprows=2)[0].drop(columns=['Unnamed: 3_level_0'])

        title_card( weapon_data=glock_data,
            weapon_name = 'glock-18',
            weapon_img = 'glock-18.png',
            weapon_caption = '''“The Glock 18 is a serviceable first-round
                            pistol that works best against unarmored opponents
                            and is capable of firing three-round bursts.”''',
            weapon_table=glock_table,
            weapon_gif = 'https://i.imgur.com/DGCO8PG.gif')



        #### Load Desert Eagle data ###
        deag_data = data.loc[data['Name'] == 'Desert Eagle']
        deag_table = pd.read_html('https://counterstrike.fandom.com/wiki/Desert_Eagle', skiprows=2)[0].drop(columns=['Unnamed: 3_level_0'])

        title_card( weapon_data = deag_data,
                    weapon_name = 'desert eagle',
                    weapon_img = 'deag.png',
                    weapon_caption = '''“As expensive as it is powerful, the Desert
                                Eagle is an iconic pistol that is difficult to
                                master but surprisingly accurate at long
                                range.”''',
                    weapon_table = deag_table,
                    weapon_gif = "https://i.imgur.com/mAL8MSF.gif")

        #### Load tec-9 data ###
        tec_data = data.loc[data['Name'] == 'Tec-9']
        tec_table = pd.read_html('https://counterstrike.fandom.com/wiki/Tec-9', skiprows=1)[0]

        title_card( weapon_data = tec_data,
            weapon_name = 'tec-9',
            weapon_img = 'tec-9.png',
            weapon_caption = '''“An ideal pistol for the Terrorist on the
                    move, the Tec-9 is lethal in close quarters
                    and features a high magazine capacity.”''',
            weapon_table = tec_table,
            weapon_gif = 'https://i.imgur.com/9ZLYpiu.gif')

        #### Load Five-Seven data ###
        five_seven_data = data.loc[data['Name'] == 'Five-SeveN']
        five_seven_table = pd.read_html('https://counterstrike.fandom.com/wiki/Five-SeveN', skiprows=2)[0].drop(columns=['Unnamed: 3_level_0'])

        title_card( weapon_data = five_seven_data,
            weapon_name = 'five-seven',
            weapon_img = 'five-seven.png',
            weapon_caption = '''“Highly accurate and armor-piercing, the
                                pricy Five-Seven is a slow-loader that
                                compensates with a generous 20-round
                                magazine and forgiving recoil.”''',
            weapon_table = five_seven_table,
            weapon_gif = 'https://i.imgur.com/PZHCHHy.gif')

        #### Load p-2000 data ###
        p2000_data = data.loc[data['Name'] == 'P2000']
        p2000_table = pd.read_html('https://counterstrike.fandom.com/wiki/P2000', skiprows=1)[0]

        title_card( weapon_data = p2000_data,
            weapon_name = 'p-2000',
            weapon_img = 'p2k.png',
            weapon_caption = '''“Accurate and controllable, the German-made
                                P2000 is a serviceable first-round pistol
                                that works best against unarmored opponents.”''',
            weapon_table = p2000_table,
            weapon_gif = 'https://i.imgur.com/Chfo1a9.gif')

        #### Load p-250 data ###
        p250_data = data.loc[data['Name'] == 'P250']
        p250_table = pd.read_html('https://counterstrike.fandom.com/wiki/P250', skiprows=1)[0]

        title_card( weapon_data = p250_data,
            weapon_name = 'p-250',
            weapon_img = 'p250.png',
            weapon_caption = '''“A low-recoil firearm with a high
                                rate of fire, the P250 is a relatively
                                inexpensive choice against armored opponents.”''',
            weapon_table = p250_table,
            weapon_gif = 'https://i.imgur.com/9YnhFca.gif')

        #### Load cz-75 data ###
        cz75_data = data.loc[data['Name'] == 'CZ75 Auto']
        cz75_table = pd.read_html('https://counterstrike.fandom.com/wiki/CZ75-Auto', skiprows=1)[0]

        title_card( weapon_data = cz75_data,
            weapon_name = 'cz-75',
            weapon_img = 'cz75.png',
            weapon_caption = '''“A fully automatic variant of the CZ75,
                                the CZ75-Auto is another inexpensive choice against
                                armored opponents. But with very little ammo provided,
                                strong trigger discipline is required.”''',
            weapon_table = cz75_table,
            weapon_gif = 'https://i.imgur.com/3FqJC8p.gif')

    # Create page for Shotgun stats
    @app.addapp(title='Shotguns')
    def shotgun_stats():
        hy.markdown('<style> .etr89bj1 > img { border-radius: 25px; } </style>', unsafe_allow_html=True)
        hy.markdown('<style> .css-ocqkz7 { align-items: center; } </style>', unsafe_allow_html=True)
        hy.markdown('<style> .css-1kyxreq { justify-content: center; } </style>', unsafe_allow_html=True)

        ### Load xm1014 data ###
        xm1014_data = data.loc[data['Name'] == 'XM1014']
        xm1014_table = pd.read_html('https://counterstrike.fandom.com/wiki/XM1014', skiprows=2)[0].drop(columns=['Unnamed: 3_level_0'])

        title_card( weapon_data = xm1014_data,
            weapon_name = 'xm1014',
            weapon_img = 'xm1014.png',
            weapon_caption = '''“The XM1014 is a powerful fully
                                automatic shotgun that justifies its
                                heftier price tag with the ability to
                                paint a room with lead fast.”''',
            weapon_table = xm1014_table,
            weapon_gif = 'https://i.imgur.com/sdZLdDA.gif')

        ### Load nova data ###
        nova_data = data.loc[data['Name'] == 'Nova']
        nova_table = pd.read_html('https://counterstrike.fandom.com/wiki/Nova', skiprows=1)[0]

        title_card( weapon_data = nova_data,
            weapon_name = 'nova',
            weapon_img = 'nova.png',
            weapon_caption = '''“The Nova's rock-bottom price
                                tag makes it a great ambush weapon
                                for a cash-strapped team.”''',
            weapon_table = nova_table,
            weapon_gif = 'https://i.imgur.com/8wXNfoP.gif')

        ### Load mag-7 data ###
        mag7_data = data.loc[data['Name'] == 'MAG-7']
        mag7_table = pd.read_html('https://counterstrike.fandom.com/wiki/MAG-7', skiprows=1)[0]

        title_card( weapon_data = mag7_data,
            weapon_name = 'mag-7',
            weapon_img = 'mag7.png',
            weapon_caption = '''“The CT-exclusive Mag-7 delivers
                                a devastating amount of damage at close range.
                                Its rapid magazine-style reloads make it a great tactical choice.”''',
            weapon_table = mag7_table,
            weapon_gif = 'https://i.imgur.com/rewtmie.gif')

        ### Load sawed-off data ###
        sawed_off_data = data.loc[data['Name'] == 'Sawed-Off']
        sawed_off_table = pd.read_html('https://counterstrike.fandom.com/wiki/Sawed-Off', skiprows=1)[0]

        title_card( weapon_data = sawed_off_data,
            weapon_name = 'sawed-off',
            weapon_img = 'sawedoff.png',
            weapon_caption = '''“The classic Sawed-Off deals very heavy
                                close-range damage, but with its low accuracy,
                                high spread and slow rate of fire, you'd better kill what you hit.”''',
            weapon_table = sawed_off_table,
            weapon_gif = 'https://i.imgur.com/tA5TkUI.gif')

    # Create page for SMG stats
    @app.addapp(title='SMGs')
    def smg_stats():
        hy.markdown('<style> .etr89bj1 > img { border-radius: 25px; } </style>', unsafe_allow_html=True)
        hy.markdown('<style> .css-ocqkz7 { align-items: center; } </style>', unsafe_allow_html=True)
        hy.markdown('<style> .css-1kyxreq { justify-content: center; } </style>', unsafe_allow_html=True)

        ### Load mp9 data ###
        mp9_data = data.loc[data['Name'] == 'MP9']
        mp9_table = pd.read_html('https://counterstrike.fandom.com/wiki/MP9', skiprows=1)[0]

        title_card( weapon_data = mp9_data,
            weapon_name = 'mp-9',
            weapon_img = 'mp9.png',
            weapon_caption = '''“Manufactured in Switzerland, the cutting-edge
                                MP9 SMG is an ergonomic polymer weapon favored
                                by private security firms.”''',
            weapon_table = mp9_table,
            weapon_gif = 'https://i.imgur.com/XqAoqKQ.gif')

        ### Load mac10 data ###
        mac10_data = data.loc[data['Name'] == 'MAC-10']
        mac10_table = pd.read_html('https://counterstrike.fandom.com/wiki/MAC-10', skiprows=2)[0].drop(columns=['Unnamed: 3_level_0'])

        title_card( weapon_data = mac10_data,
            weapon_name = 'mac-10',
            weapon_img = 'mac10.png',
            weapon_caption = '''“Essentially a box that bullets come out of,
                                the MAC-10 SMG boasts a high rate of fire,
                                with poor spread accuracy and high recoil as trade-offs.”''',
            weapon_table = mac10_table,
            weapon_gif = 'https://i.imgur.com/TK9M1zs.gif')

        ### Load pp-bizon data ###
        bizon_data = data.loc[data['Name'] == 'PP-Bizon']
        bizon_table = pd.read_html('https://counterstrike.fandom.com/wiki/PP-Bizon', skiprows=1)[0]

        title_card( weapon_data = bizon_data,
            weapon_name = 'pp-bizon',
            weapon_img = 'bizon.png',
            weapon_caption = '''“The Bizon SMG is low-damage,
                                but offers a uniquely designed high-capacity
                                drum magazine that reloads quickly.”''',
            weapon_table = bizon_table,
            weapon_gif = 'https://i.imgur.com/X7EcSI2.gif')

        ### Load mp7 data ###
        mp7_data = data.loc[data['Name'] == 'MP7']
        mp7_table = pd.read_html('https://counterstrike.fandom.com/wiki/MP7', skiprows=1)[0]

        title_card( weapon_data = mp7_data,
            weapon_name = 'mp-7',
            weapon_img = 'mp7.png',
            weapon_caption = '''“Versatile but expensive, the German-made
                                MP7 SMG is the perfect choice for high-impact
                                close-range combat.”''',
            weapon_table = mp7_table,
            weapon_gif = 'https://i.imgur.com/chamBRP.gif')

        ### Load ump45 data ###
        ump_data = data.loc[data['Name'] == 'UMP-45']
        ump_table = pd.read_html('https://counterstrike.fandom.com/wiki/UMP-45', skiprows=2)[0].drop(columns=['Unnamed: 3_level_0'])

        title_card( weapon_data = ump_data,
            weapon_name = 'ump-45',
            weapon_img = 'ump45.png',
            weapon_caption = '''“The misunderstood middle child of the SMG
                                family, the UMP45's small magazine is the only
                                drawback to an otherwise versatile close-quarters automatic.”''',
            weapon_table = ump_table,
            weapon_gif = 'https://i.imgur.com/b08tglg.gif')

        ### Load p90 data ###
        p90_data = data.loc[data['Name'] == 'P90']
        p90_table = pd.read_html('https://counterstrike.fandom.com/wiki/P90', skiprows=2)[0].drop(columns=['Unnamed: 3_level_0'])

        title_card( weapon_data = p90_data,
            weapon_name = 'p90',
            weapon_img = 'p90.png',
            weapon_caption = '''“Easily recognizable for its unique bullpup design,
                                the P90 is a great weapon to shoot on the move due to
                                its high-capacity magazine and low recoil.”''',
            weapon_table = p90_table,
            weapon_gif = 'https://i.imgur.com/WFEOWDz.gif')

    # Create page for sniper rifle stats
    @app.addapp(title='Sniper Rifles')
    def sniper_rifle_stats():
        hy.markdown('<style> .etr89bj1 > img { border-radius: 25px; } </style>', unsafe_allow_html=True)
        hy.markdown('<style> .css-ocqkz7 { align-items: center; } </style>', unsafe_allow_html=True)
        hy.markdown('<style> .css-1kyxreq { justify-content: center; } </style>', unsafe_allow_html=True)

        ### Load awp data ###
        awp_data = data.loc[data['Name'] == 'AWP']
        awp_table = pd.read_html('https://counterstrike.fandom.com/wiki/M249', skiprows=2)[0].drop(columns=['Unnamed: 3_level_0'])

        title_card( weapon_data = awp_data,
            weapon_name = 'awp',
            weapon_img = 'awp.png',
            weapon_caption = '''“High risk and high reward, the
                                infamous AWP is recognizable by its signature
                                report and one-shot, one-kill policy.”''',
            weapon_table = awp_table,
            weapon_gif = 'https://i.imgur.com/H10Mzp9.gif')

        ### Load ssg08 data ###
        ssg_data = data.loc[data['Name'] == 'SSG 08']
        ssg_table = pd.read_html('https://counterstrike.fandom.com/wiki/SSG_08', skiprows=1)[0]

        title_card( weapon_data = ssg_data,
            weapon_name = 'ssg08',
            weapon_img = 'ssg08.png',
            weapon_caption = '''“The SSG 08 bolt-action is a low-damage
                                but very cost-effective sniper rifle,
                                making it a smart choice for early-round
                                long-range marksmanship.”''',
            weapon_table = ssg_table,
            weapon_gif = 'https://i.imgur.com/qu19Z82.gif')

        ### Load ssg08 data ###
        scar_data = data.loc[data['Name'] == 'SCAR-20']
        scar_table = pd.read_html('https://counterstrike.fandom.com/wiki/SCAR-20', skiprows=1)[0]

        title_card( weapon_data = scar_data,
            weapon_name = 'scar-20',
            weapon_img = 'scar.png',
            weapon_caption = '''“The SCAR-20 is a semi-automatic sniper rifle
                                that trades a high rate of fire and powerful
                                long-distance damage for sluggish movement speed
                                and big price tag.”''',
            weapon_table = scar_table,
            weapon_gif = 'https://i.imgur.com/1eHHN35.gif')

        ### Load ssg08 data ###
        g3sg1_data = data.loc[data['Name'] == 'G3SG1']
        g3sg1_table = pd.read_html('https://counterstrike.fandom.com/wiki/G3SG1', skiprows=1)[0]

        title_card( weapon_data = g3sg1_data,
            weapon_name = 'g3sg1',
            weapon_img = 'g3sg1.png',
            weapon_caption = '''“The pricy G3SG1 lowers movement
                                speed considerably but compensates with a
                                higher rate of fire than other sniper rifles.”''',
            weapon_table = g3sg1_table,
            weapon_gif = 'https://i.imgur.com/ebwGutS.gif')

    # Create page for machine gun stats
    @app.addapp(title='Machine Guns')
    def machine_gun_stats():
        hy.markdown('<style> .etr89bj1 > img { border-radius: 25px; } </style>', unsafe_allow_html=True)
        hy.markdown('<style> .css-ocqkz7 { align-items: center; } </style>', unsafe_allow_html=True)
        hy.markdown('<style> .css-1kyxreq { justify-content: center; } </style>', unsafe_allow_html=True)

        ### Load USP-S data ###
        m249_data = data.loc[data['Name'] == 'M249']
        m249_table = pd.read_html('https://counterstrike.fandom.com/wiki/M249', skiprows=2)[0].drop(columns=['Unnamed: 3_level_0'])

        title_card( weapon_data = m249_data,
            weapon_name = 'm249',
            weapon_img = 'm249.png',
            weapon_caption = '''“A strong open-area LMG, the M249
                                is the perfect choice for players willing
                                to trade a slow fire rate for increased accuracy
                                and a high ammo capacity.”''',
            weapon_table = m249_table,
            weapon_gif = 'https://i.imgur.com/2jy80nn.gif')

        ### Load USP-S data ###
        negev_data = data.loc[data['Name'] == 'Negev']
        negev_table = pd.read_html('https://counterstrike.fandom.com/wiki/Negev', skiprows=1)[0]

        title_card( weapon_data = negev_data,
            weapon_name = 'negev',
            weapon_img = 'negev.png',
            weapon_caption = '''“The Negev is a beast that can keep the
                                enemy at bay with its pin-point supressive fire,
                                provided you have the luxury of time to gain control over it.”''',
            weapon_table = negev_table,
            weapon_gif = 'https://i.imgur.com/OVNosQn.gif')

    #Run the whole lot, we get navbar, state management and app isolation, all with this tiny amount of work.
    app.run()