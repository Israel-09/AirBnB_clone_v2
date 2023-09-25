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


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
