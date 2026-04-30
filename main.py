from src.classes.Timer import time
from src.classes.UI import UI

from src.Globals import LENGTH
from src.Globals import alignLeft

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
    while(True):
        UserSelect = UserInterface.ask("Votre choix > ")
        UserSelect = UserInterface.evaluate_choice(UserSelect) # renvoie <None> si rien ne correspond, sinon le numéro de la section choisie
        if (UserSelect is not None): break

    print('\rChoix : {}'.format(UserSelect))
    if not(UserSelect is None):
        action = UserInterface.run(UserSelect)
        if action is True:break

####################
UserInterface.display(date,alignLeft)
print("="*LENGTH)