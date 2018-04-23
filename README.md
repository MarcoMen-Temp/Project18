# Project18 - For Programming & Scripting

   ### Researched,written and compiled by: 
  > Marco Men
  

## Research
  
  This project was written and compiled using python's library package named 'panda'( an abbreviation for 'panel data'). The resources and references used are provided below:
  
 > https://archive.ics.uci.edu - 'UCI Machine Learning Reposityory'
 > https://en.m.wikipedia.org - 'Iris flower data set'
 > www.datacarpentry.org - 'Python for ecologists'
 > https://machinelearningmastery.com - 'Your First Machine Learning Project in Python Step-By-Step'
 > blog.bharatbhole.com - ' Creating boxplotswith Matplotlib'
 > https://pandas.pydata.org
 > https://matplotlib.org
 > www.kaggle.com - 'Iris Dataset ML and Deep Learning from Scratch'
 > https://medium.com - 'Basic Analysis of Iris Data set using Python'
 > https://neuraldesigner.com - 'Iris flowers classification'
 > 'Pandas For Everyone - Python Data Analysis' -Daniel Y. Chen(Addison -Wesley) -2018

## Before Start of Project

During my pre-research for this project,the conclusions reached by me were that most of the 'iris dataset' studies carried out using Python programming language was done so,by using numpy library package( as it would be the norm). After,reading matplotlib literature and documentation a realisation that 'numpy' could be used as a stand-alone,in conjunction with 'pandas',or just 'pandas'. As both packages are compatible and complimentary,there is a lot of similar and/or overlapping commands between the two packages.
Knowing that a lot of similar code was written and readily available on line,my fear would be that I would comfartably would seek answers without any learning and development on the matter
Even though, I had support in the book 'Pandas for Everyone','https://pandas.pydata.org', re-adjustment of code was required to suit to this particular dataset,as other datasets were used as examples


## Development

The Python's library packages used for this project were Panda,Matplotlib and Seaborn. I will briefly clarify them and provide evidence of the knowledge and skills acquired.


 ## Pandas

This is a relatively new Python package project that  The name is derived from the term "panel data", an econometrics term for data sets that include observations over multiple time periods for the same individuals.
The first realease was February 2013,and since then the package has been updated and improved into its current status: "
pandas: powerful Python data analysis toolkit". The latest version release was Dec 30, 2017 Version: 0.22.0
Another reason that made me choose this package was the rave reviews in its website: "https://pandas.pydata.org/pandas-docs/stable/"(definition below), which lead me to try and experiment with this relatively new tool for data analysis. Based on its features, I concluded that this package was more than suited for this project.

According with "https://pandas.pydata.org/pandas-docs/stable/"

pandas is a Python package providing fast, flexible, and expressive data structures designed to make working with “relational” or “labeled” data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, real world data analysis in Python. Additionally, it has the broader goal of becoming the most powerful and flexible open source data analysis / manipulation tool available in any language. It is already well on its way toward this goal.

## Matplotlib

This is another Python package used in this project for plotting. 
According with the "https://matplotlib.org/"

Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. Matplotlib can be used in Python scripts, the Python and IPython shells, the Jupyter notebook, web application servers, and four graphical user interface toolkits.
Matplotlib tries to make easy things easy and hard things possible. You can generate plots, histograms, power spectra, bar charts, errorcharts, scatterplots, etc., with just a few lines of code. For examples, see the sample plots and thumbnail gallery.

For simple plotting the pyplot module provides a MATLAB-like interface, particularly when combined with IPython. For the power user, you have full control of line styles, font properties, axes properties, etc, via an object oriented interface or via a set of functions familiar to MATLAB users.

## Seaborn

For this project 'Seaborn' was used to enhance graphic visualition of graphs plotted by matplotlib( different colors used to distinguish between different variables within the same graphs),to make them  more user friendly,facilitating the immediate distinction between different variables(based on 'Species' of irises). Also provides,legend to the the graphs help the users identification of different variables

According to https://seaborn.pydata.org/

Seaborn is a Python visualization library based on matplotlib. It provides a high-level interface for drawing attractive statistical graphics.


# Consistency

 > Initial Plan

My initial plan involved everything presented on this project with a SVM and KNN (by importing modules from sklearn package),as described in: "https://www.kaggle.com/kamrankausar/iris-dataset-ml-and-deep-learning-from-scratch" and "https://machinelearningmastery.com/machine-learning-in-python-step-by-step/"


  > Final Project
  
