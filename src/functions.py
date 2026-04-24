from src.GLOBALS import URL

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


def getPath(filename):    
    pass
