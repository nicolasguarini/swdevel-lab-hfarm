"""
Backend module for the FastAPI application.

This module defines a FastAPI application that serves
as the backend for the project.
"""

from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime
import pandas as pd
from .mymodules.utils import top_wines_by_rating, wines_by_least_recent_year, wines_by_recent_year, wines_by_type


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

@app.get('/wines-by-type')
def get_wines_by_type(wine_type, limit: int = 10):
    """
    Endpoint to get wines by type.

    Parameters:
        limit: (optional) an integer representing the max number of wines that has to be returned
        wine_type: (mandatory) typology of wine [red, rose, sparkling, white]
    Returns:
        dict: top wines sorted by rating (descending)
    """
    wines_by_type_result = wines_by_type(df_wines, wine_type, limit).to_dict(orient='records')
    return JSONResponse(content=wines_by_type_result)

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
