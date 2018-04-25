import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('iris.csv', header = None) # StackOverflow: 'How to add header row to pandas DataFrame and PythonHow.com-'Loading CSV data in Python with pandas
df.columns = ['Sepal Lenght','Sepal Width','Petal Lenght','Petal Width','Species']



fig = sns.lmplot (x= 'Sepal Lenght', y= 'Sepal Width', data= df, hue= 'Species')
plt.show()


fig = sns.lmplot (x= 'Petal Lenght', y= 'Petal Width', data= df, hue= 'Species')
plt.show()

