"""
For keto_learn, I want to start with a common data object, and use various functions to manipulate, analyze and train on it

This module will create the data object class and pass it onto other modules.

"""

import numpy as np
import pandas as pd
from typing import TextIO
from df_inspection import *


def read_csv_file(data_file: TextIO, object_type: str):
    '''
    Pull in a csv file and convert to needed object types:

            - Numpy Array
            - Pandas DataFrame
    '''
    
    if object_type == 'pandas_df':
    
        print('converting to pandas dataframe')
        output = pd.read_csv(data_file)
    
    elif object_type == 'numpy_array':
    
        print('converting to numpy array')
        df = pd.read_csv(data_file)
        output = df.to_numpy()
        
    return output




class Datlet:
  
  def __init__(self, file_name, file_type, file_header, nickname):
    self.file_name = file_name
    self.file_type = file_type
    self.file_header = file_header

    self.nickname = nickname # when calling the object, the __str__ method will return this

    self.pdataframe = read_csv_file(self.file_name, 'pandas_df')
    self.nparray = read_csv_file(self.file_name, 'numpy_array')

    self.headers = self.pdataframe.columns
    self.dtypes_dict = identify_dtypes(self.pdataframe)
    self.pretty_print_dtypes = 

    self.shape = self.nparray.shape

  def __str__(self):

    return f"{self.nickname}(Datlet)"

  def scatterplots():
    pass

  def inspect():
     pass

