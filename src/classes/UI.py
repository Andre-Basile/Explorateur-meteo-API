from pathlib import Path

from src.GLOBALS import LENGTH
from src.GLOBALS import HELP
from src.GLOBALS import WELCOME

#pour les recherches de la section 2
from src.API_fetcher import fetchAPI
from src.API_fetcher import buildUrl
from src.classes.ville import Ville
from src.classes.FileManager import File

from src.functions import formatObject
from src.functions import formatText

from src.GLOBALS import DATAS_FOLDER_NAME
from src.GLOBALS import HISTORIC_FILE_NAME


sections = [
    'Accueil',
    'Recherche météo',
    'Comparaison de villes',
    'Historique',
    'Statistiques',
    'Aide',
    'Quitter'
]


sections_numbers_codes = ['1', '2', '3', '4', '5', '6', '7']

class UI:    

    def __init__(self,name = "Weather For All"):
        self.appname = name
        self.menu_sections = {   #objet pour mapper les fonctions avec leurs numéros
            "1" : self.section_accueil,
            "2": self.section_recherche,
            "3": self.section_comparaison,
            "4": self.section_historique,
            "5": self.section_statistiques,
            "6": self.section_aide,
            "7": self.section_quitter,
        }

    def display(self,data,align = None):
        if(align) : 
            n = len(data)
            text = " " * (LENGTH - n - 5) + data
            print(text)
        else:
            print(data)

    def menu(self):
        text = " " * 5
        i = 1
        underliner = "     "
        for section in sections:
            text += str(i) + '.' + section + "     "
            underliner += ('-'*(len(section)+2)) + "     "
            i += 1
        text += '\n' + underliner
        return text

    def ask(self,message):
        res = input(message)
        return res

    def evaluate_choice(self,entry):
        if entry in sections_numbers_codes:
            return str(entry)
        else:
            for section in sections:
                if(entry.lower() in section.lower()):
                    return str(sections.index(section) + 1) #les indices commencent par 0
            else:
                return None
    

    def section_accueil(self):
        formatText(WELCOME,LENGTH)

    def section_recherche(self,message = "Entrez le terme de recherche(la ville) > "):
        trouve = False
        search =  input(message)
        print("\n\tRecherche de <{}> en cours...".format(search))
        url = buildUrl(search)
        response = fetchAPI(url)

        if not (response.get("error") is None):
            print("Votre recherche n'a pas abouti")
            return
        
        ville_recherchee = Ville(response)
        print("\n\tRecherche de <{}> terminée !".format(search))
        formatObject(ville_recherchee.getInfos())

        # enregistrer la recherche dans l'historique de l'utilisateur

        #accéder au dossier de <historic.json>
        dossier_courant = Path(__file__).parent # parent : classes
        parent_du_dossier_courant = dossier_courant.parent # parent : src
        parent_du_parent_du_dossier_courant = parent_du_dossier_courant.parent # parent : dossier du projet
        chemin_historique = parent_du_parent_du_dossier_courant / DATAS_FOLDER_NAME / HISTORIC_FILE_NAME
        print("le chemin de l'historique est : {}".format(chemin_historique))
        historic_file = File("Historique de recherches",chemin_historique)
        historic_file.write(ville_recherchee.toJSON())


    def section_comparaison(self):
        pass
        
    def section_historique(self):
        pass

    def section_statistiques(self):
        pass

    def section_aide(self):
        formatText(HELP,LENGTH)
    
    def section_quitter(self):
        response = input('Voulez-vous vraiment quitter ? (oui/non) > ')
        if "oui" in response.lower():
            print("Weather For All vous dit au revoir !")
            return True
        return False
   
    def run(self,user_choice):
         #section correspondante à la sélection de l'utilisateur
         fonction_correspondante = self.menu_sections.get(user_choice)
         fonction_correspondante()