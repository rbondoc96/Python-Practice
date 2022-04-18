#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    greeting = "World"

    return render_template("index.html", **{
        "greeting": greeting
    })


@app.route("/foo")
def foo():
    return render_template("foo.html")


if __name__ == "__main__":
    app.run()