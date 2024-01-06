"""
Backend module for the FastAPI application.

This module defines a FastAPI application that serves
as the backend for the project.
"""

from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime
import pandas as pd
from .mymodules.utils import *


app = FastAPI()

df_red = pd.read_csv('/app/app/datasets/Red.csv')
df_rose = pd.read_csv('/app/app/datasets/Rose.csv')
df_sparkling = pd.read_csv('/app/app/datasets/Sparkling.csv')
df_white = pd.read_csv('/app/app/datasets/White.csv')

df_red["type"] = "red"
df_rose["type"] = "rose"
df_sparkling["type"] = "sparkling"
df_white["type"] = "white"

df_wines = pd.concat([df_red, df_rose, df_sparkling, df_white])
df_wines.columns = map(str.lower, df_wines.columns)
df_wines['year'] = pd.to_numeric(df_wines['year'], errors='coerce').astype('Int64')


@app.get('/top-wines')
def get_most_rated_wines(limit: int = 10):
    """
    Endpoint to get the best reviewed wines.

    Parameters:
        limit: (optional) an integer representing the max number of wines that has to be returned
    Returns:
        dict: top wines sorted by rating (descending)
    """
    top_wines_dict = top_wines_by_rating(df_wines, limit).to_dict(orient='records')
    return JSONResponse(content=top_wines_dict)

@app.get('/most-recent-wines')
def get_most_recent_wines(limit: int = 10):
    """
    Endpoint to get the best reviewed wines.

    Parameters:
        limit: (optional) an integer representing the max number of wines that has to be returned
    Returns:
        dict: top wines sorted by rating (descending)
    """
    most_recent_wine = wines_by_recent_year(df_wines, limit).to_dict(orient='records')
    return JSONResponse(content=most_recent_wine)

@app.get('/years-range')
def get_years_range():
    years_range = years_in_wines(df_wines)
    
    return JSONResponse(content=years_range)

@app.get('/num-ratings-max-value')
def get_num_ratings_max_value():
    num_ratings_max_value = max_number_of_ratings(df_wines)
    return JSONResponse(content=num_ratings_max_value)
    
@app.get('/countries')
def get_countries():
    countries = countries_df(df_wines)
    return JSONResponse(content=countries)

@app.get('/types')
def get_types():
    types = types_df(df_wines)
    return JSONResponse(content=types)

@app.get('/least-recent-wines')
def get_least_recent_year(limit: int = 10):
    """
    Endpoint to get the best reviewed wines.

    Parameters:
        limit: (optional) an integer representing the max number of wines that has to be returned
    Returns:
        dict: top wines sorted by rating (descending)
    """
    least_recent_wines = wines_by_least_recent_year(df_wines, limit).to_dict(orient='records')
    return JSONResponse(content=least_recent_wines) 

@app.get('/advanced-search')
def advanced_search_wines(
    name: str = Query(None),
    type: str = Query(None),
    country: str = Query(None),
    region: str = Query(None),
    winery: str = Query(None),
    # ----- 
    rating_start: float = Query(None),
    rating_end: float = Query(None),
    # -----
    num_ratings_start: int = Query(None), 
    num_ratings_end: int = Query(None),
    # -----
    price_start: float = Query(None),
    price_end: float = Query(None),
    # -----
    year_start: int = Query(None),
    year_end: int = Query(None),
    
    limit: int = Query(10),
):
    """
    Endpoint for advanced search of wines.
    
    Parameters:
        category (optional): Wine category.
        country (optional): Wine country.
        region (optional): Wine region.
        winery (optional): Wine winery.
        rating (optional): Wine rating.
        num_ratings (optional): Number of ratings for the wine.
        price (optional): Wine price.
        year (optional): Wine year.
        limit (optional): Max number of wines to return.

    Returns:
        dict: Wines matching the specified criteria.
    """
    filters = {
        "name": name,
        "type": type,
        "country": country,
        "region": region,
        "winery": winery,
        "rating": (rating_start, rating_end) if rating_start is not None and rating_end is not None else None,
        "numberofratings": (num_ratings_start, num_ratings_end) if num_ratings_start is not None and num_ratings_end is not None else None,
        "price": (price_start, price_end) if price_start is not None and price_end is not None else None,
        "year": (year_start, year_end) if year_start is not None and year_end is not None else None,
    }
    result = filter_wines(df_wines, filters).head(limit).to_dict(orient='records')

    print("RESULT", result)

    return JSONResponse(content=result)

@app.get('/')
def read_root():
    """
    Root endpoint for the backend.

    Returns:
        dict: Information about the API and its endpoints.
    """
    info = {
        "message": "Welcome to the Wine API!",
        "description": "This API provides information about different types of wines.",
        "endpoints": {
            "/top-wines": "Get the best-reviewed wines.",
            "/most-recent-wines": "Get the most recently reviewed wines.",
            "/least-recent-wines": "Get the least recently reviewed wines.",
            "/get-date": "Get the current date."
        }
    }
    return JSONResponse(content=info)



@app.get('/get-date')
def get_date():
    """
    Endpoint to get the current date.

    Returns:
        dict: Current date in ISO format.
    """
    current_date = datetime.now().isoformat()
    return JSONResponse(content={"date": current_date})
