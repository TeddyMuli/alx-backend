#!/usr/bin/env python3
from flask import Flask
from flask_babel import Babel


class Config:
    """ Configuration for babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
babel = Babel(app)
