#!/usr/bin/python3
"""
A simple web app
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    '''displays welcome message'''
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hello_HBNB():
    '''displays HBNB'''
    return ("HBNB")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
