#In this code, i'll take you on how to create a histogram visualization using bokeh library on jupyter notebook
#the histogram will show the total accidents that happened in the US hourly only from 2021 - 2023, hope this helps!
#The data that is used in this training is the accidents data from kaggle, here's the link: https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents
#each paragraph break means a different cell code (recommended)

# first initiate the libraries
import pandas as pd
import numpy as np
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
output_notebook()

#Read the data from the path location of the data
accidents = pd.read_csv('The path to the data (/) use backslash!')
pd.set_option('display.max_columns', None) #this will display all the columns of the dataframe along with the contents
accidents #this will display the dataframe

#first create the hourly column
accidents['Start_Time'] = pd.to_datetime(accidents['Start_Time'])
accidents['Hourly'] = accidents['Start_Time'].dt.hour 
#removing data other than 2021 - 2023
start_date = pd.to_datetime('2021-01-01')
end_date = pd.to_datetime('2023-12-31')
filtered2123 = accidents[(accidents['Start_Time'] >= start_date) & (accidents['Start_Time'] <= end_date)] #this line will slice the data accordingly to the condition we apply
filtered2123

#tah = total accidents hourly
tah = filtered2123.groupby("Hourly").agg(Total_Accidents=("ID", "count"), Severity=("Severity", "mean"))

#Using lambda for looping
tah['Severity_Index'] = tah['Severity'].apply(lambda x: 'Low' if x < 3.0 else 'High')

#below is an example of looping not using lambda, works the same!
#creating the index using looping by for
#Severity_Index= []
#for row in tah['Severity']:
#    if row < 3.0: Severity_Index.append('Low')
#    else: Severity_Index.append('High')
#tah['Severity_Index'] = Severity_Index

#removing severity column
tah = tah.drop("Severity", axis=1)
tah = tah.reset_index()
tah

#tah histogram visualization
p = figure(width=800, height=400, title="Distribution of Accidents Hourly")

hourly_data = tah['Hourly']  # Hourly column
accidents_data = tah['Total_Accidents']  # Accidents column

# Create a Bokeh figure
histogram = figure(
    title='Accidents by Hour',
    x_axis_label='Hour',
    y_axis_label='Number of Accidents',
    tools='hover',
    tooltips=[('Hour', '@right'), ('Accidents', '@top')],
    width=600,
    height=400,
)

# Create the histogram
histogram.quad(
    top=accidents_data,
    bottom=0,
    left=hourly_data - 0.5,
    right=hourly_data + 0.5,
    fill_color='steelblue',
    line_color='black',
)

# Show the histogram
show(histogram)


