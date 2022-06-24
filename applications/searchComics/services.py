import requests
import json

#APIKEYS
public_key = "eb4a3852503df3a8903874a7fe196350"
private_key = "a4993a7a7d5c59b006b59cab31812cdffd0b7879"
time_stamp = 1 

#md5 Hash Generado como indica la documentacion de la API de Marvel
api_hash = "c04fcea826451dd82c52907bc8c0a2d1"


# Funcion que hace el GET a la API de Marvel y regresa los datos especificos

def apiReq():

    uri = "https://gateway.marvel.com:443/v1/public/characters"

    url = f'{uri}?ts={time_stamp}&apikey={public_key}&hash={api_hash}'

    response = requests.get(url)

    lista_personajes = []

    # Se comprueba el estatus de la solicitud y se itera sobre la respuesta
    # para obtener los datos solicitados

    if response.status_code == 200:

        data_API = response.json() 

        for i in data_API['data']['results']:
            id = i['id']
            name = i['name']
            image = i['thumbnail']
            appearances = i['comics']['available']
            diccionario = {
                "id": id,
                "name": name,
                "image": image,
                "appearances": appearances
            }
            lista_personajes.append(diccionario)

        return lista_personajes

    else:
        mensaje = "Error al consumir al API" + response.status_code
        return mensaje