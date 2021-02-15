import folium
locations = [(('"/Drive on NBCSN', (36.1672559, -115.1485163)), 11.122634257109622), (('"/Drive on NBCSN', (36.2083012, -115.9839128)), 75.23109576969601), (('"/Drive on NBCSN', (36.4951365, -116.421881)), 116.80814846519864), (('"/Drive on NBCSN', (36.4914385, -117.10229360771876)), 176.72383580647366), (('"/Drive on NBCSN', (37.320774, -113.00484758652519)), 224.0154039643457), (('"(Mis)adventure', (34.0536909, -118.242766)), 373.83726756755664), (('"10 Films, 1 Box', (34.0536909, -118.242766)), 373.83726756755664), (('"(Mis)adventure', (34.1729044, -118.3740371)), 374.34468129903627), (('"/Drive on NBCSN', (37.84054795, -119.51658779802511)), 425.3355945906424), (('"100 Mile Meals', (37.050096, -121.9905908)), 616.5318061466241)]
user_location = (36.2672559, -115.1485163)

fl_map = folium.Map(location=list(user_location),
                    zoom_start=7,
                    tiles= "cartodbdark_matter")

fg = folium.FeatureGroup(name="Movie Map")
fg_routes = folium.FeatureGroup(name="Routes")
fg_distances = folium.FeatureGroup(name="Distances (km)")

fill_colors = ["#3B0209","#4E030C", "#6A040F","#9D0208","#D00000","#DC2F02","#E85D04","#F48C06","#FAA307","#FAA307"]
fill_colors = list(reversed(fill_colors))
for id, movie in enumerate(locations):
    distance = movie[1]
    icon = folium.features.CustomIcon("images/map_pin.png", icon_size=(30, 30))
    popup_template = f"<b>{movie[0][0]}</b> was filmed <b>{int(distance)} km </b> away"

    popup = folium.Popup(max_width=200, html =popup_template )
    fg.add_child(folium.CircleMarker(location=[movie[0][1][0], movie[0][1][1]],
                                    radius=10,
                                    popup=popup_template,
                                    fill_color=fill_colors[id],
                                    color=fill_colors[id],
                                    fill_opacity=0.5))
    fg_distances.add_child(folium.Marker(location=[movie[0][1][0], movie[0][1][1]],
                  icon=folium.DivIcon(
                      html=f"""<div style="    font-size: 1.5em;
                                color: #FFFFFF;
                                font-weight: bold;
                                filter: drop-shadow(2px 5px 12px {fill_colors[id]}); 
                                font-family: fantasy;">{"{:.0f}".format(distance)}</div>""")
                  ))

    fg_routes.add_child(folium.PolyLine([list(user_location),[movie[0][1][0], movie[0][1][1]]],
                    color= fill_colors[id]))

fg.add_child(folium.Marker(location=list(user_location),
                                 popup="Your Location",
                                 icon = icon
                                 ))
fl_map.add_child(fg)
fl_map.add_child(fg_distances)
fl_map.add_child(fg_routes)
fl_map.add_child(folium.LayerControl())
fl_map.save('map.html')