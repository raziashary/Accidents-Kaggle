#In this code, i'll take you on how to create a heatmap using folium library on jupyter notebook
#the map will show the concentration of the accidents happened in the area

# first initiate the libraries
import folium
import json
import pandas as pd
import numpy as np

#Read the data from the path location of the data
accidents = pd.read_csv('The path to the data (/) use backslash!')

from folium.plugins import HeatMap

#creating table for total accidents
dfhm = accidents.groupby(["Start_Lat", "Start_Lng"]).agg(Total_Accidents=("ID", "count"))
#create the classification which states that if 3 or less accidents happened in the coordinates will mean the area have the low severity stated by 1 and so on
dfhm['Classification'] = dfhm['Total_Accidents'].apply(lambda x: '1' if x <= 3.0 else '2' if 4 <= x <= 10 else '3')
dfhm = dfhm.drop("Total_Accidents", axis = 1).reset_index()
dfhm['Classification'] = dfhm['Classification'].astype(int)

baseheat = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

HeatMap(dfhm, 
        min_opacity=0.4,
        blur = 18
               ).add_to(folium.FeatureGroup(name='Heat Map').add_to(baseheat))
folium.LayerControl().add_to(baseheat)
baseheat
