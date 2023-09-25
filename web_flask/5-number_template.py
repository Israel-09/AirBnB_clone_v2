#!/usr/bin/python3
"""
A simple web app
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    '''displays welcome message'''
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hello_HBNB():
    '''displays HBNB'''
    return ("HBNB")


@app.route("/c/<text>")
def dynamic_c(text):
    '''Format c text based on url'''
    f_text = text.replace('_', ' ')
    return (f"C {f_text}")


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def dynamic_python(text="is cool"):
    '''Format python text based on url'''
    f_text = text.replace('_', ' ')
    return (f"Python {f_text}")


@app.route("/number/<int:n>", strict_slashes=False)
def if_number(n):
    '''displays n only if n is an integer'''
    return(f"{n} is a number")


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", number=n)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
