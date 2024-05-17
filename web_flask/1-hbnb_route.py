#!/usr/bin/python3a
"""
a module that starts a flask app and render routes
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """landing url"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """ renders the route /hbnb """
    return "HBNB"


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
