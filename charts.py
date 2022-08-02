#when we import hydralit, we automatically get all of Streamlit
import hydralit as hy
import hydralit_components as hc
import pandas as pd
from streamlit_echarts import st_echarts
import random
import string

def render_ring_gauge(*args):

    weapon_data = args[0]

    option = {
        "series": [
            {
                "type": "gauge",
                "startAngle": 90,
                "endAngle": -270,
                "pointer": {"show": False},
                "progress": {
                    "show": True,
                    "overlap": False,
                    "roundCap": True,
                    "clip": False,
                    "itemStyle": {"borderWidth": 1, "borderColor": "#464646"},
                },
                "axisLine": {"lineStyle": {"width": 22}},
                "splitLine": {"show": False, "distance": 0, "length": 10},
                "axisTick": {"show": False},
                "axisLabel": {"show": False, "distance": 50},
                "data": [
                    {
                        "value": (int(weapon_data['DPS'])/583)*100,
                        "name": "DPS",
                        "title": {"offsetCenter": ["0%", "35%"], "color": '#FAFAFA'},
                        "detail": {"offsetCenter": ["0%", "51%"],
                        "formatter": f"{int(weapon_data['DPS'])}"},
                    },
                    {
                        "value": round((int(weapon_data['RoF'])/1000)*100),
                        "name": "RoF",
                        "title": {"offsetCenter": ["0%", "-5%"], "color": '#FAFAFA'},
                        "detail": {"offsetCenter": ["0%", "11%"]},
                        "formatter": f"{int(weapon_data['RoF'])}"
                    },
                    {
                        "value": int(weapon_data['Recoil']),
                        "name": "Recoil",
                        "title": {"offsetCenter": ["0%", "-50%"], "color": '#FAFAFA'},
                        "detail": {"offsetCenter": ["0%", "-34%"]},
                    },
                ],
                #"title": {"fontSize": 14},
                "detail": {
                    "width": 50,
                    "height": 9,
                    "fontSize": 13,
                    "color": '#FAFAFA',
                    "borderColor": "auto",
                    "borderRadius": 20,
                    "borderWidth": 1,
                    #"formatter": "{value}%",
                },
            }
        ]
    }

    st_echarts(option, height="300px", key = ''.join(random.choice(string.ascii_lowercase) for i in range(12)))