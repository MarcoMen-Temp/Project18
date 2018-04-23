# Marco Men - Project2018
# With this file, plots will be crated using data
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

iris = sns.load_dataset('iris')

print(iris)

ax = sns.boxplot(data = iris, orient= 'v', palette='Set2')  #https://seaborn.pydata.org- 'Seaborn.boxplot
plt.show()