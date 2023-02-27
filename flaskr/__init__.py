from flask import Flask, render_template

app = Flask(__name__, template_folder = "../web/")

@app.route("/")
def index():
    return "Hello world"

@app.route("/map")
def map():
    return render_template("map.html")