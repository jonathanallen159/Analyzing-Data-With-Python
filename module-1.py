# MODULE 1
# this programme is the accompanying coursework to module 1 of the analyzing data with python IBM coursework

''' LEARNING OBJECTIVES:
 - analyze python data using a dataset
 - identify three python libraries and describe their uses
 - read data using python's Pandas package
 - demonstrate how to import data and export in python
'''

### IMPORT THE DATA ###
# import the pandas package
import pandas as pd
import numpy as np

# use the pandas package to import a csv dataset
# first define a variable with the filepath
filepath = r'Code/Analyzing-Data-With-Python/imports-85.data'

# use the read csv function from the pandas package and store it as a dataframe
df = pd.read_csv(filepath, header = None) # NOTE this dataset has no header so we must specify this as default is to assume the first row is a header

# check the data has been read correctly by printing the first few rows of the dataframe and last few rows.
print(df.head(5)) # this command prints the first 5 rows of the dataframe
print(df.tail(5)) # this command prints the last 5 rows of the dataframe


### ANALYZE THE DATA ###
# pandas package has built-in methods that can be used to understand the datatype or distribution of data in a dataset
# it is helpful to check which datatypes pandas has assigned to the data as it may be better to change the encoding
datatypes = df.dtypes # this command returns the datatypes of each column
print(datatypes)

# we can then get a brief statistical analysis of all the data using a built-in pandas function
stat_description = df.describe(include = 'all') # this command gives us a brief description of the distribution of the dataset
print(stat_description)

# another useful function provides a concise summary of the dataframe
data_summary = df.info() # this functions shows the top 30 rows and bottom 30 rows of the data dataframe
print(data_summary)
