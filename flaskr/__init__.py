import folium
import map
from flask import Flask, render_template, request, redirect
from dao.CoucheDAO import CoucheDAO
from dao.CoucheDetailDAO import CoucheDetailDAO
from dao.SimbaDetailDAO import SimbaDetailDAO
from dao.SimbaDAO import SimbaDAO
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

        r_map = folium.Map(
            location = [-19.001707, 47.538223],
            zoom_start = 13
        )
        for i in range(len(data)):
            popup_couche = """
                <p>Nom : """ + data[i]._nom + """</p>
                <p>Nbr : """ + str(data[i]._nbr) + """</p>
            """
            
            folium.Marker(
                location = [data[i]._x, data[i]._y],
                icon = folium.Icon(icon = map.get_icon(data[i]._karazany), prefix = "fa", color = "green"),
                popup = popup_couche
            ).add_to(r_map)

            folium.Circle(
                location = [data[i]._x, data[i]._y],
                radius = limit,
                fill = True,
                color = "green"
            ).add_to(r_map)

            coord_simba = SimbaDetailDAO.find_simba_within_limit(con, data[i]._coord, limit)

            for i in range(len(coord_simba)):
                folium.PolyLine(
                    locations = [[coord_simba[i]._x_debut, coord_simba[i]._y_debut], [coord_simba[i]._x_fin, coord_simba[i]._y_fin]],
                    color = "red"
                ).add_to(r_map)

                simba = SimbaDAO.find_by_id(con, coord_simba[i]._idSimba)

                popup_pk = """
                    <p>Cout : """ + str(simba.calc_cout(con, 6000)) + """ Ar</p>
                    <p>Duree : """ + str(simba.calc_duration(con, 6)) + """ h</p>
                """

                folium.Marker(
                    location = [coord_simba[i]._x_debut, coord_simba[i]._y_debut],
                    icon = folium.Icon(color = "red"),
                    popup = popup_pk
                ).add_to(r_map)

                folium.Marker(
                    location = [coord_simba[i]._x_fin, coord_simba[i]._y_fin],
                    icon = folium.Icon(color = "red"),
                    popup = popup_pk
                ).add_to(r_map)

        r_map.save("./web/map.html")
        
        con.close()
        return redirect("/map")

    return app