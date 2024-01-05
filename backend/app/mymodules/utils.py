import numpy as np
from .filter_functions import filter_contains, filter_dataframe, filter_range

def top_wines_by_rating(df_wines, limit=10):
    """
    Get the top wines based on rating.

    Parameters:
        df_wines (pd.DataFrame): DataFrame containing wine information.
        limit (int): Number of top wines to return (default is 10).

    Returns:
        pd.DataFrame: Top wines sorted by rating in descending order.
    """
    return df_wines.sort_values(by="rating", ascending=False).head(limit)

def wines_by_recent_year(df_wines, limit=10):
    """
    Get the most recently reviewed wines.

    Parameters:
        df_wines (pd.DataFrame): DataFrame containing wine information.
        limit (int): Number of wines to return (default is 10).

    Returns:
        pd.DataFrame: Most recently reviewed wines sorted by year in descending order.
    """
    # Exclude wines with 'N.V.' (non-vintage) in the 'year' column
    df_wines = df_wines[df_wines['year'] != 'N.V.']
    return df_wines.sort_values(by="year", ascending=False).head(limit)

def wines_by_least_recent_year(df_wines, limit=10):
    """
    Get the least recently reviewed wines.

    Parameters:
        df_wines (pd.DataFrame): DataFrame containing wine information.
        limit (int): Number of wines to return (default is 10).

    Returns:
        pd.DataFrame: Least recently reviewed wines sorted by year in ascending order.
    """
    # Exclude wines with 'N.V.' (non-vintage) in the 'year' column
    df_wines = df_wines[df_wines['year'] != 'N.V.']
    return df_wines.sort_values(by="year", ascending=True).head(limit)

def years_in_wines(df_wines):
    # Assuming 'N.V.' is a string in the 'year' column that you want to exclude
    filtered_years = df_wines[df_wines['year'] != 'N.V.']['year'].astype(float)
    
    # Check if the result is a NumPy array
    if isinstance(filtered_years, np.ndarray):
        min_year = np.min(filtered_years)
        max_year = np.max(filtered_years)
    else:
        # If it's not a NumPy array, you can use Python built-in functions
        min_year = min(filtered_years)
        max_year = max(filtered_years)
    
    return {"min_year": min_year, "max_year": max_year}


def filter_wines(df_wines, filters):
    """
    Filter wines based on specified criteria.

    Parameters:
        df_wines (pd.DataFrame): DataFrame containing wine information.
        filters (dict): Dictionary of filters to apply to the DataFrame.

    Returns:
        pd.DataFrame: Filtered DataFrame containing wines that match the specified criteria.
    """
    # Create a copy of the original DataFrame for filtering
    filtered_wines = df_wines.copy()
    
    # Iterate through filters and apply them to the DataFrame
    for column, value in filters.items():
        if value is not None and column in df_wines.columns:
            if isinstance(value, tuple):
                # If the filter value is a tuple, apply range filtering
                filtered_wines = filter_range(filtered_wines, column, *value)
            elif column == 'name':
                # If the filter is on the 'name' column, perform substring matching
                filtered_wines = filter_contains(filtered_wines, column, value)
            elif column == 'year':
                # If the filter is on the 'year' column, apply range filtering
                filtered_wines = filter_range(filtered_wines, column, *value)
            else:
                # For other columns, apply exact match filtering
                filtered_wines = filter_dataframe(filtered_wines, column, value)

    return filtered_wines
