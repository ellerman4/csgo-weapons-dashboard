import hydralit as hy
import pandas as pd
from charts import render_ring_gauge
from st_aggrid import AgGrid
from css.streamlit_download_button import download_button
from css.custom_css import killfeed, draw_name_ammo, align_justify, footer_icons


if __name__ == '__main__':

    # Function for loading weapon table data
    def get_data_table(weapon_data):
        return pd.read_html(weapon_data['Wiki'], skiprows=1)[0]

    #   Crate a function to create a sort of template for every item passed to it
    #   i.e. https://i.gyazo.com/b1508db3014944302c498398f3251cc5.png
    #   weapon_data will be a multi-row DataFrame, so we will loop through each row
    #   And use the data in said row to create a set of hydralit elements and css/html for each

    def weapon_card(weapon_data):

        align_justify() # CSS for aligning our content

        for index, weapon in weapon_data.iterrows():   # Iterrate through each row (each weapon)
            weapon_name = weapon['Name']               # Get weapon attributes from respective columns
            weapon_img = weapon['Image Path']
            weapon_caption = weapon['Caption']
            weapon_ammo = f"{str(weapon['Clip Size'])}/{str(weapon['Max Ammo'])}"
            weapon_table = get_data_table(weapon)
            weapon_gif = weapon['Gif']
            weapon_cost = str(weapon['Cost'])
            weapon_pen = str(weapon['Armor Penetration'])

            # Clean data tables if needed (some tables are scraped with strange properties)
            if len(weapon_table.columns) > 3:
                weapon_table = weapon_table.iloc[: , :-1]
                weapon_table.columns = weapon_table.columns.droplevel()

            # Create 3 hydralit column elements, for our 'title' row
            # i.e. https://i.gyazo.com/6ecac530686e3f45903c22524e758aff.png
            title_col = hy.columns(3)

            # Call draw_name_ammo, display in first column
            with title_col[0]:
                draw_name_ammo(weapon_name, weapon_ammo)
            
            # Create metric components for cost/armor pen, put in remaining columns
            with title_col[1]:
                hy.metric(
                    label = "Cost",
                    value = weapon_cost,
                    delta = "test")

            with title_col[2]:
                hy.metric(
                    label = "Armor Penetration",
                    value = weapon_pen,
                    delta = "test")

            # Create 5 hydralit column elements, for our 'weapon' row
            # i.e. https://i.gyazo.com/d282e4a73dcd709793de4e37df64ecc4.png
            weapon_col = hy.columns(5)

            with weapon_col[0]:                 # Weapon Image
                hy.image(weapon_img,            # 'with caption'
                        width=260,
                        caption=weapon_caption)

            with weapon_col[1]:
                render_ring_gauge(
                weapon_data = weapon,
                max_dps = weapon_data['DPS'].max(),
                max_rof = weapon_data['RoF'].max(),
                max_recoil = weapon_data['Recoil'].max())  # Ring guage showing DPS, RoF, and Recoil

            with weapon_col[2]:
                hy.dataframe(weapon_table[:-1]) # Damage Table

            with weapon_col[3]:
                hy.image(weapon_gif, width=140) # Spray pattern via gif

            with weapon_col[4]:
                killfeed(weapon)           # Killfeed preview via css/html

            with hy.expander("Trivia"):
                hy.write("""""")

    # Define theme, initiate app with hy.HydraApp
    over_theme = {'txc_inactive': '#FFFFFF'}
    app = hy.HydraApp(
        title='Secure Hydralit Data Explorer',
        favicon="🐙",
        hide_streamlit_markers=True,
        banner_spacing=[5,30,60,30,5],
        use_navbar=True, 
        navbar_sticky=False,
        navbar_theme=over_theme
    )


    # Load our CS:GO weapons data from the csv file
    data = pd.read_csv('./data/CSGO-Weapons-Data.csv')
    data['Cost'] = data['Cost'].astype('str') 


    # Create a homepage
    @app.addapp(is_home=True)
    def my_home():
        hy.title('CS:GO Weapon Stats')
        hy.header('Full dataset')

        # Display the entire csv file on the homepage, available for download
        AgGrid(data.iloc[: , :-5], theme='streamlit',height=500, fit_columns_on_grid_load=True) # data.iloc[: , :-5] to drop columns irrelevant to user

        # Convert dataframe to csv
        @hy.cache()
        def convert_df(data):
            return data.to_csv().encode('utf-8')

        # Load custom download button with a streamlit markdown (re-run workaround)
        hy.markdown(
            download_button(convert_df(data),
            "weapon_stats.csv",
            "Press to Download"),
            unsafe_allow_html=True)

        # Display CS:GO logo on the homepage, align and invert color with CSS hacking
        hy.image("http://vignette3.wikia.nocookie.net/logopedia/images/c/c8/CSGO.png", width=300)
        hy.markdown('<style> .css-1kyxreq { justify-content: center; -webkit-filter: invert(100%); } </style>', unsafe_allow_html=True)

        # Load our neat footer
        footer_icons()


    # Create page for Rifle stats
    @app.addapp(title='Rifles')
    def rifle_stats():
        # Align and justify css with align_justify function
        # Could be implemented in weapon_card function to not repeat ourselves, but creates inefficient loading
        

        # Locate all the data matching 'Rifle' for column ['Type'], assign to rifle data
        # Pass rifle data to our weapon_card function
        rifle_data = data.loc[data['Type'] == 'Rifle']
        weapon_card( weapon_data = rifle_data)


    # Create page for Pistol stats
    @app.addapp(title='Pistols')
    def pistol_stats():
        

        # Locate all the data matching 'Pistol' for column ['Type'], assign to pistol data
        # Pass pistol data to our weapon_card function
        pistol_data = data.loc[data['Type'] == 'Pistol']
        weapon_card( weapon_data = pistol_data)


    # Create page for Shotgun stats
    @app.addapp(title='Shotguns')
    def shotgun_stats():
        

        # Locate all the data matching 'Shotgun' for column ['Type'], assign to shotgun data
        # Pass shotgun data to our weapon_card function
        shotgun_data = data.loc[data['Type'] == 'Shotgun']
        weapon_card( weapon_data = shotgun_data)


    # Create page for SMG stats
    @app.addapp(title='SMGs')
    def smg_stats():
        

        # Locate all the data matching 'SMG' for column ['Type'], assign to smg data
        # Pass smg data to our weapon_card function
        smg_data = data.loc[data['Type'] == 'SMG']
        weapon_card( weapon_data = smg_data)


    # Create page for Sniper Rifle stats
    @app.addapp(title='Sniper Rifles')
    def sniper_rifle_stats():
        

        # Locate all the data matching 'Sniper Rifle' for column ['Type'], assign to sniper data
        # Pass sniper data to our weapon_card function
        sniper_data = data.loc[data['Type'] == 'Sniper Rifle']
        weapon_card( weapon_data = sniper_data)


    # Create page for Machine Gun stats
    @app.addapp(title='Machine Guns')
    def machine_gun_stats():
        

        # Locate all the data matching 'MG' for column ['Type'], assign to mg data
        # Pass mg data to our weapon_card function
        mg_data = data.loc[data['Type'] == 'MG']
        weapon_card( weapon_data = mg_data)

    # Run the whole lot
    app.run()