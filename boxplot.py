# Marco Men - Project2018
# With this file, plots will be crated using data
import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd


df = pd.read_csv('iris.csv', header = None)

df1 = df.iloc[0:50:1]
df2 = df.iloc[50:100:1]
df3 = df.iloc[100:150:1]

print(df1)
print(df1.describe())

print(df2)
print(df2.describe())

print(df3)
print(df3.describe())

box, ax = plt.subplots(1,1,1 )
ax = sns.boxplot(x= 'Species', y= 'Data', data= df)
ax.set_title ('Boxplot')
ax.set_xlabel('Species')
ax.set_ylabel('Data')
plt.show()