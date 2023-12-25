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

def filter_by_type(df, type):
    return df[df["type"] == type]

def filter_by_name(df, name):
    return df[df["name"].contains(name)]

def filter_by_country(df, country):
    return df[df["country"] == country]

def filter_by_regiong(df, region):
    return df[df["region"] == region]

def filter_by_winery(df, winery):
    return df[df["winery"] == winery]

def filter_by_rating(df, rating):
    return df[df["rating"] == rating]

def filter_by_num_ratings(df, num_ratings):
    return df[df["numberofratings"] == num_ratings]

def filter_by_price(df, price):
    return df[df["price"] == price]

def filter_by_year(df, year):
    
    return df[df["year"] == str(year)]

# Main filtering function
def filter_wines(df_wines, filters):
    filtered_wines = df_wines.copy()
    print(filtered_wines.head())
    for key, value in filters.items():
        if value is not None and key in df_wines.columns:
            key_lower = key.lower()  # Convert key to lowercase
            filter_function = get_filter_function(key_lower)
            filtered_wines = filter_function(filtered_wines, value)

    print("GUARDA QUI", filtered_wines["region"])
    return filtered_wines

# Helper function to map filter keys to corresponding filter functions
def get_filter_function(key):
    filter_functions = {
        "type": filter_by_type,
        "country": filter_by_country,
        "rating": filter_by_rating,
        "numberofratings": filter_by_num_ratings,
        "price": filter_by_price,
        "year": filter_by_year,
    }
    return filter_functions.get(key, lambda df, value: df)  # Default to identity function
