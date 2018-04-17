# Marco Men - Project2018
# With this file, plots will be crated using data
import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')

hist , ax = plt.subplots( )

ax = sns.displot (Iris ['Iris'])
ax.set_title('Histogram with Density Plot')
plt.show