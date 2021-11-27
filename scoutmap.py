import folium
from pprint import pprint
from modules import*

basemaps = {
    'Google Maps': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Maps',
        overlay = True,
        control = True
    ),
    'Google Satellite': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Satellite',
        overlay = True,
        control = True
    )
}

scoutmaps = folium.Map(location=[46,2], zoom_start=7, min_zoom=7, control_scale=True)
basemaps['Google Maps'].add_to(scoutmaps)
basemaps['Google Satellite'].add_to(scoutmaps)
scoutmaps.add_child(folium.LayerControl())


for _ in range(get_elements()):
    print(_)
    html = f"{get_addresse(_)}<br>{get_people_name(_)}<br>{get_people_phone_number(_)}<br>{get_camp_size(_)}<br>{get_summer_camp(_)}"

    iframe = folium.IFrame(html)
    popup = folium.Popup(iframe, min_width=300, max_width=500)
                        
    folium.Marker([get_lat_location(_), get_long_location(_)], popup = popup, tooltip=get_addresse(_)).add_to(scoutmaps)

scoutmaps.save('scoutmaps.html')
