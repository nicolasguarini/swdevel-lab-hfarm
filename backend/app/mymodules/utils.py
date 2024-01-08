import numpy as np
import pandas as pd
from .filter_functions import filter_contains, filter_range


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
        - df_wines (pd.DataFrame): DataFrame containing
        wine information.
        - limit (int): Number of wines to return (default
        is 10).

    Returns:
        - pd.DataFrame: Most recently reviewed wines sorted
        by year in descending order.
    """
    df_wines = df_wines[df_wines['year'] != 'N.V.']
    return df_wines.sort_values(by="year", ascending=False).head(limit)


def wines_by_least_recent_year(df_wines, limit=10):
    """
    Get the least recently reviewed wines.

    Parameters:
        - df_wines (pd.DataFrame): DataFrame containing
        wine information.
        - limit (int): Number of wines to return
        (default is 10).

    Returns:
        - pd.DataFrame: Least recently reviewed wines sorted
        by year in ascending order.
    """
    df_wines = df_wines[df_wines['year'] != 'N.V.']
    return df_wines.sort_values(by="year", ascending=True).head(limit)


def countries_df(df_wines):
    """
    Extract unique countries from the 'country' column.

    Parameters:
        - df_wines (pd.DataFrame): DataFrame containing wine information.

    Returns:
        - list: List of unique countries.
    """
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
    types = df_wines['type'].astype(str).unique()
    return types.tolist()


def filter_wines(df_wines, filters):
    """
    Filter wines based on specified criteria.

    Parameters:
        - df_wines (pd.DataFrame): DataFrame containing wine information.
        - filters (dict): Dictionary of filters to apply to the DataFrame.

    Returns:
        - pd.DataFrame: Filtered DataFrame containing wines
        that match the specified criteria.
    """
    filtered_wines = df_wines.copy()
    for column, value in filters.items():
        if value and column in df_wines.columns:
            if (
                column == 'year' or
                column == 'price' or
                column == 'numberofratings' or
                column == 'rating' and None not in value
            ):
                filtered_wines = filter_range(filtered_wines, column, *value)
            else:
                filtered_wines = filter_contains(filtered_wines, column, value)

    return filtered_wines
