#!/usr/bin/python3
"""Starting a Flask web application and ensuring
   that its listening on 0.0.0.0, port 5000"""

from flask import Flask, render_template

app = Flask("__name__")


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """returns a specific string"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns a specific string"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """passing a variable to the url"""
    return f"C {text.replace('_', ' ')}"


@app.route("/python/", defaults={"text": "is cool"},
           strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """return value of variable to a url else return
    default"""
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def valid_int(n):
    """displaying the variable if its an int"""
    if isinstance(n, int):
        return f"{n} is a number"


@app.route("/number_template/<int:n>",

           strict_slashes=False)
def html_int(n):
    """displaying a html page if variable is an int"""
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=None)
