# Marco Men - Project2018
# This file will read,retrieve and manipulate data from 'iris.csv'


import pandas as pd

df = pd.read_csv('iris.csv', sep= ',' , names = ['SepalWidth(cm)', 'SepalLenght(cm)', 'PetalWidth(cm)', 'PetalLenght(cm)', 'Species']) #Stack OverFlow:'How to add header row to pandas DataFrame

print(df.head())

print (df.shape)

print (df.columns)