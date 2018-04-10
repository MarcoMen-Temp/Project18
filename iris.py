# Marco Men - Project2018
# This file will read,retrieve and manipulate data from 'iris.csv'




import pandas as pd
import numpy as np


df = pd.read_csv('iris.csv', header=None) # StackOverflow: 'How to add header row to pandas DataFrame and PythonHow.com-'Loading CSV data in Python with pandas'
df.columns = ['Sep_L', 'Sep_W', 'Pet_L', 'Pet_W', 'Species']

print(df.head())


print (df.columns)
#Assigning variables to header row(Index),to facilitate statistical calculations of the 4 numerical rows
SepLength = df ['Sep_L' ]
SepWidth = df ['Sep_W']


print(SepLength.describe()) # Statistical calculations for 1st column -Pg.73
print(SepWidth.describe())

