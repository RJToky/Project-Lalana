import folium
from connection.Bdd import Bdd
from dao.LalanaDAO import *
from dao.CoucheDAO import *

def place_marker(map, coord, popup = None, icon = None):
    folium.Marker(
        location = coord,
        icon = icon,
        popup = popup
    ).add_to(map)

def main():
    # -19.001707, 47.538223
    map = folium.Map(
        location = [-19.001707, 47.538223],
        zoom_start = 11
    )

    con = Bdd.connect()

    couche_coord = CoucheDAO.find_all_couche_coord(con)

    for i in range(len(couche_coord)):
        place_marker(map, [couche_coord[i][4], couche_coord[i][5]], couche_coord[i][3], folium.Icon(icon = "home"))

    map.save("index.html")

if __name__ == "__main__":
    main()