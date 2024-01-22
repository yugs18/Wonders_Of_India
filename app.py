from flask import Flask, flash, redirect, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/gommateshwara")
def gommateshwara():
    return render_template("gommateshwara.html")


@app.route("/hampi")
def hampi():
    return render_template("hampi.html")


@app.route("/harmandir")
def harmandir():
    return render_template("harmandir.html")


@app.route("/khajuraho")
def khajuraho():
    return render_template("khajuraho.html")


@app.route("/konark")
def konark():
    return render_template("konark.html")


@app.route("/nalanda")
def nalanda():
    return render_template("nalanda.html")


@app.route("/taj")
def taj():
    return render_template("taj.html")
