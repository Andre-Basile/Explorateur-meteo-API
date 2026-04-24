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
from src.classes.FileManager import File

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
UserInterface.run("1") # affiche le message de bienvenue
UserSelect = UserInterface.ask("Votre choix > ")
UserSelect = UserInterface.evaluate_choice(UserSelect) or "Entrée invalide" # rien que du string est retourné 

print('\rChoix : {}'.format(UserSelect))
action = UserInterface.run(UserSelect) or "Aucune section correspondante"

"""
if UserSelect == "2":
    search = UserInterface.section_recherche()
    print("\n\tRecherche de <{}> en cours...".format(search))
    url = buildUrl(search)
    response = fetchAPI(url)
    ville_recherchee = Ville(response)
    print("\n\tRecherche de <{}> terminée !".format(search))
    formatObject(ville_recherchee.getInfos())
if UserSelect == "6":
    text = UserInterface.sectionAide()
    formatText(text,LENGTH)
"""
####################

UserInterface.display(date,alignLeft)
print("="*LENGTH)