import requests

def formatObject(dic):
    print()
    print("-"*50)
    for key,val in dic.items():
        print(f"{key} : {val}")
    print("-"*50)
    print()

url = 'http://localhost:3000/api/pokemons/'
print()
n = input("Salut,quel pokméon vex-tu ? >")
url += n
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
