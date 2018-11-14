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

map = folium.Map(location=[9.977790, -84.037600], zoom_start=18, max_zoom=25, tiles="OpenStreetMap")

fg = folium.FeatureGroup(name="My Map") # Allows you to pass multiple classes (features) such as map.Marker, Map.Figure,
                                        # Map.CircleMarker, etc, to a single object feature, and then load them all using
                                        # map.add_child(fg) / fg stands for FeatureGroup. This keeps code more organized.

fg.add_child(folium.Marker(location=[9.977790, -84.037600], popup="This is my house.", icon=folium.Icon(color="green",icon_color="blue")))
fg.add_child(folium.Marker(location=[9.987790, -85.037600], popup="Far away from home", icon=folium.Icon(color="green",icon_color="blue")))

# Using above approach of adding multiple markers by repeating the method (add_child(folium.Marker(..)) is not smart nor intelligent.
# We can use for loop to add multiple markers instead.

#for coordinates in [[10.977790, -85.037600],[11.987790, -86.037600]]:
#    fg.add_child(folium.Marker(location=coordinates, popup=str(coordinates), icon=folium.Icon(color="green")))

# Even MORE efficient, we can add coordinates out from a text file, import it, and use it in folium.Marker - this by using For loop.

for lat, lon, elev, name in zip(lat,lon,elevation, name):
    # for i,j in zip([1,2,3], [4,5,6]):
    #    print(i, "and", j) -> run in terminal to understand how it works.
    iframe = folium.IFrame(html=html % (name,elev), width=200, height=200)
    #iframe = folium.IFrame(html=html_search %(name, name, elev), width=200, height=100)
    #fg.add_child(folium.Marker(location=[lat, lon], popup="Elevation: "+ str(elev) + " M", icon=folium.Icon(color="green")))
    # We may get a blank page if there are quotes(') in the strings. To avoid that change the popup argument to:
        # popup=folium.Popup(str(elev), parse_html=True))
    # However, for simple strings like elevetation values this is not a problem since there are no quotes in them.
    fg.add_child(folium.Marker(location=[lat, lon], popup=folium.Popup(iframe), icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("Map_html_pop_advanced.html")

