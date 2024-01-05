"""
Frontend module for the Flask application.

This module defines a simple Flask application that serves as the frontend for the project.
"""

from flask import Flask, render_template
import requests
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField
import os

BACKEND_HOST = 'http://backend/'
DEFAULT_TYPE_CHOICE = "Select type..."
DEFAULT_COUNTRY_CHOICE = "Select country..."

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)

class SearchWinesForm(FlaskForm):
    name = StringField(
        label="Wine name...", 
        render_kw={"placeholder": "Wine name..."}
    )

    type = SelectField(choices=[
        DEFAULT_TYPE_CHOICE, 
        "white", 
        "red", 
        "sparkling", 
        "rose"
    ]) # TODO: get all types from backend

    country = SelectField(choices=[
        DEFAULT_COUNTRY_CHOICE, 
        "Italy",
        "Germany", 
        "France",
        "Austria"
    ]) # TODO: get all countries from backedn
    
    submit = SubmitField('Search Wines!')

@app.route('/')
def index():
    """
    Render the index page.

    Returns:
        str: Rendered HTML content for the index page.
    """

    return render_template('index.html', top_wines=fetch_top_wines(6), most_recent_wines=fetch_most_recent_wines(6), least_recent_wines=fetch_least_recent_wines(6))

def fetch_top_wines(limit=10):
    url = BACKEND_HOST + "top-wines?limit=" + str(limit)

    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching wines from backend: {e}")
        return 'Wines not available'

def fetch_most_recent_wines(limit=10):
    url = BACKEND_HOST + "most-recent-wines?limit=" + str(limit)

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching wines from backend: {e}")
        return 'Wines not available'
    
def fetch_least_recent_wines(limit=10):
    url = BACKEND_HOST + "least-recent-wines?limit=" + str(limit)

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching wines from backend: {e}")
        return 'Wines not available'

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
    
        url = f'{BACKEND_HOST}advanced-search?limit=24&'

        if name != "":
            url += f'name={name}&'

        if type != DEFAULT_TYPE_CHOICE:
            url += f'type={type}&'

        if country != DEFAULT_COUNTRY_CHOICE:
            url += f'country={country}&'

        print("URL: " + url)

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return render_template('advanced-search.html', form=form, result=data, error_message=error_message)
        else:
            error_message = f'Error: Unable to fetch data from FastAPI Backend'

    return render_template('advanced-search.html', form=form, result=None, error_message=error_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
