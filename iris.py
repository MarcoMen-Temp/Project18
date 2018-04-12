# Marco Men - Project2018
# This file will read,retrieve and manipulate data from 'iris.csv'




import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('iris.csv', header=None) # StackOverflow: 'How to add header row to pandas DataFrame and PythonHow.com-'Loading CSV data in Python with pandas'
df.columns = ['Sep_L', 'Sep_W', 'Pet_L', 'Pet_W', 'Species']
print(df.head()) # Prints the first 5 rows; For the last 5 rows: print(df.tail())


print (df.columns) #Get column names on an Index Line(in Terminal)
print(df.describe())
#Assigning variables to header row(Index),to facilitate statistical calculations of the 4 numerical rows
SepLength = df ['Sep_L' ]
SepWidth = df ['Sep_W']
PetLength = df ['Pet_L']
PetWidth = df ['Pet_W']
Species = df ['Species']


# Histograms are the most common means of looking at a single variable(univariate)
print(Species.describe())
print(SepLength.describe()) # Statistical calculations(Summary of Statistics) for  columns using  'describe'method() -Pg.73

print(SepWidth.describe())
print(PetLength.describe())
print(PetWidth.describe())

#Histogram figures - www.kaggle.com -'Iris Dataset ML and Deep Learning from Scratch'
df.hist()
his = plt.gcf()
his.set_size_inches(12,6)
plt.show()





