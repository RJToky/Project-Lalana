import folium
from map import *
from flask import Flask, render_template, request, redirect
from dao.TypeCoucheDAO import TypeCoucheDAO
from connection.Bdd import Bdd

def create_app():
    app = Flask(__name__, template_folder = "../web/", static_folder = "../static/")

    @app.route("/")
    def index():
        map_template = render_template("map.html")
        form_template = render_template("form.html", data = TypeCoucheDAO.find_all(None))
        return map_template + form_template
    
    @app.route("/traitement", methods = ["GET", "POST"])
    def traitement():
        con = Bdd.connect()
        con.close()
        return redirect("/")

    return app