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
