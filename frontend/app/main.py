"""
Frontend module for the Flask application.

This module defines a simple Flask application that serves as the frontend for the project.
"""

from flask import Flask, render_template
import requests
from countries import DEFAULT_COUNTRY_CHOICE
from fetch import fetch_least_recent_wines, fetch_most_recent_wines, fetch_top_wines
from wine_types import DEFAULT_TYPE_CHOICE
from form import SearchWinesForm
import datetime
from constants import BACKEND_HOST, MAX_WINE_PRICE, SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def index():
    """
    Render the index page.

    Returns:
        str: Rendered HTML content for the index page.
    """

    return render_template(
        'index.html', 
        top_wines=fetch_top_wines(6), 
        most_recent_wines=fetch_most_recent_wines(6), 
        least_recent_wines=fetch_least_recent_wines(6)
    )

@app.route('/advanced-search', methods=['GET', 'POST'])
def advanced_search():
    """
    Render the advanced search page.

    Returns:
        str: Rendered HTML content for the advanced search page.
    """

    form = SearchWinesForm()
    error_message = None  # Initialize error message

    if form.validate_on_submit():
        type = form.type.data
        country = form.country.data
        name = form.name.data
        year_start = form.year_start.data
        year_end = form.year_end.data
        rating_start = form.rating_start.data
        rating_end = form.rating_end.data
        price_start = form.price_start.data
        price_end = form.price_end.data
    
        url = f'{BACKEND_HOST}advanced-search?limit=24&'

        if name != "":
            url += f'name={name}&'

        if type != DEFAULT_TYPE_CHOICE:
            url += f'type={type}&'

        if country != DEFAULT_COUNTRY_CHOICE:
            url += f'country={country}&'

        if year_start == None:
            year_start = 1500

        if year_end == None:
            year_end = datetime.date.today().year

        if rating_start == None:
            rating_start = 0.0
        
        if rating_end == None:
            rating_end = 5.0

        if price_start == None:
            price_start = 0

        if price_end == None:
            price_end = MAX_WINE_PRICE

        url += f'year_start={year_start}&year_end={year_end}&'
        url += f'rating_start={rating_start}&rating_end={rating_end}&'
        url += f'price_start={price_start}&price_end={price_end}&'

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return render_template('advanced-search.html', form=form, result=data, error_message=error_message)
        else:
            error_message = f'Error: Unable to fetch data from FastAPI Backend'

    return render_template('advanced-search.html', form=form, result=None, error_message=error_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
