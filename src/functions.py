from GLOBALS import URL

def formatObject(dic):
    print()
    print("-"*50)
    for key,val in dic.items():
        print(f"{key:<20} >> {val:>15}")
    print("-"*50)
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
