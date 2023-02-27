import folium
from connection.Bdd import Bdd
from dao.LalanaDAO import *
from dao.CoucheDetailDAO import *

def main():
    # -19.001707, 47.538223
    map = folium.Map(
        location = [-19.001707, 47.538223],
        zoom_start = 11
    )

    con = Bdd.connect()

    couche_detail = CoucheDetailDAO.find_all(con)

    for i in range(len(couche_detail)):
        folium.Marker(
            location = [couche_detail[i][2], couche_detail[i][3]],
            icon = folium.Icon(icon = couche_detail[i][1], prefix = "fa", color = "green"),
            popup = couche_detail[i][4]
        ).add_to(map)

        # folium.Circle(
        #     location = [couche_detail[i][2], couche_detail[i][3]],
        #     radius = 1000,
        #     fill = True,
        #     color = "green"
        # ).add_to(map)

    map.save("./web/map.html")

if __name__ == "__main__":
    main()