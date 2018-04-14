"""Marco Men - Exercise 5 (Format)
Adapted from StackOverFlow: 'Formatting Output of CSV file in Python' """ 
import csv

def concat(*args, sep= "|"):
      return sep.join(args)


print(concat("SepalLength","SepalWidth","PetalLength","PetalWidth","Species"))

with open("iris.csv") as f:
      reader = csv.reader(f)
      for row in reader:
            print('{:>10} | {:>8} | {:>9} | {:>8} | {:>9} ' .format(*row))

df.to_csv('iris_df.csv' ,sep='|')


df1 = pd.read_csv('iris_df.csv')