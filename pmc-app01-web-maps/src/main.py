import folium
import pandas

folium_map = folium.Map(location=(41.08961985883916, -112.0000093626548), zoom_start=5, tiles="Stamen Terrain")

volcanoes = pandas.read_csv("../materials/Volcanoes.txt")
volcano_colors = {}
color_options = sorted(folium.Icon.color_options)

feature_group = folium.FeatureGroup(name="Bunch of Markers")

template = """
<h5>Volcano&nbsp;Information</h5>
Name:&nbsp;<strong>%s</strong><br>
Elevation&nbsp;<strong>%s m</strong><br>
Type:&nbsp;<strong>%s</strong><br><br>
<a target="_blank" href="https://duckduckgo.com/?q=%s">Search on DDG</a>
"""

for index, volcano in volcanoes.iterrows():
    name = volcano["NAME"]
    elevation = volcano["ELEV"]
    v_type = volcano["TYPE"]
    location = (volcano["LAT"], volcano["LON"])

    if v_type not in volcano_colors.keys():
        volcano_colors[v_type] = color_options.pop(0)

    feature_group.add_child(
        folium.Marker(location=location,
                      popup=template % (name, elevation, v_type, name),
                      icon=folium.Icon(color=volcano_colors[v_type])))

folium_map.add_child(feature_group)

folium_map.save("../output/map.html")
