from src.Globals import URL

def formatObject(dic):
    border = "-"*62 #fabriquer manuellement la bordure pour l'affichage
    print()
    print(border.center(120))
    #print("\t\t   ",border)
    for key,val in dic.items():
        line = f"{key:<20} >> {val:>35}"
        print(line.center(120))
    
    print(border.center(120))
    print()

def formatText(text,max_length):
    n = len(text)
    formated = '\t'
    formated += "-" * 93 #formatage de texte
    formated += '\n\t' + text + '\n'
    formated += '\t' + "-" * 93
    print(formated)
    return formated

def obtenirEntier(message = None):
    if(message == None): message = "Entrez un nombre >> "
    while(True):
        try:
            data  = int(input(message))
        except ValueError:
            print("Valeur invalide ! Rééssayez !")
        else:
            break
    return data


def fragmenter_selon_caracteres(entry,caracteres = []):
   
    result = entry.split()  # fragmente d'abord selon les espaces,ttabulations
    t = []
    for sep in caracteres:
        for i in range(len(result)):
            result[i] = result[i].split(sep)
            t += result[i]
        result = t
    return result


def objet_qui_renvoie_le_max_et_le_min_suivant_une_cle_a_valeur_numerique(table_des_objets,cle):
    if len(table_des_objets) == 0:
        return None
    #print("Comparaison en cours...avec la cle {}".format(cle))
    #print(table_des_objets)
    maximum_actuel = table_des_objets[0]
    minimum_actuel = table_des_objets[0]
    for object in table_des_objets:

        cles = object.keys()
        if cle not in cles:
            message = f"Erreur : L'objet {object} n'a pas l'attribut '{cle}' requis pour la comparaison."
            raise ValueError(message)
        if not isinstance(object[cle], (int, float)):
            raise ValueError(f"Le champ '{cle}' de l'objet doit être un nombre pour pouvoir effectuer la comparaison")
        
        if object.get(cle) > maximum_actuel.get(cle):
            maximum_actuel = object
        if object.get(cle) < minimum_actuel.get(cle):
            minimum_actuel = object
    return {
        "maximum": maximum_actuel,
        "minimum": minimum_actuel
    }


def afficher_resultat_de_comparaison(centrer_sur:int,matrice:list):
    entete = ["Ville","Température","Humidite","Vent"]
    header = f"{entete[0]:<25}{entete[1]:<18}{entete[2]:<18}{entete[3]:<8}".center(centrer_sur)
    print(header)

    barre = ("-" * (25 + 18 + 18 + 8 + 2)).center(centrer_sur)
    print(barre)

    for line in matrice:
        tmp = f"{line[0]:<25}{line[1]:<18}{line[2]:<18}{line[3]:<8}".center(centrer_sur)
        print(tmp)
    print(barre)
