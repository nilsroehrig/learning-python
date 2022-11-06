import folium
import pandas

folium_map = folium.Map(location=(41.08961985883916, -112.0000093626548), zoom_start=5, tiles="Stamen Terrain")

volcanoes = pandas.read_csv("../materials/Volcanoes.txt")
feature_group = folium.FeatureGroup(name="Bunch of Markers")

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


for index, volcano in volcanoes.iterrows():
    name = volcano["NAME"]
    elevation = volcano["ELEV"]
    v_type = volcano["TYPE"]
    location = (volcano["LAT"], volcano["LON"])

    feature_group.add_child(
        folium.CircleMarker(location=location,
                            popup=template % (name.replace(" ", "&nbsp;"), elevation, v_type, name),
                            fill=True,
                            color="white",
                            fill_color=get_volcano_color(v_type),
                            fill_opacity=0.65,
                            radius=8,
                            weight=2))

folium_map.add_child(feature_group)

folium_map.save("../output/map.html")
