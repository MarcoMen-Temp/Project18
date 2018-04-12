# Marco Men - Project2018
# With this file, plots will be crated using data
import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')

boxplot = plt.figure( )
axes1 = boxplot.add_subplot (2,2,1)
axes1.boxplot([iris[iris['Species'] == 'Iris-Setosa'] ['Value'],
iris[iris['Species'] == 'Iris-versicolor'] ['Value'], 
iris[iris['Species'] == 'Iris-virginica'] ['Value'],
labels= ['Iris-Setosa','Iris-versicolor', 'Iris-virginica'])
axes1.set_xlabel ('Species')
axes1.set_ylabel ('Values')
axes1.set_title('Boxplot of Iris DataSet')
boxplot.show()


axes2 = fig.add_subplot (2,2,2)
scatter, ax =plt.subplots( )
ax = sns.regplot(x= 'Species','Values', data = iris)
ax.set_title('Scatterplot of Species and Values')
ax.sett
axes3 = fig.add_subplot (2,2,3)
axes4 = fig.add_subplot (2,2,4)
 
