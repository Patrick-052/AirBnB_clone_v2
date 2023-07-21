#!/usr/bin/python3
"""Starting a Flask web application and ensuring
   that its listening on 0.0.0.0, port 5000"""

from flask import Flask

app = Flask("__name__")


@app.route("/", strict_slashes=False)
def hello_hbnb():
    "returns a specific string"
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    "returns a specific string"
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c(text):
    "passing a variable to the url"
    return f"C {text.replace('_', ' ')}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=None)
