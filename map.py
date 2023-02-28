import folium
from connection.Bdd import Bdd
from dao.CoucheDetailDAO import CoucheDetailDAO
from dao.SimbaDetailDAO import SimbaDetailDAO
from dao.SimbaDAO import SimbaDAO

def get_icon(key: str) -> str:
    if key == "population":
        return "home"
    return key

def init():
    # -19.001707, 47.538223
    map = folium.Map(
        location = [-19.001707, 47.538223],
        zoom_start = 13
    )

    con = Bdd.connect()

    couche_detail = CoucheDetailDAO.find_all(con)

    for i in range(len(couche_detail)):
        popup_couche = """
            <p>Nom : """ + couche_detail[i][4] + """</p>
            <p>Nbr : """ + str(couche_detail[i][7]) + """</p>
        """
        folium.Marker(
            location = [couche_detail[i][2], couche_detail[i][3]],
            icon = folium.Icon(icon = get_icon(couche_detail[i][1]), prefix = "fa", color = "green"),
            popup = popup_couche
        ).add_to(map)
    
    coord_simba = SimbaDetailDAO.find_all(con)

    for i in range(len(coord_simba)):
        folium.PolyLine(
            locations = [[coord_simba[i][0], coord_simba[i][1]], [coord_simba[i][2], coord_simba[i][3]]],
            color = "red"
        ).add_to(map)

        simba = SimbaDAO.find_by_id(con, coord_simba[i][0])
                
        popup_pk = """
            <p>Cout : """ + str(simba.calc_cout(con, 6000)) + """ Ar</p>
            <p>Duree : """ + str(simba.calc_duration(con, 6)) + """ h</p>
        """

        folium.Marker(
            location = [coord_simba[i][0], coord_simba[i][1]],
            icon = folium.Icon(color = "red"),
            popup = popup_pk
        ).add_to(map)

        folium.Marker(
            location = [coord_simba[i][2], coord_simba[i][3]],
            icon = folium.Icon(color = "red"),
            popup = popup_pk
        ).add_to(map)

    map.save("./web/map.html")
    con.close()

if __name__ == "__main__":
    init()