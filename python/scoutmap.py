#Import
import folium           #pip install folium
from modules import*    #modules.py

#Définition du chemin pour sauvegarder la carte
chemin = '/home/robin/Documents/scoutmap/web/html/ScoutMaps.html'

#Définition du dictionnaire qui contient les cartes souhaités
basemaps = {
    'Google Maps': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Maps',
        overlay = True,
        control = True,
        min_zoom=7
    ),
    'Google Satellite': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Satellite',
        overlay = True,
        control = True,
        min_zoom=7
    )
}

#Création de la carte
scoutmaps = folium.Map(location=[46,2], zoom_start=7, min_zoom=7, control_scale=True)

#Ajouts des cartes souhaités à la carte de base ('Open street Map')
basemaps['Google Maps'].add_to(scoutmaps)
basemaps['Google Satellite'].add_to(scoutmaps)

#Ajout d'un bouton permettant de changer de style de carte
scoutmaps.add_child(folium.LayerControl())

#Boucle qui itère dans le fichier data.json pour afficher des marqueurs contenant des informations sur la carte
for _ in range(get_elements()):     #Récupère la longeur du dictionnaire, la valeur récupérer permet de définir combien de fois la boucle itère

    html = f"{get_addresse(_)}<br>{get_people_name(_)}<br>{get_people_phone_number(_)}<br>{get_camp_size(_)}<br>{get_summer_camp(_)}"   #Stock dans la variable une chaîne de caratère contenant plusieurs informations
    iframe = folium.IFrame(html)

    popup = folium.Popup(iframe, min_width=300, max_width=500)      #Définition des dimmension de 'iFrame
                        
    folium.Marker([get_lat_location(_), get_long_location(_)], popup = popup, tooltip=get_addresse(_)).add_to(scoutmaps) #Place les marqueurs sur la carte

scoutmaps.save(chemin) #Sauvegarde de la carte
