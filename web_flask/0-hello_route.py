#!/usr/bin/python3
"""Starting a Flask web application"""

from flask import Flask
app = Flask("__name__")


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


if __name__ == 'main':
    app.run(host='0.0.0.0', port=5000, debug=None)
