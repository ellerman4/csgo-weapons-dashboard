from streamlit_echarts import st_echarts
import random
import string
import pandas as pd

def render_ring_gauge(weapon_data, max_dps, max_rof, max_recoil):

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
                        "value": round((int(weapon_data['DPS'])/max_dps)*100),
                        "name": "DPS",
                        "title": {"offsetCenter": ["0%", "35%"], "color": '#FAFAFA'},
                        "detail": {"offsetCenter": ["0%", "51%"],},
                    },
                    {
                        "value": round((int(weapon_data['RoF'])/max_rof)*100),
                        "name": "RoF",
                        "title": {"offsetCenter": ["0%", "-5%"], "color": '#FAFAFA'},
                        "detail": {"offsetCenter": ["0%", "11%"]},
                    },
                    {
                        "value": round((int(weapon_data['Recoil'])/max_recoil)*100),
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
                    "formatter": "{value}%",
                },
            }
        ]
    }

    st_echarts(option, height="300px", key = ''.join(random.choice(string.ascii_lowercase) for i in range(12)))