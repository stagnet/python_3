
# TODO Web map using folium and leaflet.js ...

import folium
import pandas
data = pandas.read_csv('Volcanoes.txt') #! read data from external csv file..
lat = list(data["LAT"])
lon = list(data["LON"])
elv = list(data['ELEV'])

map_1 = folium.Map(location= [48.7767982,-121.8109970],tiles="Stamen Terrain", zoom_start= 3)

#* creates a FeatureGroup in which we can create multiple features into our map
fg = folium.FeatureGroup(name="my marker")

for lt,ln,el in zip(lat,lon,elv): #! Remember you must use "lat" as first and "lon" as second iterable value
    #! do not try to write "lon" as first and "lat" as second
    fg.add_child(folium.Marker(location=[lt,ln],popup=(el),tooltip=("a volcanic place in america"),icon=(folium.Icon(color = 'lightblue',icon= 'info-sign'))))

map_1.add_child(fg)
map_1.save("my map2.html")