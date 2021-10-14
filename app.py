import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map([38.58, -99.09], zoom_start=5, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):  # zip method  get data by row
    iframe = folium.IFrame(html=""" <h4>Volcano information:</h4> Height: {} m""".format(str(el)), width=200,
                           height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=color_producer(el))))

map.add_child(fg)

map.save("Map1.html")
