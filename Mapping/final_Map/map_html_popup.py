
#? This is the final version of webmap with layer control option...
import folium
import pandas

data = pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
ele = list(data['ELEV'])
name = list(data['NAME'])

def color_producer(elevation):
    if elevation<1000:
        return "pink"
    elif 1000<=elevation<3000:
        return "lightgreen"
    else:
        return "red"

#? here we create a html var which is used for the stylizing and hyperlink the string to their web search..
html = """Volcano name:<br>
<a href="https://www.google.com/search?q=%%20%s%%20" target="_blank">%s</a><br>Height: %s m"""

map1 = folium.Map(location=[38.58,-99.09],tiles="OpenStreetMap",zoom_start=6)

fgm = folium.FeatureGroup(name= "markers")
for lt,ln,el,nam in zip (lat,lon,ele,name):
    iframe = folium.IFrame(html = html %(nam,nam,el),width= 200,height = 100)
#? above line plays a vital role in hyperlink functionality ,its a method which allow us to use html in folium..
    fgm.add_child(folium.Marker(location = [lt,ln],popup =folium.Popup(html= iframe),icon= folium.Icon(color_producer(el))))


fgp = folium.FeatureGroup(name="population density",overlay= True)
#? here the following line will create a population polygon using .json file
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']< 10000000
else 'yellow' if 10000000<= x['properties']['POP2005']<20000000 else 'red'}))

map1.add_child(fgm)
map1.add_child(fgp)
map1.add_child(folium.LayerControl())
map1.save("advance_map.html")
#! TIP: create multiple featureGroups for a better a more niche layerControl panel