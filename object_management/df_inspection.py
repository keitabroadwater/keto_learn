'''Functions to inpsect and modify dataframe.'''


def identify_dtypes(df):
    '''Input: dataframe
    
        Output: table of column names, dtype, and two example values
    '''


    dtypes_dict = {}

    sample_row1 = df.sample()
    sample_row2 = df.sample()


    for column in df.columns:
        print(column, df.dtypes[column])
        dtypes_dict[column] = {'dtype': df.dtypes[column], 'sample_value1' = sample_row1[column], \
                               'sample_value2' = sample_row2[column] }


    return dtypes_dict


def pretty_print_dtypes_dict(dtypes_dict):

    '''Input: dtypes dictionary generated above
    
        Output: pretty table done in matplotlib
    '''

    