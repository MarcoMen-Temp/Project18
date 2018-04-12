# Marco Men - Project2018
# This file will read,retrieve and manipulate data from 'iris.csv'




import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('iris.csv', header=None) # StackOverflow: 'How to add header row to pandas DataFrame and PythonHow.com-'Loading CSV data in Python with pandas'
df.columns = ['Sep_L', 'Sep_W', 'Pet_L', 'Pet_W', 'Species']

print(df.head()) # Prints the first 5 rows


print (df.columns) #Get column names on an Index Line(in Terminal)
#Assigning variables to header row(Index),to facilitate statistical calculations of the 4 numerical rows
SepLength = df ['Sep_L' ]
SepWidth = df ['Sep_W']
PetLength = df ['Pet_L']
PetWidth = df ['Pet_W']

# Histograms are the most common means of looking at a single variable(univariate)
print(SepLength.describe()) # Statistical calculations(Summary of Statistics) for  columns using  'describe'method() -Pg.73

fig = plt.figure()
axes1 = fig.add_subplopt(1,1,1)# 2 graph rows(1- Histogram;2- Boxplot)
axes1.hist(SepLength[df ['Sep_L'], bins= 10)
axes1.set_title('Histogram of Sepal Lenght(cm)')
axes1.set_xlabel('Frequency')
axes1.set_ylabel('Bin')
fig.show ( )

#Boxplot next
boxplot = plt.figure( )
axes1 = boxplot.add_subplot(1,1,1)
axes1.boxplot([df['Species'] == 'Iris Setosa'] ['Lenght'], 
df['Species'] == 'Iris Versicolor'] ['Lenght'], 
df['Species'] == 'Iris Virginica'] ['Lenght'])

Iris Setosa,Iris Versicolor,Iris Virginica

print(SepWidth.describe())

fig = plt.figure()
axes1 = fig.add_subplopt(1,1,1)# 2 graph rows(1- Histogram;2- Boxplot)
axes1.hist(SepLength[df ['Sep_W'], bins= 10)
axes1.set_title('Histogram of Sepal Width(cm)')
axes1.set_xlabel('Frequency')
axes1.set_ylabel('Bin')
fig.show ( )

print(PetLength.describe())

fig = plt.figure()
axes1 = fig.add_subplopt(1,1,1)# 2 graph rows(1- Histogram;2- Boxplot)
axes1.hist(SepLength[df ['Pet_L'], bins= 10)
axes1.set_title('Histogram of Petal Lenght(cm)')
axes1.set_xlabel('Frequency')
axes1.set_ylabel('Bin')
fig.show ( )

print(PetWidth.describe())

fig = plt.figure()
axes1 = fig.add_subplopt(1,1,1)# 2 graph rows(1- Histogram;2- Boxplot)
axes1.hist(SepLength[df ['Pet_W'], bins= 10)
axes1.set_title('Histogram of Petal Width(cm)')
axes1.set_xlabel('Frequency')
axes1.set_ylabel('Bin')
fig.show ( )
