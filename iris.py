# Marco Men - Project2018
# This file will read,retrieve and manipulate data from 'iris.csv'




import pandas as pd
from pandas import read_csv
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('iris.csv', header = None) # StackOverflow: 'How to add header row to pandas DataFrame and PythonHow.com-'Loading CSV data in Python with pandas'
df.columns = ['Sepal Lenght','Sepal Width','Petal Lenght','Petal Width','Species']

df.to_csv('iris_df.csv',index = False)


df1 = pd.read_csv('iris_df.csv')

print(df1.head())

 # Prints the first 5 rows; For the last 5 rows: print(df.tail())


print (df1.columns) #Get column names on an Index Line(in Terminal)
print(df1.describe())
#Assigning variables to header row(Index),to facilitate statistical calculations of the 4 numerical rows
SepLength = df1 ['Sepal Lenght' ]
SepWidth = df1 ['Sepal Width']
PetLength = df1 ['Petal Lenght']
PetWidth = df1 ['Petal Width']
Species = df1 ['Species']
df1.groupby(['Species']).size()


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





