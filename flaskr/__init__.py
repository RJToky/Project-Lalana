import json
from flask import Flask, render_template, request
from dao.LalanaDetailDao import LalanaDetailDAO

def create_app():
    app = Flask(__name__, template_folder = "../web/", static_folder = "../static/")

    @app.route("/")
    def index():
        map_template = render_template("map.html")
        cout_template = render_template("cout.html", data = LalanaDetailDAO.find_all(None))
        return map_template + cout_template
    
    @app.route("/traitement", methods = ["GET", "POST"])
    def traitement():
        data = LalanaDetailDAO.find_by_id(None, int(request.args.get("idLalana")))
        data = [data.nomLalana, data.nomType, data.cout]
        return json.dumps(data)

    return app