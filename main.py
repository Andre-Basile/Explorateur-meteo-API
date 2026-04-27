from src.classes.Timer import time
from src.classes.UI import UI

from src.Globals import LENGTH
from src.Globals import URL
from src.Globals import alignLeft
from src.Globals import URL

from src.API_fetcher import fetchAPI
from src.API_fetcher import buildUrl

from src.Functions import formatObject
from src.Functions import formatText

from src.classes.Ville import Ville
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
UserSelect = None

while(True):
    UserSelect = UserInterface.ask("Votre choix > ")
    UserSelect = UserInterface.evaluate_choice(UserSelect) or None
    if (UserSelect is not None): break

print('\rChoix : {}'.format(UserSelect))
if not(UserSelect is None):action = UserInterface.run(UserSelect) or "Aucune section correspondante"

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