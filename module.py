#Import des modules
import os
import json
from geopy.geocoders import Nominatim   #pip install geopy

geolocator = Nominatim(user_agent='ScoutMaps')  #Nominatim exige que cette valeur soit définie sur le nom de l'application. L'objectif est de pouvoir limiter le nombre de demandes par candidature

CUR_DIR = os.path.dirname(os.path.abspath(__file__)) #Récupère chemin du dossier parent du fichier actuel (ici : '~/Documents/test')
data = os.path.join(CUR_DIR, "data.json") #Créer le chemin pour le fichier.json avec CUR_DIR ('~/Documents/test/data.json')

#Récupération du contenu de fichier json dans un dictionnaire ('result')
with open(data, "r") as f:
    result = json.load(f)

###############################################################################################################################################################################################################################
#Définition des fonctions : 
###############################################################################################################################################################################################################################

#Retourne la longeur du dictionnaire 'result'
def get_elements():
    return len(result)  #Retourne la longeur par ex: le dictionnaire contient les clés (0, 1, 2). Retourne 3. Cette valeur servira à créer un nouveau dictionnaire par la suite

#Retourne le nom de la personne dans une chaîne de caractère
def get_people_name(i):
    return result[f"{i}"].get('people_name')

#Retourne le numéro de téléphone de la personne dans une chaîne de caractère
def get_people_phone_number(i):
    return result[f"{i}"].get('phone_number')

#Retourne l'addresse de la personne dans une chaîne de caractère
def get_addresse(i):
    return result[f"{i}"].get('address')

#Retourne la taille de l'unité pouvant camper sur le lieu dans une chaîne de caractère
def get_camp_size(i):
    size = result[f"{i}"].get('size')
    return f"Camp pour: {size}"

#Retourne si le lieu est adapté au camp d'été dans une chaîne de caractère
def get_summer_camp(i):
    summer = result[f"{i}"].get('summer')
    return f"Camp d'été: {summer}"    

#Retourne la latitude de la localisation dans un chaîne de caractère
def get_lat_location(i):
    location = result[f"{i}"].get('location')
    return location[0]

#Retourne la longitude de la localisation dans un chaîne de caractère
def get_long_location(i):
    location = result[f"{i}"].get('location')
    return location[1]

#Ajout d'un nouveau dictionnaire avec les informations dans le fichier json
def add_dictionary(input_name, input_number, input_address, input_description, input_size, input_summer, lat, long): #Paramètre (input_name, input_number, etc) recupérer avec la fonction 'get_user_input'
    result[str(get_elements())] = {'people_name': input_name, 'phone_number': input_number, 'address': input_address, 'description': input_description, 'size': input_size, 'summer': input_summer, 'location': [lat, long]} #Création du nouveau dictionnaire
    with open(data, 'w') as f:  
        json.dump(result, f, indent=4) #Ajout du nouveau dictionnaire

#Récupération des données entrer par l'utilisateur
def get_user_input():
    input_name = input("NOM et Prénom du propriétaire: ").title()
    input_number = input("Numéro de téléphone du propriétaire: ")
    input_address = input("Addresse du lieu: ").title()
    input_description = input("Description du lieu:").capitalize()
    input_size = input("Possibilité d'acceuil (1)Troupe/Compa (2)Meute/Ronde (3)Patrouille/Equipe: ")
    input_summer = input("Camp d'été (oui/non): ")
    location = geolocator.geocode(input_address)
    lat, long = location.latitude, location.longitude
    add_dictionary(input_name, input_number, input_address, input_description, input_size, input_summer, lat, long)


