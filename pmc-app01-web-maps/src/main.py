import folium
import pandas

folium_map = folium.Map(location=(41.08961985883916, -112.0000093626548), zoom_start=5, tiles="Stamen Terrain")

volcanoes = pandas.read_csv("../materials/Volcanoes.txt")

feature_group = folium.FeatureGroup(name="Bunch of Markers")
volcano_colors = {}
color_options = sorted(folium.Icon.color_options)

for index, volcano in volcanoes.iterrows():
    volcano_type = volcano["TYPE"]

    if volcano_type not in volcano_colors.keys():
        volcano_colors[volcano_type] = color_options.pop(0)

    feature_group.add_child(
        folium.Marker((volcano["LAT"], volcano["LON"]), f"{volcano['NAME']}\n{volcano_type}",
                      icon=folium.Icon(color=volcano_colors[volcano_type])))

folium_map.add_child(feature_group)

folium_map.save("../output/map.html")
