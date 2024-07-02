#!/usr/bin/env python3

"""
A simple Flask application that serves a web page.

This script sets up a basic Flask web server with one route ("/") that renders
an HTML template.

Modules:
    flask: A micro web framework for Python.
    flask_babel: A Flask extension for i18n and l10n.

Functions:
    index(): Renders and returns the '0-index.html' template.

Usage:
    Run this script to start a Flask web server and serve the '0-index.html'
    at the root URL.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration for Babel."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Initialize the Flask application
app = Flask(__name__)
app.config.from_object(Config)

# Initialize Babel
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get_local function gets local language of user."""
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/")
def index():
    """
    Route for the root URL ("/").

    Returns:
        str: The rendered HTML template '0-index.html'.
    """
    return render_template('2-index.html')


# Run the Flask web server if this script is executed directly
if __name__ == '__main__':
    app.run()
