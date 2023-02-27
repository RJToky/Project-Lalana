import folium
from flask import Flask, render_template, request, redirect
from dao.CoucheDAO import CoucheDAO
from dao.CoucheDetailDAO import CoucheDetailDAO

def create_app():
    app = Flask(__name__, template_folder = "../web/", static_folder = "../static/")

    @app.route("/")
    @app.route("/map")
    def index():
        map_template = render_template("map.html")
        form_template = render_template("form.html", data = CoucheDAO.find_all(None))
        return map_template + form_template
    
    @app.route("/traitement", methods = ["GET", "POST"])
    def traitement():
        if request.form["couche"] == "0":
            data = CoucheDetailDAO.find_all(None)
        else:
            data = CoucheDetailDAO.find_by_id(None, request.form["couche"])

        map = folium.Map(
            location = [-19.001707, 47.538223],
            zoom_start = 11
        )
        for i in range(len(data)):
            folium.Marker(
                location = [data[i][2], data[i][3]],
                icon = folium.Icon(icon = data[i][1], prefix = "fa", color = "green"),
                popup = data[i][4]
            ).add_to(map)

            folium.Circle(
                location = [data[i][2], data[i][3]],
                radius = request.form["limite"],
                fill = True,
                color = "green"
            ).add_to(map)

        map.save("./web/map.html")

        return redirect("/")

    return app