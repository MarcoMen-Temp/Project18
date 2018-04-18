# Project18

> Iris Dataset retrieved from: " https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data " and saved as a csv file on Microsoft VS Code.

A Iris.py was opened that will read,retrive and manipulate data from csv(through import function and export of csv files)

I will be using pandas for python,numpy,anaconda python with VS Code,matplotlib and seaborn for this project

Created subsets of the all iris dataset:
  df = DataFrame for the whole 'iris dataset'
  df1 = DataFrame for 'Iris-setosa'(using the iloc[]method,appended the index range (0,50,1)-(start,end not incl.,stepvalue)
  df2 = DataFrame for 'Iris-versicolor'
  df3 = DataFrame for 'Iris-virginica'
  
  For each DataFrame ,make the basic stats calculations(.describe()method) in 'iris.py'
  Plot graphs will be in a separate file('plot.py)
  
  Graphs include:
    >Histograms and scatterplots for all 4 variables('Sepal Width', 'Sepal Lenght', 'Petal Width', 'Petal Lenght')
    >The differences based on species is caracterised by different colours
    
    
# This Readme File

This file's focus is on the Machine Learning aspect of this Project,and not so much on the Iris Dataset itself. The reason for this is,after conducting extensive enough research,one quickly reaches the conclusion that very little new information has been added to it,since it was first published in 1936,by an English biologist and statician named Ronald Fisher.
I will however,provide a brief explanation of what the Iris DataSet is, for what it has been useful, and how it fits in the subject of Data Science and/or Analytics
    
    
# About the Iris Data Set

  Iris dataset is a multivariate data set and since it was introduced by Ronald Fisher in 1936 in his paper('The use of multiple measurements in taxonomic problems has been used by other biologists,staticians and students(for statistical studies and projects)
  Its data is comprised by 150 rows and 5 columns('Sepal Width', Sepal Lenght', Petal Width', 'Petal Lenght' and 'Species')
  The 4 first columns are measurements in cms,and the 5th column('Species') describes the type of iris flower
  
 The data set is composed as folows: 
    >First 50 entries - Iris Setosa
    >From 51 -100 entries - Iris Versicolor
    >From 101 - 150 entries - Iris Virginica
    
Plenty of information available online and I provided a list of resources used by me whilst doing this project. I used the information to gather information,filter and reuse what I considered relevant. Also,to provide some benchmark for the results of the algorithms written by me in Python
    

# Data Science

  One of the cornerstones of Data Science is the subject of Machine Learning and this is the main context of this project. 
  What was once done manually is possible to automate the most tedious and time consuming tasks. For example,plotting      histograms,scatterplots and boxplots for all 4 different measurements of the different subsets of species and compiling it all back together would require months to perform,using traditional statistical studies technique. With Machine Learning,one can achieve this in a matter of weeks and with a lot less effort.
  There are however,tricks,skills and techiniques to know. For a Data Scientist,the data retrieved from a source might be too raw(or unsupervised),so the number of information extrapolated by that data will be limited,using Machine Learning. To enhance results,data must be manipulated and (re) assembled in a more tidy(cleaned) manner. So that the machine can perform the correct calculations and yield the results required.
  A broad knowledge of statistics is required for any Data Analysis project
  
  # The Files and Algorithms
  
  The first file iris.csv(Comma Separated Values) was downloaded from UCI Machine Learning website. I then created another file in Python Anaconda(v.3.6) named 'iris.py'
  
  ## Iris.py
  
  This file opened and stored iris.csv as a dataframe(or short df),using pandas library. From there I used built-in commands(pandas) to calculate a summary of basic statistics calculations(min.,max.,std. dev.,frequency,quartiles).
  
  A this was my first time using pandas for Python,I tried different commands(add columns for header,print the first 5 rows of dataframes,append by index row numbers values to different subsets of the dataframe
  
  ## Plot.py
  
  This file uses Matplotlib and Seaborn to plot pairplot graphs in a matrix. Histograms and scatter plots for the different species of iris separated by different colours. We can see that Iris versicolor and virginica are very closely related,because their distributed very closely(almost overlapping). Here the use of contrasting colour is most beneficial for anyone analysing data so closely related
  
  
  ## Boxplot.py
  
  This file shows the boxplot for the diferent variables(measurements). And we can visualise the calculated minimum, maximum,mean values from iris.py of both Sepal and Petal width and lenght(4 boxplots for each)
  
  
  
  ## Resources and References Used :
  
  https://archive.ics.uci.edu - 'UCI Machine Learning Reposityory'
  https://en.m.wikipedia.org - 'Iris flower data set'
  www.datacarpentry.org - 'Python for ecologists'
  https://machinelearningmastery.com - 'Your First Machine Learning Projectin Python Step-By-Step'
  blog.bharatbhole.com - ' Creating boxplotswith Matplotlib'
  https://pandas.pydata.org
  https://matplotlib.org
  www.kaggle.com - 'Iris Dataset ML and Deep Learning from Scratch'
  https://medium.com - 'Basic Analysis of Iris Data set using Python'
  https://neuraldesigner.com - 'Iris flowers classification'
'Pandas For Everyone - Python Data Analysis' -Daniel Y. Chen(Addison -Wesley) -2018
