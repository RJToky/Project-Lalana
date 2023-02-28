import folium
from connection.Bdd import Bdd
from dao.CoucheDetailDAO import CoucheDetailDAO
from dao.SimbaDetailDAO import SimbaDetailDAO
from dao.SimbaDAO import SimbaDAO

def get_icon(key: str) -> str:
    if key == "Etablissement":
        return "school"
    elif key == "Hopital":
        return "hospital"
    return "marker"

def instance_map(location = [-19.001707, 47.538223], zoom_start = 13):
    folium_map = folium.Map(
        location = location,
        zoom_start = zoom_start
    )
    return folium_map

def init():
    folium_map = instance_map()
    con = Bdd.connect()

    couche_detail = CoucheDetailDAO.find_all(con)
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
    
    simba_detail = SimbaDetailDAO.find_all(con)
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

if __name__ == "__main__":
    init()