from src.GLOBALS import LENGTH
from src.GLOBALS import HELP

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

    def evaluateChoice(self,entry):
        if entry in sections_numbers_codes:
            return str(entry)
        else:
            for section in sections:
                if(entry.lower() in section.lower()):
                    return str(sections.index(section) + 1) #les indices commencent par 0
            else:
                return None
    
    def sectionMeteo(self,message = "Entrez le terme de recherche(la ville) > "):
        search =  input(message)
        return search
    
    def sectionAide(self):
        return HELP
    
    def sectionQuitter(self):
        response = input('Voulez-vous vraiment quitter ? (oui/non) > ')
        if "oui" in response.lower():
            return True
        return False