The reason for not include the the SVM and KNN,was that a conclusion was reached that the project with the desciptive statistics and the graphs plotted was sufficient to demonstrate the results required,the calculation of a summary of descriptive statistics and the plotting of garphs associated with those calculations,to facilitate users' understanding of final results of data retrieved,manipulated and assembled,by the data analyst
Overall, the main objectives and learning outcomes were achived by me,and they include:
  > Understanding of requirements for retrieving and storing data files(i.e.CSV files) into a Python environment in order to best manipulate and assemble data required.  **(Please see note below)**
  > Understanding of basic panda's commands to save CSV files into dataframes(df),append column rows(header) without affecting the indexation of rows(df.column),list the five first rows of dataframe(with df.head),list the five last rows(df.tail).
  > Understanding how to list a summary of descriptive statistical calculations(df.describe) of the dataframe saved,or its individual calculations(i.e df.mean(),or df.std(),df.max(),df.min(),df.median(),etc.
  > Differences between Series(thought as a Python list) and Dataframes(thought as a Series dictionary in Python terms) in Pandas
  > Basic understanding of the similarities between numpy and panda packages(between panda Series and numpy ndarray). Also,similar commands are used by both packages for the same results regarding statistics
  > Understanding on how to select specific rows, create subsets from a dataframe(using iloc-index number or loc-index label).  Example include, the creation of df1,df2,df3(variables) created and index values appended using the iloc command.
  > Understanding of similarities between loc and iloc of Dataframes and Numpy's ix command,which no longer works in latest version of Pandas(it works on Pandas' Series)
  > Learn commands to load a Dataframe file for plotting using Matplotlib and Seaborn
  > Basic understanding of plotting with Panda objects.
  
  ** Note- The iris dataset provided me no issues regarding missing data,NaNs or index issues. Although, I prepared myself to tackle such events,were they to arise - The process of 'tidying data' for analysis.
  
  
  ## Documentation
  
  
  > Iris Dataset retrieved from: " https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data " and saved as a csv file on Microsoft VS Code.

A Iris.py was opened that will read,retrive and manipulate data from csv(through import function and export of csv files)

I will be using pandas for python,anaconda python with VS Code,matplotlib and seaborn for this project

Created subsets of the all iris dataset:
  df = DataFrame for the whole 'iris dataset'
  df1 = DataFrame for 'Iris-setosa'(using the iloc[]method,appended the index range (0,50,1)-(start,end not incl.,stepvalue)
  df2 = DataFrame for 'Iris-versicolor'
  df3 = DataFrame for 'Iris-virginica'
  These block of code was implemented while discovering and experimenting code with Pandas. For each DataFrame ,make the basic stats calculations(.describe()method) in 'iris.py'
  
  Plot graphs will be in a separate files('plot.py' and 'boxplot.py')
  
  Graphs include:
    'plot.py'
    
      >Histograms and scatterplots for all 4 variables('Sepal Width', 'Sepal Lenght', 'Petal Width', 'Petal Lenght')
      >The differences based on species is caracterised by different colours.
      > The co-relationship between the different species can be clearly viewed in the scatterplots
      > The histograms provide a visualisation of frequency,mean and mode
    
   'boxplot.py'
   
    > Boxplots for all value columns( 'Sepal Width', 'Sepal Lenght', 'Petal Width', ' Petal Lenght')
    > Boxplots provide a clear visualisation of median(Q2),minimum(lower observation on whisker and maximum(highest observation) values,lower quartile(Q1),and upper quartile(Q3)
    
    
# This Readme File

This file's focus is on the Machine Learning aspect of this Project,and not so much on the Iris Dataset itself. The reason for this is,after conducting extensive enough research,one quickly reaches the conclusion that very little new information has been added to it,since it was first published in 1936,by an English biologist and statician named Ronald Fisher.
I will however,provide a brief explanation of what the Iris DataSet is, for what it has been useful, and how it fits in the subject of Data Science and/or Analytics. I will attach a section at the end of this file with headings: 'Research', 'Development', 'Consistency' and 'Documentation
    
    
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
  
  This file shows the boxplot for the diferent variables(measurements). And we can visualise the calculated minimum, maximum,median,and quartile values from iris.py of both Sepal and Petal width and lenght(4 boxplots for each)


