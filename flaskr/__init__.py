import folium
from map import *
from flask import Flask, render_template, request, redirect
from dao.TypeCoucheDAO import TypeCoucheDAO
from dao.SimbaDetailDAO import SimbaDetailDAO
from dao.CoucheDetailDAO import CoucheDetailDAO
from dao.SimbaDAO import SimbaDAO
from connection.Bdd import Bdd

def create_app():
    app = Flask(__name__, template_folder = "../web/", static_folder = "../static/")

    @app.route("/")
    def index():
        map_template = render_template("map.html")
        form_template = render_template("form.html", data = TypeCoucheDAO.find_all(None))
        return map_template + form_template
    
    @app.route("/map")
    def result():
        map_template = render_template("map.html")
        form_template = render_template("form.html", data = TypeCoucheDAO.find_all(None))
        return map_template + form_template
    
    @app.route("/traitement", methods = ["GET", "POST"])
    def traitement():
        folium_map = instance_map()

        con = Bdd.connect()
        limit = request.form["limit"]
        typeCouche = request.form["typeCouche"]

        if typeCouche == "0":
            couche_detail = CoucheDetailDAO.find_all(con)
        else:
            couche_detail = CoucheDetailDAO.find_by_idTypeCouche(con, typeCouche)

        for i in range(len(couche_detail)):
            popup_couche = """
                <p>Nom : """ + couche_detail[i].nom + """</p>
                <p>Nbr : """ + str(couche_detail[i].nbr) + """</p>
            """
            
            folium.Marker(
                location = [couche_detail[i].x, couche_detail[i].y],
                icon = folium.Icon(icon = get_icon(couche_detail[i].nomType), prefix = "fa", color = "green"),
                popup = popup_couche
            ).add_to(folium_map)

            folium.Circle(
                location = [couche_detail[i].x, couche_detail[i].y],
                radius = limit,
                fill = True,
                color = "green"
            ).add_to(folium_map)

            simba_detail = SimbaDetailDAO.find_simba_within_couche(con, couche_detail[i].coord, limit)

            for i in range(len(simba_detail)):
                folium.PolyLine(
                    locations = [[simba_detail[i].x_debut, simba_detail[i].y_debut], [simba_detail[i].x_fin, simba_detail[i].y_fin]],
                    color = "red"
                ).add_to(folium_map)

                simba = SimbaDAO.find_by_id(con, simba_detail[i].idSimba)
                
                popup_pk = """
                    <p>Cout : """ + str(simba.calc_cout(con)) + """ Ar</p>
                    <p>Duree : """ + str(simba.calc_duration(con)) + """ h</p>
                """

                folium.Marker(
                    location = [simba_detail[i].x_debut, simba_detail[i].y_debut],
                    icon = folium.Icon(color = "red"),
                    popup = popup_pk
                ).add_to(folium_map)

                folium.Marker(
                    location = [simba_detail[i].x_fin, simba_detail[i].y_fin],
                    icon = folium.Icon(color = "red"),
                    popup = popup_pk
                ).add_to(folium_map)

        folium_map.save("./web/map.html")
        
        con.close()
        return redirect("/map")

    return app