[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ellerman4-csgo-weapons-dashboard-app-l3k5mr.streamlitapp.com/)
# Overview
A simple streamlit application for visualizing weapon data from [Counter Strike:Global Offensive](https://store.steampowered.com/app/730/CounterStrike_Global_Offensive/) with:

- Recoil, RoF, and DPS percentages, relative to max values by weapon type
- Spray pattern visualization
- Armored/Unarmored damage stats by hit area
- Killfeed preview via some basic css

![ff03d412307ab50a65c6ba4c13a53644](https://user-images.githubusercontent.com/106990217/183538534-b5d63517-6e58-4d2c-9b9f-68cd61e15621.png)

## Usage
1.  Clone repository
2.  Install dependencies (listed below)
3.  Initialize a local Streamlit server with the command:
```python
streamlit run app.py
```

## Requirements
```python
hydralit==1.0.13
hydralit_components==1.0.10
pandas==1.4.2
streamlit==1.10.0
streamlit_echarts==0.4.0
streamlit-aggrid==0.2.3
```

## Acknowledgments
Original dataset from [kaggle](https://www.kaggle.com/datasets/vatsalparsaniya/csgo-weapons)
