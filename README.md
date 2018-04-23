# Project18 - For Programming & Scripting

   ### Researched, written and compiled by: 
  > Marco Men
  

## Research
  
  This project was written and compiled using python's library package named 'panda'( an abbreviation for 'panel data'). The resources and references used are provided below:
  
 * https://archive.ics.uci.edu - 'UCI Machine Learning Reposityory'
 * https://en.m.wikipedia.org - 'Iris flower data set'
 * https://statcan.gc.ca - 'Constructing box and whisker plots'
 * www.datacarpentry.org - 'Python for ecologists'
 * https://machinelearningmastery.com - 'Your First Machine Learning Project in Python Step-By-Step'
 * blog.bharatbhole.com - ' Creating boxplotswith Matplotlib'
 * https://pandas.pydata.org
 * https://matplotlib.org
 * www.kaggle.com - 'Iris Dataset ML and Deep Learning from Scratch'
 * https://medium.com - 'Basic Analysis of Iris Data set using Python'
 * https://neuraldesigner.com - 'Iris flowers classification'
 * 'Pandas For Everyone - Python Data Analysis' -Daniel Y. Chen(Addison -Wesley) -2018

## Before Start of the Project

Upon completion of literature review consisting of matplotlib documentation review, I have come to a conclusion that 'numpy' could be used as a stand-alone, in conjunction with 'pandas', or just 'pandas' as both packages are compatible and complimentary. There are multiple similar and/or overlapping commands between the two packages. I have thoroughly researched Pandas package and determined that it will be most suitable to complete the project using this package.

## Development

Python's library packages used for this project were Panda, Matplotlib and Seaborn. I will briefly clarify them and provide evidence of the knowledge and skills acquired below:

 ## Pandas

This is a relatively new Python package project name of which is derived from the term "panel data", an econometrics term for data sets that include observations over multiple time periods for the same individuals.
The first realease was February 2013 and since then the package has been updated and improved into its current status: "pandas: powerful Python data analysis toolkit". The latest version release was Dec 30, 2017 Version: 0.22.0
Furthermore, this package has received excellent reviews on its website: "https://pandas.pydata.org/pandas-docs/stable/" (definition below), which lead me to a decision to experiment with this relatively new tool for data analysis. Based on its features, I concluded that this package was most suitable for this project.

According to "https://pandas.pydata.org/pandas-docs/stable/ "pandas is a Python package providing fast, flexible, and expressive data structures designed to make working with “relational” or “labeled” data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, real world data analysis in Python. Additionally, it has the broader goal of becoming the most powerful and flexible open source data analysis / manipulation tool available in any language. It is already well on its way toward this goal."

## Matplotlib

Another Python package used in this project for plotting is matplotlib. 
According to the "https://matplotlib.org/ "Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. Matplotlib can be used in Python scripts, the Python and IPython shells, the Jupyter notebook, web application servers, and four graphical user interface toolkits.
Matplotlib tries to make easy things easy and hard things possible. You can generate plots, histograms, power spectra, bar charts, errorcharts, scatterplots, etc., with just a few lines of code.
For simple plotting the pyplot module provides a MATLAB-like interface, particularly when combined with IPython. For the power user, you have full control of line styles, font properties, axes properties, etc, via an object oriented interface or via a set of functions familiar to MATLAB users."

## Seaborn

For this project 'Seaborn' was used to enhance graphic visualisation of graphs plotted by matplotlib. To make them  more user friendly, facilitating the immediate distinction between different variables based on 'Species' of irises, several different colours were applied. Seaborn also provides a legend to the the graphs to help the users in identification of different variables.

According to https://seaborn.pydata.org/ "Seaborn is a Python visualization library based on matplotlib. It provides a high-level interface for drawing attractive statistical graphics."

# Consistency

 > Initial Plan

My initial plan involved everything presented in this project with a SVM and KNN (by importing modules from sklearn package),as described in: "https://www.kaggle.com/kamrankausar/iris-dataset-ml-and-deep-learning-from-scratch" and "https://machinelearningmastery.com/machine-learning-in-python-step-by-step/"

 > Final Project
  
I decided  against including the SVM and KNN, as all of the objectives were reached by calculating the summary of desciptive statistics and the graphs plotted were sufficient to demonstrate to the  users the results of the analysed data.  

