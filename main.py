from src.classes.timer import time
from src.classes.UI import UI

from src.GLOBALS import LENGTH
from src.GLOBALS import URL
from src.GLOBALS import alignLeft
from src.GLOBALS import URL

from src.API_fetcher import fetchAPI
from src.API_fetcher import buildUrl

from src.functions import formatObject
from src.functions import formatText

from src.classes.ville import Ville

#chargement des données depuis le .env
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")

#variables globales
UserInterface = UI()
TIME_KEEPER = time()

#Programme principal
print()
print("="*LENGTH)
####################
date = TIME_KEEPER.getFormalTime()
text = UserInterface.menu()
text = '\n' +  UserInterface.menu() + '\n'

print("Bienvenue sur Weather For All,votre assistant météo smart !")
UserInterface.display(text)
UserSelect = UserInterface.ask("Votre choix > ")
UserSelect = UserInterface.evaluateChoice(UserSelect) or "Entrée invalide" #rien que du string est retourné 

print('\rchoice : {}'.format(UserSelect))

if UserSelect == "2":
    search = UserInterface.sectionMeteo()
    print("\n\tRecherche de <{}> en cours...".format(search))
   # url = URL
   # url = 'http://localhost:3000/api/pokemons/1'
    #url = URL + "?q={}&appid={}&units=metric&lang=fr".format(search,api_key)
    url = buildUrl(search)
    response = fetchAPI(url)
    ville_recherchee = Ville(response)
    #formatObject(response["data"])
    print("\n\tRecherche de <{}> terminée !".format(search))
    formatObject(ville_recherchee.getInfos())
   # formatObject(response)
if UserSelect == "6":
    text = UserInterface.sectionAide()
    formatText(text,LENGTH)
        
####################

UserInterface.display(date,alignLeft)
print("="*LENGTH)