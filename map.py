import folium
from connection.Bdd import Bdd
from dao.LalanaDAO import *
from dao.CoucheDAO import *

def main():
    # -19.001707, 47.538223
    map = folium.Map(
        location = [-19.001707, 47.538223],
        zoom_start = 11
    )

    con = Bdd.connect()

    couche_coord = CoucheDAO.find_all_couche_coord(con)

    for i in range(len(couche_coord)):
        folium.Marker(
            location = [couche_coord[i][2], couche_coord[i][3]],
            icon = folium.Icon(icon = couche_coord[i][1], prefix = "fa"),
            popup = couche_coord[i][4]
        ).add_to(map)

    map.save("./web/map.html")

if __name__ == "__main__":
    main()