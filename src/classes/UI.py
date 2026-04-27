from pathlib import Path

from src.Globals import LENGTH
from src.Globals import HELP
from src.Globals import WELCOME

#pour les recherches de la section 2
from src.API_fetcher import fetchAPI
from src.API_fetcher import buildUrl
from src.classes.Ville import Ville
from src.classes.FileManager import File

from src.Functions import formatObject
from src.Functions import formatText
from src.Functions import fragmenter_selon_caracteres
from src.Functions import objet_qui_renvoie_le_max_et_le_min_suivant_une_cle_a_valeur_numerique
from src.Functions import afficher_resultat_de_comparaison

from src.Globals import DATAS_FOLDER_NAME
from src.Globals import HISTORIC_FILE_NAME



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
        souligneur = "     "
        for section in sections:
            text += str(i) + '.' + section + "     "
            souligneur += ('-'*(len(section)+2)) + "     "
            i += 1
        text += '\n' + souligneur
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
    
    def chemin_vers_le_fichier_historique(self):
        #accéder au dossier du fichier <historic.json>
        dossier_courant = Path(__file__).parent # parent : classes
        parent_du_dossier_courant = dossier_courant.parent # parent : src
        parent_du_parent_du_dossier_courant = parent_du_dossier_courant.parent # parent : dossier du projet
        chemin_historique = parent_du_parent_du_dossier_courant / DATAS_FOLDER_NAME / HISTORIC_FILE_NAME
        return chemin_historique

    def section_accueil(self):
        formatText(WELCOME,LENGTH)

    def section_recherche(self,message = "Entrez le terme de recherche(la ville) > "):
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

        # demander à l'utilisateur s'il veut enregistrer cette recherche dans son historique
        enregistrer = self.ask_for_saving()

        if(enregistrer):
            # enregistrer la recherche dans l'historique de l'utilisateur
            chemin_historique = self.chemin_vers_le_fichier_historique()
            historic_file = File("Historique de recherches",chemin_historique)
            historic_file.write(ville_recherchee.toJSON())
            self.display("Recherche enregistrée !")
        

    def section_comparaison(self):
        results = []
        matrice_pour_affichage_resultat = []
        search = input('Entrez les noms des villes à comparer, séparés par une virgule ou un espace > ')
        villes_a_comparer = fragmenter_selon_caracteres(search, [','])
        chemin_historique = self.chemin_vers_le_fichier_historique()
        historic_file = File("Historique de recherches",chemin_historique)
        # Logique pour comparer les villes
        """
         - on lance de nouvelles recherches pour toutes les villes entrées par l'utilisateur 
        """

        donnes_temporaires_utilisees_pour_faute_de_connexion = [
    {
        "code_pays": "JP",
        "localisation": "Pr\u00e9fecture de Tokyo",
        "temperature": 12.42,
        "seaLevel": 1020,
        "humidite": 72,
        "ressenti": 11.6,
        "ciel": "nuageux",
        "vent": 7.72,
        "nuages": 75,
        "fuseau": 32400
    },
    {
        "code_pays": "US",
        "localisation": "Portland",
        "temperature": 9.3,
        "seaLevel": 1014,
        "humidite": 53,
        "ressenti": 9.3,
        "ciel": "ciel d\u00e9gag\u00e9",
        "vent": 0.45,
        "nuages": 0,
        "fuseau": -25200
    },
    {
        "code_pays": "BJ",
        "localisation": "Parakou",
        "temperature": 28.37,
        "seaLevel": 1010,
        "humidite": 64,
        "ressenti": 30.54,
        "ciel": "partiellement nuageux",
        "vent": 4.5,
        "nuages": 25,
        "fuseau": 3600
    },
    {
        "code_pays": "BJ",
        "localisation": "Cotonou",
        "temperature": 29.99,
        "seaLevel": 1010,
        "humidite": 79,
        "ressenti": 36.99,
        "ciel": "partiellement nuageux",
        "vent": 5.14,
        "nuages": 40,
        "fuseau": 3600
    }
]
        i = 0

        for terme in villes_a_comparer:
            url = buildUrl(terme)
           # response = fetchAPI(url)
           # response = donnes_temporaires_utilisees_pour_faute_de_connexion[i]
            response = fetchAPI(url)
            i+=1
            #print("respose.ge(erreur) = {}".format(response.get("error")))
            if (response.get("error") is None):
                #loc,temp,hum,vent
                #tmp = Ville(response).toJSON()
                tmp = Ville(response).toJSON()
              #  print("Taille de tmp : {}".format(len(tmp)))
               # print("tmp est : ",tmp)
                #tmp = response
                extracted_informations = {
                    "localisation" : tmp.get("localisation"),
                    "temperature" : tmp.get("temperature"),
                    "humidite" : tmp.get("humidite"),
                    "vent" : tmp.get("vent")
                }
                results.append(extracted_informations)
                line = [tmp.get("localisation"),str(tmp.get("temperature")) + "°C",str(tmp.get("humidite")) + "%",str(tmp.get("vent")) + "m/s"]
                matrice_pour_affichage_resultat.append(line)

        func = objet_qui_renvoie_le_max_et_le_min_suivant_une_cle_a_valeur_numerique
        critere_temperature = func(results,"temperature")
        critere_humidite = func(results,"humidite")
        critere_vent = func(results,"vent")

        #print("critere temperature : {}".format(critere_temperature))
        la_plus_chaude = critere_temperature.get("maximum")
        la_plus_humide = critere_humidite.get("maximum")
        plus_venteux = critere_vent.get("maximum")
        la_plus_fraiche = critere_temperature.get("minimum")
            # print("Le type de {} est {} et villes a comparer est : {}".format(terme,type(terme),villes_a_comparer))
          #  ville = historic_file.rechercher(terme)
            # print(ville)
          #  if ville is None:
                # on lance la recherche de la ville via l'API et on l'enregistre
           #     url = buildUrl(terme)
           #     response = fetchAPI(url)
            #    print(response)

           #     if (response.get("error") is None): # la recherche a abouti
           #         ville_recherchee = Ville(response)
           # else:
            #    results.append(ville)
       # print(results)
       # print("La plus chaude est {},\n la plus humide est {},\n le plus venteux est {}\n et la plus fraîche est {}".format(la_plus_chaude.get("localisation"),la_plus_humide.get("localisation"),plus_venteux.get("localisation"),la_plus_fraiche.get("localisation")))
       # print("TEST DE LA NOUVELLE FONCTION D'AFFICHAGE...")
        print("\n\n")
        afficher_resultat_de_comparaison(120,matrice_pour_affichage_resultat)
       # print("FIN DU TEST !")
        
        result = {
            "Plus chaude" : la_plus_chaude.get("localisation"),
            "Plus fraiche" : la_plus_fraiche.get("localisation"),
            "Plus humide" : la_plus_humide.get("localisation"),
            "Plus venteux" : plus_venteux.get("localisation")
        }

        formatObject(result)


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

    def ask_for_saving(self,message = "Voulez-vous enregistrer cette recherche dans votre historique ? (oui/non) > "):
        response = input(message)
        if "oui" in response.lower():
            return True
        return False