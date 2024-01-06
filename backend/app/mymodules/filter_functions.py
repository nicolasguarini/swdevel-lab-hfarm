import pandas as pd

def filter_dataframe(df, column, value):
    """
    Filter a DataFrame based on a specific value in a specified column.

    Parameters:
        df (pd.DataFrame): The DataFrame to be filtered.
        column (str): The name of the column in the DataFrame for filtering.
        value: The specific value to filter for in the specified column.

    Returns:
        pd.DataFrame: Filtered DataFrame containing only rows where the specified column has the specified value.
    """
    return df[df[column] == value]

def filter_contains(df, column, value):
    """
    Filter a DataFrame based on substring matching in a specified column.

    Parameters:
        df (pd.DataFrame): The DataFrame to be filtered.
        column (str): The name of the column in the DataFrame for filtering.
        value: The substring to check for in the specified column.

    Returns:
        pd.DataFrame: Filtered DataFrame containing only rows that match the substring condition.
    """
    if column == 'year':
        return df[df["year"] == str(value)]  
    else:
        return df[df[column].str.contains(value, case=False, na=False)]

def filter_range(df, column, min_value, max_value):
    """
    Filter a DataFrame based on a numeric range or exact match for the 'year' column.

    Parameters:
        df (pd.DataFrame): The DataFrame to be filtered.
        column (str): The name of the column in the DataFrame for filtering.
        min_value: The minimum value for the range or exact match.
        max_value: The maximum value for the range.

    Returns:
        pd.DataFrame: Filtered DataFrame containing only rows where the specified column's values fall within the specified range.
    """ 
    return df[(df[column] >= min_value) & (df[column] <= max_value)]
