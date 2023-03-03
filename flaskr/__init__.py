import json
from map import *
from flask import Flask, render_template, request
from connection.Bdd import Bdd
from dao.LalanaDetailDao import LalanaDetailDAO
from dao.CoucheDetailDAO import CoucheDetailDAO
from dao.TypeCoucheDAO import TypeCoucheDAO
from model.Lalana import Lalana

def create_app():
    app = Flask(__name__, template_folder = "../web/", static_folder = "../static/")

    @app.route("/")
    def index():
        con = Bdd.connect()

        data = LalanaDetailDAO.find_all(con)
        row = [data[0].nomLalana, data[0].nomType, data[0].coutReparation, time_as_text(data[0].dureeReparation)]
        list_lalana = LalanaDetailDAO.find_all(con)

        map_template = render_template("map.html")
        cout_template = render_template("cout.html", data = row, list_lalana = list_lalana)

        con.close()
        return map_template + cout_template
    
    @app.route("/traitement_cout", methods = ["GET", "POST"])
    def traitement_cout():
        data = LalanaDetailDAO.find_by_id(None, int(request.args.get("idLalana")))
        data = [data.nomLalana, data.nomType, data.coutReparation, time_as_text(data.dureeReparation)]

        return json.dumps(data)

    @app.route("/couche")
    def couche(
        data = [
            TypeCoucheDAO.find_all(None),
            LalanaDetailDAO.find_all(None),
            CoucheDetailDAO.find_all(None)
        ]):
        return render_template("couche.html", data = data)
    
    @app.route("/result_couche", methods = ["GET", "POST"])
    def result_couche():
        idTypeCouche = int(request.args.get("idTypeCouche"))
        idLalana = int(request.args.get("idLalana"))
        rayon = -1

        con = Bdd.connect()

        if idTypeCouche == 0 and idLalana == 0 and request.args.get("rayon") == "":
            return couche()

        elif idTypeCouche != 0 and idLalana == 0 and request.args.get("rayon") == "":
            data = [
                TypeCoucheDAO.find_all(con),
                LalanaDetailDAO.find_all(con), 
                CoucheDetailDAO.find_by_idTypeCouche(con, int(idTypeCouche))
            ]
            return couche(data)
        
        elif idTypeCouche == 0 and idLalana != 0 and request.args.get("rayon") != "":
            rayon = float(request.args.get("rayon"))
            data = [
                TypeCoucheDAO.find_all(con),
                LalanaDetailDAO.find_all(con), 
                CoucheDetailDAO.find_all_couche_in_lalana(con, idLalana, rayon)
            ]

        else:
            if request.args.get("rayon") != "":
                rayon = float(request.args.get("rayon"))

            data = [
                TypeCoucheDAO.find_all(con),
                LalanaDetailDAO.find_all(con), 
                CoucheDetailDAO.find_all_couche_in_lalana_by_idTypeCouche(con, idTypeCouche, idLalana, rayon)
            ]
            
        con.close()
        return couche(data)
    
    @app.route("/lalana")
    def lalana(
        data = [
            TypeCoucheDAO.find_all(None),
            ["---"]
        ]):
        return render_template("lalana.html", data = data)
    
    @app.route("/result_lalana", methods = ["GET", "POST"])
    def result_lalana():
        idTypeCouche = int(request.args.get("idTypeCouche"))

        if idTypeCouche != 0 and request.args.get("rayon") != "":
            rayon = float(request.args.get("rayon"))

            data = [
                TypeCoucheDAO.find_all(None),
                Lalana.trier_par_nbr_couche(None, idTypeCouche, rayon)
            ]
            return render_template("lalana.html", data = data)

        return lalana()
    
    return app