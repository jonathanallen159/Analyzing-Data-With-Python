# MODULE 1
# this programme is the accompanying coursework to module 1 of the analyzing data with python IBM coursework

''' LEARNING OBJECTIVES:
 - analyze python data using a dataset
 - identify three python libraries and describe their uses
 - read data using python's Pandas package
 - demonstrate how to import data and export in python
'''

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
