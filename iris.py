# Marco Men - Project2018
# This file will read,retrieve and manipulate data from 'iris.csv'




import pandas as pd
from pandas import read_csv
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('iris.csv', header = None) # StackOverflow: 'How to add header row to pandas DataFrame and PythonHow.com-'Loading CSV data in Python with pandas'

df.columns = ['Sepal Lenght','Sepal Width','Petal Lenght','Petal Width','Species']



 # Prints the first 5 rows; For the last 5 rows: print(df.tail())


print (df.columns) #Get column names on an Index Line(in Terminal)
print(df.describe())
#Assigning variables to header row(Index),to facilitate statistical calculations of the 4 numerical rows
SepLength = df ['Sepal Lenght' ]
SepWidth = df ['Sepal Width']
PetLength = df ['Petal Lenght']
PetWidth = df ['Petal Width']
Species = df ['Species']
print(df.groupby('Species').size())

#Create subsets based on different types of 'Iris'
df1 = df.iloc[0:50:1]
df2 = df.iloc[50:100:1]
df3 = df.iloc[100:150:1]


print(df1)
print (df2)
print(df3)


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





