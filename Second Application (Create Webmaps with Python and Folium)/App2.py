import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
# On terminal we can run $data.columns to check column names.


lat = list(data["LAT"])
lon = list(data["LON"])
elevation = list(data["ELEV"])
name = list(data["NAME"])


html = """
<h4>Volcano Information: </h4>
Name: %s<br>
Height: %s M
"""
html_search = """
Volcano name:<br>
<a href='https://www.google.com/search?q"%s"' target="_blank">%s</a><br>
Height: %s M
"""

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[9.977790, -84.037600], zoom_start=18, max_zoom=25, tiles="OpenStreetMap")

fg_volcanoes = folium.FeatureGroup(name="Volcanoes") # Allows you to pass multiple classes (features) such as map.Marker, Map.Figure,
                                        # Map.CircleMarker, etc, to a single object feature, and then load them all using
                                        # map.add_child(fg) / fg stands for FeatureGroup. This keeps code more organized.
fg_population = folium.FeatureGroup(name="Population")
#fg.add_child(folium.Marker(location=[9.977790, -84.037600], popup="This is my house.", icon=folium.Icon(color="green",icon_color="blue")))
#fg.add_child(folium.Marker(location=[9.987790, -85.037600], popup="Far away from home", icon=folium.Icon(color="green",icon_color="blue")))

# Using above approach of adding multiple markers by repeating the method (add_child(folium.Marker(..)) is not smart nor intelligent.
# We can use for loop to add multiple markers instead.

#for coordinates in [[10.977790, -85.037600],[11.987790, -86.037600]]:
#    fg.add_child(folium.Marker(location=coordinates, popup=str(coordinates), icon=folium.Icon(color="green")))

# Even MORE efficient, we can add coordinates out from a text file, import it, and use it in folium.Marker - this by using For loop.
fg_population.add_child(folium.GeoJson(data=open("world.json", 'r', encoding='utf-8-sig').read(), style_function=lambda x:{'fillColor':'green'
if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005']  < 20000000 else 'red'}))
# x represents "features" key in .json file.
# fillColor attribute is an attribute from JavaScript code. Remember this is passed in the backend to JS.
# Here full explanation:
'''
The dictionary is then used on the background by Javascript to build the map.
Things like fillColor are Javascript code. Javascript expects a JSON string with such options (colors) to make the map.
The x part seems like a blackbox because it is hardcoded in folium. The x basically iterates through the JSON data going over all features keys.
The iteration is implemented inside folium, that's why it looks like magic here.

We can see the structure of world.json file, specifically on 'features' key by running on terminal: "cat world.json | jq '.features' | less"
'''

for lat, lon, elev, name in zip(lat,lon,elevation, name):
    # for i,j in zip([1,2,3], [4,5,6]):
    #    print(i, "and", j) -> run in terminal to understand how it works.
    iframe = folium.IFrame(html=html % (name,elev), width=200, height=200)
    #iframe = folium.IFrame(html=html_search %(name, name, elev), width=200, height=100)
    #fg.add_child(folium.Marker(location=[lat, lon], popup="Elevation: "+ str(elev) + " M", icon=folium.Icon(color="green")))
    # We may get a blank page if there are quotes(') in the strings. To avoid that change the popup argument to:
        # popup=folium.Popup(str(elev), parse_html=True))
    # However, for simple strings like elevetation values this is not a problem since there are no quotes in them
    fg_volcanoes.add_child(folium.CircleMarker(location=[lat, lon], radius=8, popup=folium.Popup(iframe),
                fill_color=color_producer(elev), color='grey', fill_opacity=0.7))

map.add_child(fg_volcanoes) # Feature group for volcanoes
map.add_child(fg_population) # Feature group for population

map.add_child(folium.LayerControl())

map.save("Map_html_pop_advanced.html")
