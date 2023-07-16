#In this code, i'll take you on how to create a choropleth map using folium library on jupyter notebook
#the map will show the total of accidents per us counties

# first initiate the libraries
import folium
import json
import pandas as pd
import numpy as np

#Read the data from the path location of the data
accidents = pd.read_csv('The path to the data (/) use backslash!')

#Map 1
#create a dataframe grouped by city that contain total accidents and frequent hour and severity index

groupc = accidents.groupby('County')
most_frequent_hour = groupc['Hourly'].agg(lambda x: x.value_counts().idxmax())
least_frequent_hour = groupc['Hourly'].agg(lambda x: x.value_counts().idxmax())

#hc = Hourly City
hc = pd.DataFrame({
    'Most Frequent Hour': most_frequent_hour,
    'Least Frequent Hour': least_frequent_hour,
})

#create the groupby main dataframe
dfm = accidents.groupby('County').agg(Total_Accidents=("ID", "count"), Severity=("Severity","mean"), Latitude=("Start_Lat", "mean"), Longitude=("Start_Lng", "mean"))

#lambda for loop
dfm['Severity_Index'] = dfm['Severity'].apply(lambda x: 'Low' if x < 3.0 else 'High')
dfm = dfm.drop("Severity", axis = 1)
dfm['Latitude'] = dfm['Latitude'].astype(int)
dfm['Longitude'] = dfm['Longitude'].astype(int)

#merge table
mapdata = dfm.merge(hc, left_index=True, right_index=True)
mapdata = mapdata.reset_index()

#create the map
geojson_data = "geojson file path"

us_map = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

choropleth_layer = folium.Choropleth(
    geo_data=geojson_data,
    name='Accidents in US Counties',
    data=mapdata,
    columns=['County', 'Total_Accidents'],
    key_on='feature.properties.NAME',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Total Accidents',
    highlight=True,
).add_to(us_map)

us_map
mapdata = mapdata.reset_index().rename(columns={mapdata.index.name:'id'})
mapdata
