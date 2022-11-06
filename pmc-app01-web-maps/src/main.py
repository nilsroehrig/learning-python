import folium
import pandas

folium_map = folium.Map(location=(41.08961985883916, -112.0000093626548), zoom_start=5, tiles="Stamen Terrain")

volcanoes = pandas.read_csv("../materials/Volcanoes.txt")
volcano_markers = folium.FeatureGroup(name="Volcanoes")

template = """
<h5>Volcano&nbsp;Information</h5>
Name:&nbsp;<strong>%s</strong><br>
Elevation&nbsp;<strong>%s m</strong><br>
Type:&nbsp;<strong>%s</strong><br><br>
<a target="_blank" href="https://duckduckgo.com/?q=%s">Search on DDG</a>
"""

volcano_colors = {}
color_options = sorted(
    [c for c in folium.Icon.color_options if c not in ('lightred',
                                                       'lightgreen',
                                                       'lightblue',
                                                       'lightgray')])


def get_volcano_color(volcano_type):
    if volcano_type not in volcano_colors.keys():
        volcano_colors[volcano_type] = color_options.pop(0)
    return volcano_colors[volcano_type]


def population_color(population_count):
    color = "red"

    if population_count < 5000000:
        color = "blue"
    elif population_count < 20000000:
        color = "green"
    elif population_count < 50000000:
        color = "yellow"
    elif population_count < 200000000:
        color = "orange"

    return color


for index, volcano in volcanoes.iterrows():
    name = volcano["NAME"]
    elevation = volcano["ELEV"]
    v_type = volcano["TYPE"]
    location = (volcano["LAT"], volcano["LON"])

    volcano_markers.add_child(
        folium.CircleMarker(location=location,
                            popup=template % (name.replace(" ", "&nbsp;"), elevation, v_type, name),
                            fill=True,
                            color="white",
                            fill_color=get_volcano_color(v_type),
                            fill_opacity=0.65,
                            radius=8,
                            weight=2))

population = folium.FeatureGroup(name="Population")

with open("../materials/world.json", mode="r", encoding="utf-8-sig") as world:
    population.add_child(folium.GeoJson(
        world.read(),
        style_function=lambda c: {
            "fillColor": population_color(c["properties"]["POP2005"])
        }))

folium_map.add_child(population)
folium_map.add_child(volcano_markers)

folium_map.save("../output/map.html")
