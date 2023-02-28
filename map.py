import folium
from connection.Bdd import Bdd
from dao.CoucheDetailDAO import CoucheDetailDAO
from dao.SimbaDetailDAO import SimbaDetailDAO

def init():
    # -19.001707, 47.538223
    map = folium.Map(
        location = [-19.001707, 47.538223],
        zoom_start = 13
    )

    con = Bdd.connect()

    couche_detail = CoucheDetailDAO.find_all(con)

    for i in range(len(couche_detail)):
        folium.Marker(
            location = [couche_detail[i][2], couche_detail[i][3]],
            icon = folium.Icon(icon = couche_detail[i][1], prefix = "fa", color = "green"),
            popup = couche_detail[i][4]
        ).add_to(map)
    
    coord_simba = SimbaDetailDAO.find_all(con)

    for i in range(len(coord_simba)):
        folium.PolyLine(
            locations = [[coord_simba[i][0], coord_simba[i][1]], [coord_simba[i][2], coord_simba[i][3]]],
            color = "red"
        ).add_to(map)

    map.save("./web/map.html")
    con.close()

if __name__ == "__main__":
    init()