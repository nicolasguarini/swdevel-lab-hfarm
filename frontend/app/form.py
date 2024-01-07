from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    SubmitField,
    StringField,
    IntegerField,
    FloatField,
    validators
)
from countries import COUNTRIES, DEFAULT_COUNTRY_CHOICE
from wine_types import TYPES, DEFAULT_TYPE_CHOICE
import datetime


class SearchWinesForm(FlaskForm):
    """
    Represents a FlaskForm for searching wines with various criteria.

    Attributes:
        name (StringField): The name of the wine.
        type (SelectField): The type of the wine.
        country (SelectField): The country of origin for the wine.
        year_start (IntegerField): The minimum year of production for the wine.
        year_end (IntegerField): The maximum year of production for the wine.
        rating_start (FloatField): The minimum rating for the wine.
        rating_end (FloatField): The maximum rating for the wine.
        price_start (FloatField): The minimum price for the wine.
        price_end (FloatField): The maximum price for the wine.
        submit (SubmitField): Submit button for initiating the wine search.

    Note:
        This form includes various fields for specifying search criteria such as
        name, type, country, production year range, rating range, and price range.
        Each field is appropriately configured with placeholders, validation constraints,
        and default choices where applicable.
    """
    
    name = StringField(
        label="Wine name...",
        render_kw={"placeholder": "Wine name..."}
    )

    type = SelectField(choices=[DEFAULT_TYPE_CHOICE] + TYPES)
    country = SelectField(choices=[DEFAULT_COUNTRY_CHOICE] + COUNTRIES)

    year_start = IntegerField("Min Year", render_kw={
        "placeholder": "Min Year",
        "min": 0,
        "max": datetime.date.today().year,
    }, validators=[validators.Optional()])

    year_end = IntegerField("Min Year", render_kw={
        "placeholder": "Max Year",
        "min": 0,
        "max": datetime.date.today().year
    }, validators=[validators.Optional()])

    rating_start = FloatField("Min Rating", render_kw={
        "placeholder": "Min Rating",
        "min": 0,
        "max": 5
    }, validators=[validators.Optional()])

    rating_end = FloatField("Max Rating", render_kw={
        "placeholder": "Max Rating",
        "min": 0,
        "max": 5
    }, validators=[validators.Optional()])

    price_start = FloatField("Min Price", render_kw={
        "placeholder": "Min Price",
        "min": 0,
    }, validators=[validators.Optional()])

    price_end = FloatField("Max Price", render_kw={
        "placeholder": "Max Price",
        "min": 0,
    }, validators=[validators.Optional()])

    submit = SubmitField('Search Wines!')
