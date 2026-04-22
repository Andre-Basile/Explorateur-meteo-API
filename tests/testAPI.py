import requests

print("--- André teste l'API JSONPlaceholder ---")

# On ajoute le chemin vers les utilisateurs (users)
url = 'https://jsonplaceholder.typicode.com/users/1'

response = requests.get(url)

print("Status code : {}".format(response.status_code))
if(response.status_code==200):
    print("Les données sont bien venues chez André")
    print("Les voici :")
    data = response.json()
    print(data)
    for keys,val in enumerate(data):
        print(f"{keys} : {val}")
else:
    print('Oups, il y a eu un problème avec la requête')
#print("Les résulats obtenus sont : \n\tcode de statut > {}\n\t réponse>{}".format(response.status_code,response.json()))