Overall, the main objectives and learning outcomes were achived by me,and they include:
  - Basic understanding of technical knowledge,skills and tools available for data analysis
  - Understanding of requirements for retrieving and storing data files(i.e.CSV files) into a Python environment in order to best manipulate and assemble data required.  **(Please see note below)**
  - Understanding of basic panda's commands to save CSV files into dataframes(df),append column rows(header) without affecting the indexation of rows(df.column),list the five first rows of dataframe(with df.head),list the five last rows(df.tail),obtain information on the type of Panda objects(Series or Dataframe used(df.info()) and size of file
  - Understanding how to list a summary of descriptive statistical calculations(df.describe) of the dataframe saved,or its individual calculations(i.e df.mean(),or df.std(),df.max(),df.min(),df.median(),etc.
  - Understanding on how to select specific rows, create subsets from a dataframe(using iloc-index number or loc-index label).
  - Learn commands to load a Dataframe file for plotting using Matplotlib and Seaborn
  - Basic understanding of plotting with Panda objects.
  
  ** Note- The iris dataset provided me no issues regarding missing data,NaNs or index issues. Although, I prepared myself to tackle such events,were they to arise - The process of 'tidying data' of Dataframe  and making it ready for analysis is also a learning outcome attained by me
  
  
  ## Documentation
  
  
  > Iris Dataset retrieved from: " https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data " and saved as a csv file on Microsoft VS Code.

A Iris.py was opened that will read,retrive and manipulate data from csv(through import function and export of csv files)

I used anaconda python with VS Code, pandas,matplotlib and seaborn for this project

Created subsets of the all iris dataset:
 - df = DataFrame for the whole 'iris dataset'
 - df1 = DataFrame for 'Iris-setosa'(using the iloc[]method,appended the index range (0,50,1)-(start,end not incl.,stepvalue)
 - df2 = DataFrame for 'Iris-versicolor'
 - df3 = DataFrame for 'Iris-virginica'
  These block of code was implemented while discovering and experimenting code with Pandas. For each DataFrame ,make the basic stats calculations(.describe()method) in 'iris.py'
    
    
# About the Iris Data Set

  Iris dataset is a multivariate data set and since it was introduced by Ronald Fisher in 1936 in his paper('The use of multiple measurements in taxonomic problems has been used by other biologists,staticians and students(for statistical studies and projects)
  Its data is comprised by 150 rows and 5 columns('Sepal Width', Sepal Lenght', Petal Width', 'Petal Lenght' and 'Species')
  The 4 first columns are measurements in cms,and the 5th column('Species') describes the type of iris flower
  
 The data set is composed as folows: 
    * First 50 entries - Iris Setosa
    * From 51 -100 entries - Iris Versicolor
    * From 101 - 150 entries - Iris Virginica
    
Plenty of information available online and I provided a list of resources used by me whilst doing this project. I used the resources and references listed above to gather information,filter and use what I considered relevant. Also,to provide some benchmark for the results of the algorithms written by me in Python,with regards to outputs.

    

# Data Science

  One of the cornerstones of Data Science is the subject of Machine Learning and this is the main context of this project. 
  What was once done manually is possible to automate the most tedious and time consuming tasks. For example,plotting      histograms,scatterplots and boxplots for all 4 different measurements of the different subsets of species and compiling it all back together would require months to perform,using traditional statistical studies technique. With Machine Learning,one can achieve this in a matter of weeks and with a lot less effort.
  There are however,tricks,skills and techiniques to know. For a Data Scientist,the data retrieved from a source might be too raw(or unsupervised),so the number of information extrapolated by that data will be limited,using Machine Learning. To enhance results,data must be manipulated and (re) assembled in a more tidy(cleaned) manner. So that the machine can perform the correct calculations and yield the results required.
  A broad knowledge of statistics is required for any Data Analysis project
  
  # The Files and Algorithms
  
  All my files are in this repository in a folder named 'Project18'.
  The first file iris.csv(Comma Separated Values) was downloaded from UCI Machine Learning website. I then stored the values in another file in the format of a Dataframe. I named this file 'iris.py'. 
  
  ## Iris.py
  
  This file opened and stored iris.csv as a dataframe(or short df),using pandas library. From there I used built-in commands(df.describe()) to calculate a summary of basic statistics calculations(min.,max.,std. dev.,frequency,quartiles).
  
  As this was my first time using pandas for Python,I tried different commands(add columns for header,print the first 5 rows of dataframes,append by index row numbers values to different subsets of the dataframe,list information about the Dataframe.
  
  ## Plot.py
  
  This file uses Matplotlib and Seaborn to plot pairplot graphs in a matrix. Histograms and scatter plots for the different species of iris separated by different colours. We can see that Iris versicolor and virginica are very closely related,because their distributed very closely(almost overlapping). Here the use of contrasting colours is most beneficial for anyone analysing data, from so closely related variables. As this provides a clearer distinction of the two.
  Each row in the matrix represents each of the 4 variables ('Sepal Width', 'Sepal Lenght', 'Petal Width', 'Petal Lenght')
  The histograms provide a visualisation of frequency and distribution of data
  
    
  
  ## Boxplot.py
  
  This file shows the boxplots for the different species of irises.
  Boxplots provide a clear visualisation of median(Q2),minimum(lower observation on whisker and maximum(highest observation) values,lower quartile(Q1),and upper quartile(Q3)  from iris.py of all 4 columns('Sepal Width', 'Sepal Lenght', 'Petal Width' and 'Petal Lenght')


