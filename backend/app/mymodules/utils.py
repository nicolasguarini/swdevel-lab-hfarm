import pandas as pd

def top_wines_by_rating(df_wines, limit=10):
    top_wines = df_wines.sort_values(by="Rating", ascending=False)
    return top_wines.head(limit)

def wines_by_recent_year(df_wines, limit = 10):
    df_wines = df_wines[df_wines['Year'] != 'N.V.']
    most_recent_wines = df_wines.sort_values(by="Year", ascending=False)
    return most_recent_wines.head(limit)

def wines_by_least_recent_year(df_wines, limit=10):
    df_wines = df_wines[df_wines['Year'] != 'N.V.']
    least_recent_wines = df_wines.sort_values(by="Year", ascending=True)
    return least_recent_wines.head(limit)

def wines_by_type(df, wine_type, limit=10):
    filtered_wines = df[df["type"] == wine_type]
    return filtered_wines.head(limit)
