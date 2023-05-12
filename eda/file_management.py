"""
Pull in file and convert to needed object types:

- Numpy Array
- Pandas DataFrame

"""

import numpy as np
import pandas as pd
from typing import TextIO


def read_csv_file(file: TextIO, object_type: str):
    
    if object_type == 'pandas_df':
    
        print('converting to pandas dataframe')
        output = pd.read_csv(data_file)
    
    elif object_type == 'numpy_array':
    
        print('converting to numpy array')
        output = df.to_numpy()
        
    return output