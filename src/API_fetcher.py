import requests
from src.Globals import URL

#récupération des données depuis le .env
from dotenv import load_dotenv
import os
load_dotenv()
#Fin

#fonctions
api_key = os.getenv("OPENWEATHER_API_KEY")
#?q={ville}&appid={votre_clé_api}&units=metric&lang=fr"
def buildUrl(ville):
    url = URL + "?q={}&appid={}&units=metric&lang=fr".format(ville,api_key)
    return url


def fetchAPI(url,params=None):
    response = None
    try:        
        response = requests.get(url,params,timeout=15) #get peut gérer les paramètres de requête directement        
        response.raise_for_status() #lève une exception pour les codes d'erreur HTTP
        return response.json()  
    except requests.exceptions.Timeout as e:
        Error_object = {
            "error" : True,
            "cause" : "Timeout"
        }
        return Error_object
    except requests.exceptions.ConnectionError as e:
        Error_object = {
            "error" : True,
            "cause" : "Connection Error"
        }
        return Error_object
    except requests.exceptions.RequestException as e:
        Error_object = {
            "error" : True,
            "cause" : "Request Exception"
        }
        return Error_object



"""
import requests

def formatObject(dic):
    print()
    print("-"*50)
    for key,val in dic.items():
        print(f"{key} : {val}")
    print("-"*50)
    print()

response = requests.get(url)

print(f"code de statut : {response.status_code}")

print(f"Headers :")
formatObject(response.headers)

if( response.status_code==200):
    print('Les données obtenues après ta requete sont les suivantes :')
    json = response.json()
    print(json["message"])
    formatObject(response.json()["data"])
else:
    print("Erreur serveur !")


"""