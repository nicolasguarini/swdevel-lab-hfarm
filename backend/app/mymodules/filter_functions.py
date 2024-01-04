import pandas as pd

def filter_dataframe(df, column, value):
    return df[df[column] == value]

def filter_contains(df, column, value):
    if column == 'year':
        return df[df["year"] == str(value)]  
    else:
        return df[df[column].str.contains(value, case=False, na=False)]

def filter_range(df, column, min_value, max_value):
    if column == 'year':
        df[column] =  pd.to_numeric(df[column], errors='coerce').astype('Int64')
    return df[(df[column] >= min_value) & (df[column] <= max_value)]
