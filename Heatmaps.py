
from folium.plugins import HeatMap

#creating table for total accidents
dfhm = accidents.groupby(["Start_Lat", "Start_Lng"]).agg(Total_Accidents=("ID", "count"))
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
