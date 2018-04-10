# Marco Men - Project2018
# This file will read,retrieve and manipulate data from 'iris.csv'


import pandas as pd

df = pd.read_csv('iris.csv', sep= ',')

print(df.head())

print (df.shape)

print (df.columns)