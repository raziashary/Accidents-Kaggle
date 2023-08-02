#Import the libraries
import folium
import json
import pandas as pd
import numpy as np
from math import pi

#import bokeh library for visualization
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.palettes import Category20c
from bokeh.transform import cumsum
output_notebook()

#import the accidents data from local
accidents = pd.read_csv('data/path')

#making the yearly and hourly column from the start time column
accidents['Start_Time'] = pd.to_datetime(accidents['Start_Time'])
accidents['Hourly'] = accidents['Start_Time'].dt.month_name()
accidents['Year'] = accidents['Start_Time'].dt.year

# Group by 'Year' and 'Month' and calculate the total count
monthly_counts = accidents.groupby(['Year', 'Month']).agg(NumberofAccidents=("ID", "count"))

#Reshape the table using pivot command
pivot_monthly = monthly_counts.pivot_table(index='Year', columns='Month', values='NumberofAccidents', fill_value=0)

#create a pie chart
pivot_monthly.drop(pivot_monthly.iloc[:, 0:4], inplace=True, axis=1)
pivot_monthly.drop(pivot_monthly.iloc[:, 1:9], inplace=True, axis=1)
data = pivot_monthly.reset_index()

data['angle'] = data['January']/data['January'].sum() * 2*pi
data['color'] = Category20c[len(data['Year'].unique())]

p = figure(height=350, title="Accidents Pie Chart", toolbar_location=None,
           tools="hover", tooltips="@Year: @January", x_range=(-0.5, 1.0))

p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='Year', source=data)

p.axis.axis_label = None
p.axis.visible = False
p.grid.grid_line_color = None

show(p)
