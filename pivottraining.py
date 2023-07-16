#In this code, i'll take you on how to create a new dataframe on jupyter notebook
#We will create a new dataframe that contains month-tren based on year
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

#For this table, first create a column in main table that contains monthly value classified
accidents['Month'] = accidents['Start_Time'].dt.month_name() 
accidents['Year'] = accidents['Start_Time'].dt.year

# Group by 'Year' and 'Month' and calculate the total count
monthly_counts = accidents.groupby(['Year', 'Month']).agg(NumberofAccidents=("ID", "count"))

#Reshape the table using pivot command
pivot_monthly = monthly_counts.pivot_table(index='Year', columns='Month', values='NumberofAccidents', fill_value=0)
pivot_monthly
