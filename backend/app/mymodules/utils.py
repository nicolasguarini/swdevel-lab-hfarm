from .filter_functions import filter_contains, filter_dataframe, filter_range

def top_wines_by_rating(df_wines, limit=10):
    return df_wines.sort_values(by="rating", ascending=False).head(limit)

def wines_by_recent_year(df_wines, limit=10):
    df_wines = df_wines[df_wines['year'] != 'N.V.']
    return df_wines.sort_values(by="year", ascending=False).head(limit)

def wines_by_least_recent_year(df_wines, limit=10):
    df_wines = df_wines[df_wines['year'] != 'N.V.']
    return df_wines.sort_values(by="year", ascending=True).head(limit)

def filter_wines(df_wines, filters):
    filtered_wines = df_wines.copy()
    
    for column, value in filters.items():
        if value is not None and column in df_wines.columns:
            if isinstance(value, tuple):
                filtered_wines = filter_range(filtered_wines, column, *value)
            elif column == 'name':
                filtered_wines = filter_contains(filtered_wines, column, value)
            elif column == 'year':
                filtered_wines = filter_range(filtered_wines, column, *value)
            else:
                filtered_wines = filter_dataframe(filtered_wines, column, value)

    return filtered_wines