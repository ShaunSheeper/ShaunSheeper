#Import des modules
from math import trunc
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

#Retourne la latitude de la localisation dans un chaîne de caractère
def get_lat_location(i):
    location = result[f"{i}"].get('location')
    return location[0]

#Retourne la longitude de la localisation dans un chaîne de caractère
def get_long_location(i):
    location = result[f"{i}"].get('location')
    return location[1]

#Ajout d'un nouveau dictionnaire avec les informations dans le fichier json
def add_dictionary(input_name_1, input_number_1, input_address, input_description, input_size, input_summer, lat, long): #Paramètre (input_name_1, input_number_1, etc) recupérer avec la fonction 'get_user_input'
    result[str(get_elements())] = {'people_name': input_name_1, 'phone_number': input_number_1, 'address': input_address, 'description': input_description, 'size': input_size, 'summer': input_summer, 'location': [lat, long]} #Création du nouveau dictionnaire
    with open(data, 'w') as f:  
        json.dump(result, f, indent=4) #Ajout du nouveau dictionnaire

#Récupération des données entrer par l'utilisateur
def get_user_input():
    while True:
        input_name_1 = input("NOM et Prénom du propriétaire: ").title()
        answer = input("Voulez vous ajouter un second contact (oui/non) ?").capitalize()
        if answer == "OUI":
            input_name_2 = input("NOM et Prénom du propriétaire: ").title()
        else:
            input_number_1 = input("Numéro du propriétaire: ")
            if len(input_number_1) != 10:
                input_number_1 = input("Le numéro doit contenir 10 chiffres: ")
            else:
                answer = input("Voulez ajouter un second numéro (oui/non) ?")
                input_number_2 = input("Numéro du propriétaire: ")
        
        


"""
        
        input_address = input("Addresse du lieu: ")
        input_description = input("Description du lieu:")

        input_size = input("Possibilité d'acceuil (1)Troupe/Compa (2)Meute/Ronde (3)Patrouille/Equipe: ")
        if input_size == "1":
            input_size = "Troupe/Compa"
        elif input_size == "2":
            input_size = "Meute/Ronde"
        else:
            input_size = "Patrouille/Equipe"

        input_summer = input("Camp d'été (oui/non): ")
        if input_summer == "yes":
            input_summer = True
        else:
            input_summer = False

        location = geolocator.geocode(input_address)
        lat, long = location.latitude, location.longitude
        add_dictionary(input_name_1, input_number_1, input_address, input_description, input_size, input_summer, lat, long)
"""
get_user_input()


