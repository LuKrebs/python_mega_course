import folium as fl
import pandas as pd

def color_generator(elevation):
    elevation = int(elevation)
    if elevation < 1000:
        return "green"
    elif elevation >= 1000 and elevation < 3000:
        return "orange"
    else:
        return "red"

style_function = lambda x: {"fillColor": "green" if x['properties']['POP2005'] < 30000000
else 'orange' if 30000000 <= x['properties']['POP2005'] < 100000000 else "red"}

data = pd.read_csv("Volcanoes_USA.txt")
lat = data["LAT"]
lon = data["LON"]
elev = data["ELEV"]

base_map = fl.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")

fgv = fl.FeatureGroup(name="Vulcanos Map")
for lt, ln, el in zip(lat,lon,elev):
    fgv.add_child(fl.Marker(location=[lt, ln], popup="{} m".format(el), icon=fl.Icon(color=color_generator(el))))
    # fg.add_child(fl.Circle(location=[lt, ln], popup="{} m".format(el), color=color_generator(el), fill_color=color_generator(el), radius = 50, fill_opacity=0.7))

fgp = fl.FeatureGroup(name="Population")
fgp.add_child(fl.GeoJson(data=(open("world.json", encoding="utf-8-sig").read()),
style_function=style_function))

base_map.add_child(fgv)
base_map.add_child(fgp)
base_map.add_child(fl.LayerControl())
base_map.save("map.html")
