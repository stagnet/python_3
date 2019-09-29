
# TODO Web map using folium and leaflet.js ...

import folium
import pandas
data = pandas.read_csv('Volcanoes.txt')  #! read data from external csv file..
lat = list(data["LAT"])
lon = list(data["LON"])
elv = list(data['ELEV'])


# * this function is used for converting pointers colors on the basis of their elevation..
def color_marker(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation <=  3000:
        return "lightblue"
    else:
        return "lightred"


map_1 = folium.Map(location=[38.04, -99.09],tiles="OpenStreetMap", zoom_start=7)

# * creates a FeatureGroup in which we can create multiple features into our map
fg = folium.FeatureGroup(name="my marker")

# ! Remember you must use "lat" as first and "lon" as second iterable value#! do not try to write 
# !"lon" as first and "lat" as second
for lt, ln, el in zip(lat, lon, elv):
    
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+"m", tooltip=("a volcanic place in america"), icon=(folium.Icon(color_marker(el)))))

map_1.add_child(fg)
map_1.save("my map1.html")
