#!/usr/bin/python3a
"""
a module that starts a flask app and render routes
"""
from flask import Flask, abort, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """landing url"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """ renders the route /hbnb """
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    """ handles a route /c with some given value """
    return f"C {text.replace('_', ' ')}"


@app.route('/python/')
@app.route('/python/<text>')
def pythonr(text='is cool'):
    """ handles a route /python with some given value """
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<n>')
def is_number(n):
    """checks if n is number"""
    try:
        n = int(n)
        return f"{n} is a number"
    except ValueError as err:
        abort(404)


@app.route('/number_template/<int:n>')
def number_template(n):
    """ Checks if n is a number and renders a template """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
