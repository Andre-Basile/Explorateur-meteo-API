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
from src.Functions import afficher_historique

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
            solution = response.get("solution")
            print("Votre recherche n'a pas abouti.{}".format(solution))
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
        else:
            self.display("Recherche non enregistrée !")
        

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

        i = 0

        for terme in villes_a_comparer:
            url = buildUrl(terme)
           # response = donnes_temporaires_utilisees_pour_faute_de_connexion[i]
            response = fetchAPI(url)
            #print("response : {}".format(response))
            i+=1
            if (response.get("error") is None):
                tmp = Ville(response).toJSON()
                extracted_informations = {
                    "localisation" : tmp.get("localisation"),
                    "temperature" : tmp.get("temperature"),
                    "humidite" : tmp.get("humidite"),
                    "vent" : tmp.get("vent")
                }
                results.append(extracted_informations)
                line = [tmp.get("localisation"),str(tmp.get("temperature")) + "°C",str(tmp.get("humidite")) + "%",str(tmp.get("vent")) + "m/s"]
                matrice_pour_affichage_resultat.append(line)
            
            if not (response.get("error") is None):
                solution = response.get("solution") # obtenir la solution au problème
                #print("Votre recherche n'a pas abouti.{}".format(solution))
                # return
                

        if len(results) == 0:
            print("Aucun résultat trouvé pour les villes entrées !")
            return
        func = objet_qui_renvoie_le_max_et_le_min_suivant_une_cle_a_valeur_numerique
        critere_temperature = func(results,"temperature")
        critere_humidite = func(results,"humidite")
        critere_vent = func(results,"vent")


        la_plus_chaude = critere_temperature.get("maximum")
        la_plus_humide = critere_humidite.get("maximum")
        plus_venteux = critere_vent.get("maximum")
        la_plus_fraiche = critere_temperature.get("minimum")
        print("\n\n")
        afficher_resultat_de_comparaison(120,matrice_pour_affichage_resultat)

        
        result = {
            "Plus chaude" : la_plus_chaude.get("localisation"),
            "Plus fraiche" : la_plus_fraiche.get("localisation"),
            "Plus humide" : la_plus_humide.get("localisation"),
            "Plus venteux" : plus_venteux.get("localisation")
        }

        formatObject(result)


    def section_historique(self):
        
        chemin_historique = self.chemin_vers_le_fichier_historique()
        historic_file = File("Historique de recherches",chemin_historique)
        response = historic_file.read()       

        entete = ["Date","Code pays","Ville","Température","Humidité","Vent","Fuseau horaire"]
        cles_cibles = ["date","code_pays","localisation","temperature","humidite","vent","fuseau"]
        
        print("\t Historique des recherches...\n")
        afficher_historique(response,entete,cles_cibles,120)

    def section_statistiques(self):
        chemin_historique = self.chemin_vers_le_fichier_historique()
        historic_file = File("Historique de recherches",chemin_historique)
        noms_villes_consultees = historic_file.obtenir_villes_distinctes_enregistrees()

        dic = {}
        for ville in noms_villes_consultees:
            dic[ville] = f"(Consulté {historic_file.obtenir_nombre_de_consultation(ville)} fois)"


        print(" " * 28,"Les villes que vous avez consultées...")
        formatObject(dic,False)
        print(f"\t\tObtenir les statistiques de quelle ville ?")
        ville_cible = input("\t\t> ")

        valid = False
        for ville in noms_villes_consultees:
            if ville_cible.lower() in ville.lower():
                ville_cible = ville
                valid = True
        if not valid:
            print("Vous n'avez pas recherché cette ville <{}> auparavant ! ".format(ville_cible).center(LENGTH))
            return None
        # on continue si la réponse est valide, c'est-à-dire parmi les villes auparavant recherchées
        text = f"Affichage des stats de <<{ville_cible}>>"
        print()
        print(text.center(LENGTH))
        print(("-" * len(text)).center(LENGTH))

        occurences_de_la_ville_ciblee = historic_file.rechercher_toutes_les_occurences(ville_cible)
        tableau = []
        entete = ["Dates","Températures","Degrés d'humidité"]
        entete = f"| {entete[0]:<30}{entete[1]:<20}{entete[2]:>20} |".center(LENGTH)
        tableau.insert(0,entete)
        for occurence in occurences_de_la_ville_ciblee:
            date = occurence.get("date")
            temperature = "   " + str(round(occurence.get("temperature"), 2)) + "°C"
            humidite = str(round(occurence.get("humidite"), 2)) + "%  "
            tmp = f"| {date:<30}{temperature:<20}{humidite:>20} |".center(LENGTH)
            tableau.append(tmp)

        underliner1 = ("-" * (30 + 20 + 20 + 4))
        underliner1 = f"{underliner1}".center(LENGTH)
        
        underliner2 = ("-" * (30 + 20 + 20))
        underliner2 = f"| {underliner2} |".center(LENGTH)

        tableau.insert(0,underliner1)
        tableau.insert(2,underliner2)
        tableau.append(underliner1)
        for l in tableau:print(l)

        # calcul de la température moyenne et du degré moyen d'humidité
        temperatures = []
        degres_humidite = []
        for occr in occurences_de_la_ville_ciblee:
            temperatures.append(float(occr.get("temperature")))
            degres_humidite.append(float(occr.get("humidite")))

        temperature_moyenne = round( sum(temperatures) / len(occurences_de_la_ville_ciblee), 2) # sum() est natif de Python
        humidite_moyenne =  round( sum(degres_humidite) / len(occurences_de_la_ville_ciblee), 2)
        
        temperature_min = min(temperatures)
        temperature_max = max(temperatures)

        humidite_min = min(degres_humidite)
        humidite_max = max(degres_humidite)
        
        infos_temperature = {
            "Température moyenne" : str(temperature_moyenne) + "°C",
            "Température minimale" : str(temperature_min) + "°C",
            "Température maximale" : str(temperature_max) + "°C"
        }

        infos_humidite = {
            "Humidité moyenne" : str(humidite_moyenne) + "°C",
            "Humidité minimale" : str(humidite_min) + "%",
            "Humidité maximale" : str(humidite_max) + "%"
        }

        formatObject(infos_temperature,False)
        formatObject(infos_humidite,False)


    def section_aide(self):
        formatText(HELP,LENGTH)
    
    def section_quitter(self):
        response = input('Voulez-vous vraiment quitter ? (oui/non) > ')
        if "oui" in response.lower():
            print("Weather For All vous dit au revoir !")
            return True
        return False
   
    def run(self,user_choice):
         # section correspondante à la sélection de l'utilisateur
         fonction_correspondante = self.menu_sections.get(user_choice)
         return fonction_correspondante()

    def ask_for_saving(self,message = "Voulez-vous enregistrer cette recherche dans votre historique ? (oui/non) > "):
        response = input(message)
        if "oui" in response.lower():
            return True
        return False