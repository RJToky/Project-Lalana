import folium
from connection.Bdd import Bdd
from dao.CoucheDetailDAO import CoucheDetailDAO
from dao.SimbaDetailDAO import SimbaDetailDAO
from dao.TypeCoucheDAO import TypeCoucheDAO
from dao.SimbaDAO import SimbaDAO
from dao.PkDAO import PkDAO

def time_as_text(time: float) -> str:
    if time < 24:
        return str(time) + "h"
    j = int(time // 24)
    h = int(time % 24)
    return str(j) + "j " + str(h) + "h"

def get_icon(key: str) -> str:
    if key == "Etablissement":
        return "school"
    elif key == "Hopital":
        return "hospital"
    return "home"

def instance_map(location = [-19.001707, 47.538223], zoom_start = 13):
    folium_map = folium.Map(
        location = location,
        zoom_start = zoom_start
    )
    return folium_map

def init():
    folium_map = instance_map()
    con = Bdd.connect()

    type_couche = TypeCoucheDAO.find_all(con)
    for i in range(len(type_couche)):
        layer_couche = folium.FeatureGroup(type_couche[i].nomType)
        couche_detail = CoucheDetailDAO.find_by_idTypeCouche(con, type_couche[i].idTypeCouche)

        for j in range(len(couche_detail)):
            popup_couche = """
                <p>Nom : """ + couche_detail[j].nom + """</p>
                <p>Nbr : """ + str(couche_detail[j].nbr) + """</p>
            """
            folium.Marker(
                location = [couche_detail[j].x, couche_detail[j].y],
                icon = folium.Icon(icon = get_icon(couche_detail[j].nomType), prefix = "fa", color = "green"),
                popup = popup_couche
            ).add_to(layer_couche)

            layer_couche.add_to(folium_map)
    
    simba_detail = SimbaDetailDAO.find_all(con)
    for i in range(len(simba_detail)):
        layer_simba = folium.FeatureGroup("Simba")

        folium.PolyLine(
            locations = [[simba_detail[i].x_debut, simba_detail[i].y_debut], [simba_detail[i].x_fin, simba_detail[i].y_fin]],
            color = "red"
        ).add_to(layer_simba)

        simba = SimbaDAO.find_by_id(con, simba_detail[i].idSimba)
        
        popup_pk1 = """
            <p>PK : """ + str(int(PkDAO.find_by_id(con, simba.idPk_debut).valeur)) + """</p>
            <p>Cout : """ + str(simba.calc_cout(con)) + """ Ar</p>
            <p>Duree : """ + time_as_text(simba.calc_duration(con)) + """ </p>
        """

        folium.Marker(
            location = [simba_detail[i].x_debut, simba_detail[i].y_debut],
            icon = folium.Icon(color = "red"),
            popup = popup_pk1
        ).add_to(layer_simba)

        popup_pk2 = """
            <p>PK : """ + str(int(PkDAO.find_by_id(con, simba.idPk_fin).valeur)) + """</p>
            <p>Cout : """ + str(simba.calc_cout(con)) + """ Ar</p>
            <p>Duree : """ + time_as_text(simba.calc_duration(con)) + """ </p>
        """
        folium.Marker(
            location = [simba_detail[i].x_fin, simba_detail[i].y_fin],
            icon = folium.Icon(color = "red"),
            popup = popup_pk2
        ).add_to(layer_simba)

        layer_simba.add_to(folium_map)

    folium.LayerControl().add_to(folium_map)
    folium_map.save("./web/map.html")
    
    con.close()

if __name__ == "__main__":
    init()