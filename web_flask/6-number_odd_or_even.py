#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Hello is displayed"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """display c"""
    texts = text.replace('_', ' ')
    return "C {}".format(texts)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """ displays python"""
    texts = text.replace('_', ' ')
    return "Python {}".format(texts)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """displays n"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def template(n):
    return render_template('templates/5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    return render_template('templates/6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
