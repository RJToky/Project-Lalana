import folium
import map
from flask import Flask, render_template, request, redirect
from dao.CoucheDAO import CoucheDAO
from dao.CoucheDetailDAO import CoucheDetailDAO
from dao.SimbaDetailDAO import SimbaDetailDAO
from connection.Bdd import Bdd

def create_app():
    app = Flask(__name__, template_folder = "../web/", static_folder = "../static/")

    @app.route("/")
    def index():
        map.init()
        map_template = render_template("map.html")
        form_template = render_template("form.html", data = CoucheDAO.find_all(None))
        return map_template + form_template
    
    @app.route("/map")
    def result():
        map_template = render_template("map.html")
        form_template = render_template("form.html", data = CoucheDAO.find_all(None))
        return map_template + form_template
    
    @app.route("/traitement", methods = ["GET", "POST"])
    def traitement():
        con = Bdd.connect()
        limit = request.form["limit"]

        if request.form["couche"] == "0":
            data = CoucheDetailDAO.find_all(con)
        else:
            data = CoucheDetailDAO.find_by_id(con, request.form["couche"])

        map = folium.Map(
            location = [-19.001707, 47.538223],
            zoom_start = 13
        )
        for i in range(len(data)):
            folium.Marker(
                location = [data[i][2], data[i][3]],
                icon = folium.Icon(icon = data[i][1], prefix = "fa", color = "green"),
                popup = data[i][4]
            ).add_to(map)

            folium.Circle(
                location = [data[i][2], data[i][3]],
                radius = limit,
                fill = True,
                color = "green"
            ).add_to(map)

            coord_simba = SimbaDetailDAO.find_simba_within_limit(con, data[i][6], limit)

            for i in range(len(coord_simba)):
                folium.PolyLine(
                    locations = [[coord_simba[i][0], coord_simba[i][1]], [coord_simba[i][2], coord_simba[i][3]]],
                    color = "red"
                ).add_to(map)

        map.save("./web/map.html")
        
        con.close()
        return redirect("/map")

    return app