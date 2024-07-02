#!/usr/bin/env python3

"""
A simple Flask application that serves a web page.

This script sets up a basic Flask web server with one route ("/") that renders
an HTML template.

Modules:
    flask: A micro web framework for Python.

Functions:
    index(): Renders and returns the '0-index.html' template.

Usage:
    Run this script to start a Flask web server and serve the '0-index.html'
    at the root URL.
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config():
    """Configuration for Babel."""

    LANGUAGES = ["en", "fr"]


# Initialize the Flask application
app = Flask(__name__)
babel = Babel(app, default_locale=Config.LANGUAGES[0], default_timezone='UTC')


@app.route("/")
def index():
    """
    Route for the root URL ("/").

    Returns:
        str: The rendered HTML template '0-index.html'.
    """
    return render_template('1-index.html')


# Run the Flask web server if this script is executed directly
if __name__ == '__main__':
    app.run()
