# Marco Men - Project2018
# With this file, plots will be crated using data
import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')

fig = sns.pairplot (iris)
plt.show()






