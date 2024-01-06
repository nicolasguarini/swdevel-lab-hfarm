import numpy as np
import pandas as pd
from .filter_functions import filter_contains, filter_dataframe, filter_range

def top_wines_by_rating(df_wines, limit=10):
    """
    Get the top wines based on rating.

    Parameters:
        - df_wines (pd.DataFrame): DataFrame containing wine information.
        - limit (int): Number of top wines to return (default is 10).

    Returns:
        - pd.DataFrame: Top wines sorted by rating in descending order.
    """
    return df_wines.sort_values(by="rating", ascending=False).head(limit)

def wines_by_recent_year(df_wines, limit=10):
    """
    Get the most recently reviewed wines.

    Parameters:
        - df_wines (pd.DataFrame): DataFrame containing wine information.
        - limit (int): Number of wines to return (default is 10).

    Returns:
        - pd.DataFrame: Most recently reviewed wines sorted by year in descending order.
    """
    df_wines = df_wines[df_wines['year'] != 'N.V.']
    return df_wines.sort_values(by="year", ascending=False).head(limit)

def wines_by_least_recent_year(df_wines, limit=10):
    """
    Get the least recently reviewed wines.

    Parameters:
        - df_wines (pd.DataFrame): DataFrame containing wine information.
        - limit (int): Number of wines to return (default is 10).

    Returns:
        - pd.DataFrame: Least recently reviewed wines sorted by year in ascending order.
    """
    df_wines = df_wines[df_wines['year'] != 'N.V.']
    return df_wines.sort_values(by="year", ascending=True).head(limit)

def years_in_wines(df_wines):
    """
    Extract the minimum and maximum years from the 'year' column.

    Parameters:
        - df_wines (pd.DataFrame): DataFrame containing wine information.

    Returns:
        - dict: Dictionary with the minimum and maximum years.
    """
    filtered_years = df_wines[df_wines['year'] != 'N.V.']['year'].astype(float)
    min_year = np.min(filtered_years)
    max_year = np.max(filtered_years)
    
    return {"min_year": min_year, "max_year": max_year}

def max_number_of_ratings(df_wines):
    """
    Get the maximum number of ratings in the DataFrame.

    Parameters:
        - df_wines (pd.DataFrame): DataFrame containing wine information.

    Returns:
        - dict: Dictionary with the maximum number of ratings.
    """
    # Find the maximum number of ratings in the DataFrame
    max_ratings = int(df_wines['numberofratings'].max())
    
    # Return a dictionary with the maximum number of ratings
    return {"max_number_of_ratings": max_ratings}

def countries_df(df_wines):
    """
    Extract unique countries from the 'country' column.

    Parameters:
        - df_wines (pd.DataFrame): DataFrame containing wine information.

    Returns:
        - list: List of unique countries.
    """
    # Get unique countries from the 'country' column and convert to a Python list
    countries = df_wines['country'].astype(str).unique()
    return countries.tolist()

def types_df(df_wines):
    """
    Extract unique wine types from the 'type' column.

    Parameters:
        - df_wines (pd.DataFrame): DataFrame containing wine information.

    Returns:
        - list: List of unique wine types.
    """
    # Get unique wine types from the 'type' column and convert to a Python list
    types = df_wines['type'].astype(str).unique()
    return types.tolist()

def filter_wines(df_wines, filters):
    """
    Filter wines based on specified criteria.

    Parameters:
        - df_wines (pd.DataFrame): DataFrame containing wine information.
        - filters (dict): Dictionary of filters to apply to the DataFrame.

    Returns:
        - pd.DataFrame: Filtered DataFrame containing wines that match the specified criteria.
    """
    filtered_wines = df_wines.copy()
    
    for column, value in filters.items():
        if value is not None and column in df_wines.columns:
            if column == 'year' or column == 'price' or column == 'numberofratings' and None not in value:
                filtered_wines = filter_range(filtered_wines, column, *value)
            elif column == 'name' or column == 'type' or column == 'winery' or column == 'region':
                filtered_wines = filter_contains(filtered_wines, column, value)
            elif column == 'rating':
                filtered_wines = filter_by_rating(filtered_wines, value)                
    
    # Return the filtered DataFrame
    return filtered_wines

def filter_by_rating(df_wines, target_rating):
    """
    Filter the DataFrame based on the desired rating.

    Parameters:
        - df_wines (pd.DataFrame): DataFrame containing wine information.
        - target_rating (float): Desired rating from 0 to 5.

    Returns:
        - pd.DataFrame: DataFrame with only instances that have the desired rating.
    """
    # Check if the target rating is within the valid range [0, 5]
    if 0 <= target_rating <= 5:
        # Filter the DataFrame to include only instances with the desired rating
        filtered_df = df_wines[(target_rating <= df_wines['rating']) & (df_wines['rating'] < target_rating + 1)]
        return filtered_df
    else:
        # Raise a ValueError if the target rating is outside the valid range
        raise ValueError("The rating must be between 0 and 5.")
